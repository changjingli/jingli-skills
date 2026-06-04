# Terminology Guide

Use this guide to keep terminology consistent within the same passage or article. Defaults are not rigid global law: choose the term that fits the scene, then keep it stable unless context genuinely changes.

## Consistency Rules

- Build a temporary terminology map for each article or long passage.
- The first clear rendering of a key term becomes the article-local default.
- Do not alternate between multiple Chinese renderings for the same English term just for variety.
- If a term has two legitimate senses, distinguish them explicitly in the map, such as `deploy (infra)` -> `部署` and `ship/release` -> `发版/发布`.
- Prefer keeping widely used industry abbreviations when Chinese translation sounds forced, such as `PR`, `CI`, `API`, `SDK`, and `CLI`.
- Surface the terminology map only for long texts, technical texts, or when the user asks about consistency. For short sentence translation, apply it silently.

## Default Technical/Product Terms

| English | Default Chinese | Notes |
| --- | --- | --- |
| agent | agent / 智能体 | In AI engineering context, prefer `agent` when it is already community jargon; use `智能体` when explaining to broader readers. Do not use `代理` unless it means proxy. |
| Codex agent | Codex agent | Keep product + role stable. |
| repository / repo | 仓库 | Avoid mixing with `代码库` in the same article unless explaining the concept. |
| codebase | 代码库 | Use for the body of code, not the Git hosting container. |
| commit | commit / 提交 | Keep `commit` in Git-heavy contexts; use `提交` for broader readers. |
| pull request / PR | PR | Avoid `拉取请求` unless explaining GitHub terminology to beginners. |
| CI | CI | Do not force `持续集成` unless the source is educational. |
| CI configuration | CI 配置 | Keep concise. |
| deploy | 部署 | Use for infrastructure/service deployment. |
| ship / shipping | 交付 / 发布 / 发版 | Product context decides: `ship a product` -> `交付/发布产品`; engineering release rhythm -> `发版`. |
| release | 发布 / 发版 | Product announcement -> `发布`; engineering cadence -> `发版`. |
| internal beta | 内测版 | Avoid alternating with `内部 beta` after choosing one. |
| alpha tester | alpha 测试者 | Keep `alpha` when product-stage nuance matters. |
| observability | 可观测性 | Standard technical term. |
| infrastructure | 基础设施 | Standard technical term. |
| tooling | 工具链 / 工具 | `工具链` for a system of tools; `工具` for individual utilities. |
| scaffold | 脚手架 | Standard dev term. |
| package manager | 包管理器 | Standard dev term. |
| application framework | 应用框架 | Standard dev term. |
| daily active users | 日活用户 | Product metric context. |
| power users | 重度用户 / 高阶用户 | Choose by tone; keep stable. |
| feedback loop | 反馈回路 | Standard product/engineering term. |
| workflow | 工作流 | Standard term. |
| prompt | prompt / 提示词 | Keep `prompt` for AI-native audience; use `提示词` for broader audience. |
| subagent | subagent / 子 agent | Keep stable with the article's jargon level. |

## Ambiguity Notes

- `build`: In product/startup context, usually `打造/共建/构建`; in engineering implementation context, `构建`; in recruiting slogans, often `共建`.
- `ambitious`: In startup context, prefer `有野心/敢破局/不甘平庸`; avoid pejorative `野心勃勃` unless the source is critical.
- `manual / manually-written`: In AI-coding context, often better as `人手写的/人工手写的/亲手写的`; avoid stiff `手动编写`.
