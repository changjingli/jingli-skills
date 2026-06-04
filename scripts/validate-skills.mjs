import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const skillsDir = path.join(root, "skills");
const namePattern = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n?/);
  if (!match) {
    throw new Error("missing YAML frontmatter");
  }

  const data = {};
  for (const rawLine of match[1].split("\n")) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#")) continue;

    const keyMatch = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (!keyMatch) {
      throw new Error(`unsupported frontmatter line: ${rawLine}`);
    }

    const [, key, rawValue] = keyMatch;
    data[key] = rawValue.replace(/^["']|["']$/g, "").trim();
  }

  return data;
}

async function listSkillDirs() {
  const entries = await readdir(skillsDir);
  const dirs = [];

  for (const entry of entries) {
    const fullPath = path.join(skillsDir, entry);
    const entryStat = await stat(fullPath);
    if (entryStat.isDirectory()) {
      dirs.push(entry);
    }
  }

  return dirs.sort();
}

async function validateSkill(dirName) {
  const skillPath = path.join(skillsDir, dirName);
  const skillMdPath = path.join(skillPath, "SKILL.md");
  const manifestPath = path.join(skillPath, "manifest.json");
  const errors = [];

  if (!namePattern.test(dirName)) {
    errors.push("folder name must be lower hyphen-case");
  }

  let content = "";
  try {
    content = await readFile(skillMdPath, "utf8");
  } catch {
    errors.push("missing SKILL.md");
    return errors;
  }

  let frontmatter;
  try {
    frontmatter = parseFrontmatter(content);
  } catch (error) {
    errors.push(error.message);
    return errors;
  }

  if (!frontmatter.name) {
    errors.push("frontmatter.name is required");
  } else if (!namePattern.test(frontmatter.name)) {
    errors.push("frontmatter.name must be lower hyphen-case");
  } else if (frontmatter.name !== dirName) {
    errors.push(`frontmatter.name must match folder name (${dirName})`);
  }

  if (!frontmatter.description) {
    errors.push("frontmatter.description is required");
  } else if (frontmatter.description.length > 1024) {
    errors.push("frontmatter.description must be 1024 characters or fewer");
  } else if (frontmatter.description.includes("<") || frontmatter.description.includes(">")) {
    errors.push("frontmatter.description cannot contain angle brackets");
  }

  try {
    const manifestRaw = await readFile(manifestPath, "utf8");
    const manifest = JSON.parse(manifestRaw);

    if (manifest.name !== dirName) {
      errors.push(`manifest.name must match folder name (${dirName})`);
    }

    if (manifest.entry && manifest.entry !== "SKILL.md") {
      errors.push("manifest.entry must be SKILL.md when present");
    }

    if (manifest.compat !== undefined) {
      if (!Array.isArray(manifest.compat) || manifest.compat.length === 0) {
        errors.push("manifest.compat must be a non-empty array when present");
      } else if (manifest.compat.some((item) => typeof item !== "string" || item.trim() === "")) {
        errors.push("manifest.compat entries must be non-empty strings");
      }
    }
  } catch (error) {
    if (error.code !== "ENOENT") {
      errors.push(`invalid manifest.json: ${error.message}`);
    }
  }

  return errors;
}

const dirs = await listSkillDirs();

if (dirs.length === 0) {
  console.error("No skills found under skills/.");
  process.exit(1);
}

let failureCount = 0;

for (const dirName of dirs) {
  const errors = await validateSkill(dirName);
  if (errors.length > 0) {
    failureCount += 1;
    console.error(`x ${dirName}`);
    for (const error of errors) {
      console.error(`  - ${error}`);
    }
  } else {
    console.log(`ok ${dirName}`);
  }
}

if (failureCount > 0) {
  process.exit(1);
}
