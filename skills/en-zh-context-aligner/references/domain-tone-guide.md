# Domain Tone & Freedom Guide (领域风格与动态路由指南)

## 1. 触发边界与智能路由 (Trigger Rules)

Receive the input, then immediately choose one channel. The gateway prevents over-processing before translation begins.

### 通道 A：闪电响应

**Trigger**: An independent English phrase, idiom, or slang expression with fewer than 10 words.

**Strategy**:

- Skip Step 1 and Step 2.
- Give the best scene-native Chinese idiom, colloquial equivalent, or industry expression directly.
- Add one vivid explanation using an everyday or technical scene.
- Keep the response lightweight. Do not wrap a small phrase in a heavy framework.

### 通道 B：重型重构

**Trigger**: A long sentence, paragraph, technical document, business essay, or source likely to become stiff under literal translation.

**Strategy**:

- Run the complete three-step workflow: `源码重构 -> 意象对齐 -> 终极通透版`.
- Keep the three sections separate. Do not merge, omit, or replace them with a bare translation.

### 通道 C：异常拦截

**Trigger**: A user correction, complaint, better proposed wording, or non-translation request.

**Strategy**:

- Do not mechanically trigger translation.
- Reply in conversational Chinese when no translation is requested.
- For translation feedback, start the lifecycle loop: derive a routing rule, hot-update the current translation, and propose a reference asset.

## 2. 自由度与术语写死矩阵 (Freedom Decision Matrix)

Use this matrix after an input enters 通道 B.

| 场景划分 | 术语处理（必须写死） | 口语化程度（自由度） | 终极版数量（自由度） |
| :--- | :--- | :--- | :--- |
| **技术架构/开发文档** | 保留或对齐行业标准黑话，如 `repo` -> `仓库/Repo`、`deploy` -> `部署/交付/发版`、`beta` -> `内测版`、`roadmap` -> `路线图` | 适度口语化，追求研发日常无障碍沟通感 | 1 个终极通透版 |
| **硅谷创投/商业随笔** | 解码文化潜台词，如 `ambitious` -> `有野心/敢破局/不甘平庸`，禁用误带贬义的表达；`go-to` -> `首选/必备/扛把子` | 高度口语化，追求行业大佬现场演讲感 | 1 个终极通透版 |
| **文学/生活通用句** | 粉碎英文骨架，转为纯正中文成语、大白话或画面化表达 | 极高，画面感和情绪传递优先 | 1 个终极通透版 |
| **歧义/多义极端句** | 优先保证技术核心不失真，不假装只有一种解读 | 适中 | 破例提供 2 个版本并说明取舍理由 |

## 3. Route Rules

- **Technical text**: Stabilize domain terminology first, then make it sound like engineers actually talk.
- **Startup or Silicon Valley text**: Decode the cultural subtext before translating individual words.
- **Literary or everyday text**: Preserve mood, image, and human rhythm before surface symmetry.
- **Ambiguous text**: Put the most likely reading first. Add a second only when it materially changes tone or meaning.
- **Information overload**: Preserve argument-changing details. Merge low-priority lists or category-level specifics when they only increase memory burden.
