# Solution-to-Frontend Workflow Refactor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor `solution-to-frontend` into a parent-owned, evidence-gated workflow with temporary `progress.md` state, explicit technical capability decisions, reviewable visual gates, and deterministic child-skill boundaries.

**Architecture:** Keep the skill cross-agent and Markdown-first. Make `SKILL.md` a thin coordinator over a static workflow protocol, stage playbooks, capability policies, and explicit adapters. Store execution state in a temporary workspace-local `progress.md`; formal facts and approvals remain in stage artifacts. Add a small Node ESM validator and scenario runner for structural and routing regressions, with Markdown-only fallback when scripts are unavailable.

**Tech Stack:** Markdown skill files, YAML frontmatter, Node.js ESM, Node built-in `assert/strict`, existing `npm run validate` repository validator. No runtime framework or new npm dependency.

## Global Constraints

- `solution-to-frontend` is the sole parent orchestrator and state owner.
- Every transition requires `Activity`, `Artifact`, and `Commitment` evidence.
- No approved technical capability architecture -> no visual ideation or V0 implementation.
- No reviewable visual artifact -> no visual approval.
- No approved representative V0 -> no scale implementation plan.
- `progress.md` is workspace-local temporary state, is not a formal artifact, and is deleted only after formal acceptance is complete.
- Superpowers supplies leaf engineering practices only; its meta-workflow and brainstorming state machine are not composed into pre-V0 stages.
- React back-office workflows with material list, search, filter, detail, edit, permission, batch-action, or approval behavior must evaluate Ant Design Pro Components.
- Existing framework or Tailwind presence does not prove a capable component system.
- Any `Build` decision must record concrete incompatibility with `Reuse` and `Adopt` candidates.
- Formal decisions and approvals must be promoted to stage-owned artifacts before `progress.md` cleanup.

---

## File Map

| File | Responsibility |
|---|---|
| `skills/solution-to-frontend/SKILL.md` | Thin parent coordinator, stage routing, child return contract, gates |
| `skills/solution-to-frontend/assets/progress-template.md` | Temporary progress document template |
| `skills/solution-to-frontend/references/workflow-protocol.md` | State machine, transition evidence, invalidation, cleanup |
| `skills/solution-to-frontend/references/stages/*.md` | Focused stage playbooks |
| `skills/solution-to-frontend/references/policies/*.md` | Golden paths and capability selection policy |
| `skills/solution-to-frontend/references/adapters/*.md` | Impeccable and Superpowers leaf-skill contracts |
| `skills/solution-to-frontend/scripts/validate-progress.mjs` | Progress schema and transition validator |
| `skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs` | Eight forward tests and child-advance regressions |
| `skills/solution-to-frontend/references/project-artifacts.md` | Formal artifact map and temporary-file lifecycle |
| `skills/solution-to-frontend/references/content-design.md` | Workflow capability requirements before technical decisions |
| `skills/solution-to-frontend/references/technical-baseline.md` | Concern inventory, evidence grades, candidate policies |
| `skills/solution-to-frontend/references/visual-v0.md` | Visual evidence and V0 approval gates |
| `skills/solution-to-frontend/references/scale-delivery.md` | Post-V0 planning, delivery, and acceptance |

---

### Task 1: Add Progress Schema and Validator

**Files:**
- Create: `skills/solution-to-frontend/assets/progress-template.md`
- Create: `skills/solution-to-frontend/scripts/validate-progress.mjs`
- Test: `skills/solution-to-frontend/tests/progress-validator.test.mjs`

**Interfaces:**
- `parseProgressDocument(content)` returns `{ frontmatter, sections }` or a descriptive validation error.
- `validateProgressDocument(content, context)` returns `{ valid: boolean, errors: string[] }`.
- `context` contains `formalArtifacts: Set<string>`, `approvedStages: Set<string>`, and `allowCleanup: boolean`.
- Valid stages are `BOOTSTRAP`, `INTAKE`, `CONTENT`, `CAPABILITY`, `VISUAL_DIRECTION`, `REPRESENTATIVE_V0`, `SCALE_DELIVERY`, `COMPLETE`.
- Valid statuses are `active`, `awaiting_approval`, `blocked`, `approved`, and `superseded`.

- [ ] **Step 1: Write failing validator tests**

Add Node `assert/strict` tests for:

```js
const validProgress = `---
schema: solution-to-frontend-progress/v1
status: active
current_stage: CONTENT
stage_status: active
next_gate: content-approval
updated_at: 2026-08-15
---

