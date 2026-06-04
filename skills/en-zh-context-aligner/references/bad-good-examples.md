# Paired Examples: 好味道 vs 坏味道

Use these examples to calibrate taste. Bad examples are not just less elegant; they reveal failure modes the skill should actively avoid.

## Case 1: 极端量词的否定转化

- Bad: `打造并交付一个带有 0 行手动编写代码的软件内部测试版。`
- Good: `全程没手写过一行原生代码，直接硬核交付了一款内测版软件。`
- Why bad: 中文里 `带有 0 行手动编写代码` 极度反人类，不符合正常人说话习惯。必须转化为带情绪的否定句，如 `没手写过一行`。

## Case 2: 文化色彩词的意象重构

- Bad: `我们正在寻找野心勃勃的工程团队来和我们一起建立这个。`
- Good: `我们正在寻找有野心、敢破局的工程团队与我们共建。`
- Why bad: 中文里 `野心勃勃` 常带贬义，且 `建立这个` 语意模糊。在创业招募场景中，`ambitious` 代表不甘平庸的极客精神，`build this` 代表共建产品或事业。

## Case 3: 经典翻译腔句式的结构重排

- Bad: `这使得 Node.js 成为一个具有非常高性能的工具，它是 Google Chrome 的核心。`
- Good: `正因继承了 Google Chrome 底层核心 V8 的强悍基因，Node.js 拥有极佳的性能表现。`
- Why bad: `成为一个具有...的...` 是典型翻译腔。中文习惯先交代因果和背景，再落到主体表现。技术上也要校准：Node.js 不是 Chrome 的核心；它运行在 Chrome 的 V8 引擎之上。

## Mechanical Bad Smells

- `带有 0 行`
- `具有...性能`
- `...的其中之一`
- `对于...而言`
- `建立这个`
- `野心勃勃的团队`
