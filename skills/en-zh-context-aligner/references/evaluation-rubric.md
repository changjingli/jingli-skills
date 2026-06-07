# Evaluation Rubric

Use this rubric for self-review or agent review after drafting.

## 1. 路由正确度 (20%)

- Independent phrases under 10 English words use 通道 A and do not receive the heavy three-step template.
- Long, technical, business, or translationese-prone text uses 通道 B.
- User corrections or non-translation requests use 通道 C instead of mechanically restarting translation.

## 2. 结构完整度 (20%)

- Every 通道 B answer includes separate `一、源码重构`, `二、意象对齐`, and `三、终极通透版` sections.
- Source reconstruction peels off nested modifiers with parentheses where useful.
- Image alignment includes a comparison table with `字面平淡意（坏味道）` and `中文神会平替（好味道）`.

## 3. 技术事实度 (25%)

- Identifies and corrects technical or logical ambiguity in the English source.
- Preserves core terms and does not invent facts.
- Handles vague pronouns or causal links such as `this allows`, `which makes`, or `it is based on` with domain-aware clarity.

## 4. 松弛度与气场 (25%)

- Read the final translation aloud. It should sound like a living Chinese architect, founder, writer, or practitioner in the target scene.
- No obvious translationese, including `具有...性能`, `是...的其中之一`, `被认为...`, `被期望...`, or literal zero-quantity phrasing.
- The strongest hook appears early when Chinese would naturally lead with it.
- Tone matches the source without becoming artificially dramatic.

## 5. 认知熵与循环层 (10%)

- Dense secondary detail is merged only when it lowers memory burden without changing the argument.
- When the user improves a translation, the response derives a reusable routing rule, applies it immediately, and provides a concrete reference asset in a code block.

## Pass Bar

- Pass: correct gateway, accurate meaning, native Chinese rhythm, no major bad smells.
- Revise: accurate but stiff, overly literal preposition mapping, missing cultural subtext.
- Fail: wrong gateway, missing mandatory 通道 B steps, mistranslated technical facts, foreign-sounding Chinese, or a final version that requires rereading.