## Gate Status
## Active Stage
## Working Decisions
| ID | Decision | Status | Evidence | Promote to |
|---|---|---|---|---|
| D-1 | Use typed mock adapter | tentative | 02-content-design.md | technical-capability.md |
## Executor Runs
## Resume Here
`;
const validContext = {
  formalArtifacts: new Set(["02-content-design.md"]),
  approvedStages: new Set(),
  allowCleanup: false,
};
const progressWithInvalidStage = validProgress.replace("current_stage: CONTENT", "current_stage: nonsense");
const progressWithoutPromotionTarget = validProgress.replace("technical-capability.md", "");
const progressWithCompleteStatus = validProgress
  .replace("current_stage: CONTENT", "current_stage: COMPLETE")
  .replace("stage_status: active", "stage_status: approved");

assert.equal(validateProgressDocument(validProgress, validContext).valid, true);
assert.match(validateProgressDocument(progressWithInvalidStage, validContext).errors.join('\n'), /stage/);
assert.match(validateProgressDocument(progressWithoutPromotionTarget, validContext).errors.join('\n'), /promotion/);
assert.match(validateProgressDocument(progressWithCompleteStatus, { ...validContext, allowCleanup: false }).errors.join('\n'), /cleanup/);
```

- [ ] **Step 2: Run the tests and verify the expected failure**

Run: `node --test skills/solution-to-frontend/tests/progress-validator.test.mjs`

Expected: FAIL because the validator module and progress template do not yet exist.

- [ ] **Step 3: Write the minimal template and validator**

Use YAML frontmatter fields `schema`, `status`, `current_stage`, `stage_status`, `next_gate`, and `updated_at`. Require sections for `Gate Status`, `Active Stage`, `Working Decisions`, `Executor Runs`, and `Resume Here`. Reject unknown stages/statuses, tentative decisions without `Promote to`, and `COMPLETE` without `allowCleanup`.

- [ ] **Step 4: Run the tests and repository validator**

Run: `node --test skills/solution-to-frontend/tests/progress-validator.test.mjs`

Expected: PASS with malformed-stage, missing-promotion, and premature-cleanup cases covered.

Run: `npm run validate`

Expected: PASS for all skills.

- [ ] **Step 5: Commit**

```bash
git add skills/solution-to-frontend/assets/progress-template.md skills/solution-to-frontend/scripts/validate-progress.mjs skills/solution-to-frontend/tests/progress-validator.test.mjs
git commit -m "Add solution workflow progress validator"
```

### Task 2: Encode the Parent Workflow Protocol

**Files:**
- Create: `skills/solution-to-frontend/references/workflow-protocol.md`
- Modify: `skills/solution-to-frontend/references/project-artifacts.md`
- Create: `skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs`

**Interfaces:**
- Protocol consumers use the state names and transition predicates defined in Task 1.
- Formal artifact names remain `00-intake.md`, `01-outcome.md`, `02-content-design.md`, `technical-capability.md`, `03-visual-brief.md`, `04-v0.md`, `05-scale-plan.md`, and `06-acceptance.md`.

- [ ] **Step 1: Add protocol assertions to the regression test**

Add textual assertions that the protocol contains the complete state sequence, the `Activity`/`Artifact`/`Commitment` rule, all five invalidation relationships, and the cleanup condition requiring formal acceptance before deleting `progress.md`.

- [ ] **Step 2: Run the targeted test to verify it fails**

Run: `node --test skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs`

Expected: FAIL because `workflow-protocol.md` does not yet exist.

- [ ] **Step 3: Write the protocol and artifact lifecycle**

Document startup reconciliation, child return semantics, stage transitions, upstream invalidation, approval ownership, formal artifact promotion, interrupted-run recovery, and `progress.md` cleanup. Update `project-artifacts.md` to list `technical-capability.md`, distinguish formal files from the temporary progress file, and link the template.

- [ ] **Step 4: Run targeted tests and inspect the diff**

Run: `node --test skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs`

Expected: PASS for protocol assertions.

Run: `git diff --check`

Expected: no whitespace errors.

- [ ] **Step 5: Commit**

```bash
git add skills/solution-to-frontend/references/workflow-protocol.md skills/solution-to-frontend/references/project-artifacts.md skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs
git commit -m "Define parent-owned solution workflow protocol"
```

### Task 3: Extract Capability Policies and Golden Paths

**Files:**
- Create: `skills/solution-to-frontend/references/policies/golden-paths.md`
- Create: `skills/solution-to-frontend/references/policies/technical-decisions.md`
- Modify: `skills/solution-to-frontend/references/technical-baseline.md`

**Interfaces:**
- `technical-baseline.md` links to policies rather than duplicating their full decision matrix.
- The policy vocabulary is fixed: concern inventory, evidence grade, `Reuse`, `Adopt`, `Build`, candidate, incompatibility, boundary, approval.

- [ ] **Step 1: Add the eight capability-routing regression cases**

Add fixtures/assertions for: Next.js + Tailwind complex React admin, incumbent Ant Design admin, mature shadcn admin system, Vue admin, two simple settings forms, specialized canvas/editor, brainstorming premature plan recommendation, and interrupted `progress.md` recovery.

- [ ] **Step 2: Run the cases before policy implementation**

Run: `node --test skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs`

Expected: FAIL because the policy files and required routing text are absent.

- [ ] **Step 3: Write the policies**

`golden-paths.md` defines when an incumbent is established and capable, how supported paths are advertised, and what evidence a deviation requires. `technical-decisions.md` defines the concern inventory, evidence grades, comparison dimensions, Pro Components candidate trigger, platform exclusions, disproportionate-adoption exceptions, and required decision-table fields.

- [ ] **Step 4: Refactor `technical-baseline.md` into the policy entrypoint**

Make it load for any absent, weak, or unevidenced material concern, even when a framework or CSS utility exists. Keep the default stack concise and link the detailed policy documents.

- [ ] **Step 5: Run regression tests and validate links**

Run: `node --test skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs`

Expected: PASS for all eight capability-routing cases.

Run: `npm run validate`

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add skills/solution-to-frontend/references/policies skills/solution-to-frontend/references/technical-baseline.md skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs
git commit -m "Add capability selection policies and golden paths"
```

### Task 4: Split Stage Playbooks and Add Visual Evidence Gates

**Files:**
- Create: `skills/solution-to-frontend/references/stages/intake.md`
- Create: `skills/solution-to-frontend/references/stages/content.md`
- Create: `skills/solution-to-frontend/references/stages/capability.md`
- Create: `skills/solution-to-frontend/references/stages/visual.md`
- Create: `skills/solution-to-frontend/references/stages/v0.md`
- Create: `skills/solution-to-frontend/references/stages/scale-delivery.md`
- Modify: `skills/solution-to-frontend/references/content-design.md`
- Modify: `skills/solution-to-frontend/references/visual-v0.md`
- Modify: `skills/solution-to-frontend/references/scale-delivery.md`

**Interfaces:**
- Each playbook declares `Inputs`, `Activity`, `Formal artifact`, `Reviewable evidence`, `Approval`, `Failure return`, and `Next stage`.
- `visual.md` requires a rendered mockup, browser preview, or representative screenshot; a written design spec alone is invalid.
- `v0.md` requires runtime evidence and explicit representative-V0 approval before scale planning.

- [ ] **Step 1: Add missing-stage and visual-evidence assertions**

Assert that each playbook has all seven contract headings, `visual-v0.md` rejects text-only evidence, and `scale-delivery.md` requires approved V0 evidence.

- [ ] **Step 2: Run targeted tests and verify failure**

Run: `node --test skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs`

Expected: FAIL because the stage playbook directory does not exist and existing references lack the contract headings.

- [ ] **Step 3: Write the six focused playbooks**

Keep shared rules in `workflow-protocol.md`; each stage file only defines stage-local activity, evidence, approval request shape, failure classification, and artifact updates.

- [ ] **Step 4: Update existing stage references**

Add capability requirements to content design, technical decision approval and implementation-approach comparison to visual V0, and the post-V0 plan gate to scale delivery. Preserve existing domain detail by linking from the playbooks instead of duplicating it.

- [ ] **Step 5: Run tests and repository validation**

Run: `node --test skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs && npm run validate`

Expected: PASS with no broken local references.

- [ ] **Step 6: Commit**

```bash
git add skills/solution-to-frontend/references/stages skills/solution-to-frontend/references/content-design.md skills/solution-to-frontend/references/visual-v0.md skills/solution-to-frontend/references/scale-delivery.md
git commit -m "Add stage playbooks and visual evidence gates"
```

### Task 5: Define Specialist Adapters and Rebuild the Parent Skill

**Files:**
- Create: `skills/solution-to-frontend/references/adapters/impeccable.md`
- Create: `skills/solution-to-frontend/references/adapters/superpowers-engineering.md`
- Modify: `skills/solution-to-frontend/SKILL.md`

**Interfaces:**
- Every adapter declares `Trigger`, `Inputs`, `Allowed outputs`, `Formal artifact destination`, `Approval authority`, `Failure fallback`, and `Return-to-parent behavior`.
- Impeccable is used for product context initialization, visual direction, critique/audit, and polish within visual/V0 stages.
- Superpowers is used only for leaf engineering work: TDD, systematic debugging, verification, and `writing-plans` after V0 approval in `SCALE_DELIVERY`.

- [ ] **Step 1: Add parent/adapter regression assertions**

Assert that the parent skill contains the state sequence, `progress.md` lifecycle, child return rule, absence of `superpowers:brainstorming` as a required dependency, and post-V0-only `writing-plans` trigger.

- [ ] **Step 2: Run the test to verify it fails**

Run: `node --test skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs`

Expected: FAIL against the current monolithic coordinator.

- [ ] **Step 3: Write the two adapter contracts**

Describe exact invocation names, stage triggers, evidence destinations, fallback behavior, and prohibited stage transitions. Do not duplicate the external skills' entire workflows.

- [ ] **Step 4: Rewrite `SKILL.md` as the thin coordinator**

Keep overview, project isolation, startup/resume protocol, stage table, hard gates, approval protocol, adapter routing, and completion/cleanup. Move detailed concern policies and stage procedures to references. State that child recommendations never change parent state.

- [ ] **Step 5: Run targeted tests and inspect token/structure quality**

Run: `node --test skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs`

Expected: PASS for parent orchestration assertions.

Run: `npm run validate`

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add skills/solution-to-frontend/SKILL.md skills/solution-to-frontend/references/adapters
git commit -m "Refactor solution skill into parent coordinator"
```

### Task 6: Add Interruption, Invalidation, and Cleanup Regression Tests

**Files:**
- Modify: `skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs`
- Modify: `skills/solution-to-frontend/tests/progress-validator.test.mjs`

**Interfaces:**
- Scenario runner exports `runScenario(name)` and returns `{ passed, observations, failures }`.
- Scenarios inspect only the skill text, references, policies, and validator behavior; they do not call external agents or mutate project artifacts.

- [ ] **Step 1: Write failing interruption and invalidation tests**

Cover: a child returns a written UI spec and recommends planning; a content change invalidates downstream stages; a partial run resumes from `progress.md`; cleanup is rejected before acceptance and succeeds after acceptance.

- [ ] **Step 2: Run the scenarios and verify expected failures**

Run: `node --test skills/solution-to-frontend/tests/solution-to-frontend-regressions.mjs skills/solution-to-frontend/tests/progress-validator.test.mjs`

Expected: FAIL for missing protocol clauses or validator transitions before implementation.

- [ ] **Step 3: Add the smallest scenario fixtures and assertions**

Use explicit fixture strings for formal approval states and progress frontmatter. Assert that child completion leaves the parent stage unchanged, invalidation marks downstream artifacts superseded, and cleanup requires `allowCleanup`.

- [ ] **Step 4: Run the complete regression suite**

Run: `node --test skills/solution-to-frontend/tests/*.test.mjs skills/solution-to-frontend/tests/*.mjs`

Expected: PASS for all eight forward scenarios plus progress lifecycle cases.

- [ ] **Step 5: Commit**

```bash
git add skills/solution-to-frontend/tests
git commit -m "Cover workflow resume and gate regressions"
```

### Task 7: Repository-Level Verification and Handoff

**Files:**
- Test: all files under `skills/solution-to-frontend/` and `scripts/validate-skills.mjs`.

No README or manifest edit is planned; only add one if a preceding implementation task proves an existing discovery contract is invalid, and keep that change in the same task with a specific failing validation.

**Interfaces:**
- No new external dependency is introduced.
- Existing skill discovery metadata remains valid and `manifest.entry` remains `SKILL.md`.

- [ ] **Step 1: Run Markdown and skill structure checks**

Run: `npm run validate`

Expected: every skill prints `ok` and the process exits 0.

- [ ] **Step 2: Run all solution-to-frontend tests**

Run: `node --test skills/solution-to-frontend/tests/*.test.mjs skills/solution-to-frontend/tests/*.mjs`

Expected: all tests pass, including eight routing scenarios, progress validation, invalidation, resume, and cleanup.

- [ ] **Step 3: Run whitespace and reference checks**

Run: `git diff --check`

Expected: no output.

Run: `rg -n "TBD|TODO|PLACEHOLDER|writing-plans.*before|visual.*approval.*text" skills/solution-to-frontend docs/superpowers/plans/2026-08-15-solution-to-frontend-workflow-refactor.md`

Expected: no unresolved placeholder or contradictory routing language.

- [ ] **Step 4: Review the final diff against the confirmed spec**

Verify every acceptance criterion in `docs/superpowers/specs/2026-08-15-technical-capability-authority-design.md` maps to a changed file or passing test. Confirm `progress.md` itself is not present in this repository after tests.

- [ ] **Step 5: Commit the completed refactor**

```bash
git add skills/solution-to-frontend
git commit -m "Refactor solution frontend workflow architecture"
```

- [ ] **Step 6: Push only after the full verification pass**

```bash
git push origin main
```

Expected: remote `main` advances from the verified local commit and `git status --short` is empty.
