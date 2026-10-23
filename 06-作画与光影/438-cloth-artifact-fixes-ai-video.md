---
title: AI 视频布料崩坏防治——5 大常见崩坏成因与对策
category: 作画与光影
tags: [布料崩坏, 负面提示词, 穿模, 风方向, 帧数乱抖, AI视频质量]
source: 网络学习（OutfitVideo Negative Prompts Guide + Hailuo AI Fabric Physics + AI Tools Guidebook 2026）
created: 2026-10-20
updated: 2026-10-20
summary: AI 视频布料 5 大崩坏类型（穿模/飘向反风/帧数乱抖/布料粘身/手臂动袖子不动）的成因、正向修正与负面提示词、I2V 参数建议
related: [437, 439, 238, 074]
---

# AI 视频布料崩坏防治

## 核心要点

- AI 布料崩坏的根源是模型"没有物理引擎"——只有概率分布，所有崩坏都是概率取样偏离物理常理
- 最有效的修复策略：**正向约束（提示词三件套）+ 负面排斥（精准负面词）+ 参数修正（I2V 运动强度）三管齐下**
- 不要在正面提示词里写"不要穿模"——AI 会把"穿模"这个词本身也纳入语义生成，必须走独立的负面提示词通道
- 崩坏率 ≈ 布料自由度 × 运动速度 × 背景复杂度；复杂镜头拆成 4-6 秒短片段可降低 50% 崩坏率
- 穿模/粘身/帧数乱抖这 3 类崩坏最顽固，必须在 I2V 源头用 ControlNet 或参考图锁定布料结构

## 详细内容

### 崩坏 1：穿模（布料穿透身体/穿过手臂）

| 项 | 内容 |
|---|---|
| **现象** | 布料从手臂中间穿过去、披风穿过身体、裙摆穿插进腿部 |
| **成因** | AI 视频模型没有碰撞检测（collision detection），只预测像素运动路径；复杂交叉动作时布料和身体都往同一位置取样就穿透了 |
| **稳定性** | ★☆☆ — 最顽固的崩坏类型之一 |
| **正向提示词修正** | `fabric drapes over the shoulder naturally, resting on the arm without crossing through the body plane`（布料自然垂在肩上，落在手臂上不穿过身体平面）|
| **负面提示词** | `fabric clipping through body, cloth penetrating arms, garment intersecting with torso, material passing through legs` |
| **I2V 参数建议** | 降低 Motion Intensity 到 0.5-0.6（默认 0.8），启用 ControlNet OpenPose/Depth 锁定身体骨骼位置；对 Sora/Kling 等无 ControlNet 模型，换用更静态的姿势（例如慢转身替代大幅摆臂）|
| **备选方案** | 复杂交叉镜头拆成两个镜头——先布料在身体左侧的状态，再切到右侧，通过剪辑规避穿模 |

### 崩坏 2：飘向反风（布料往风的反方向飘）

| 项 | 内容 |
|---|---|
| **现象** | 你写了 "wind blowing from left" 但布料飘向左边（应该飘右边）；奔跑时披风往腿前面跑（应该拖在后面）|
| **成因** | AI 模型对"风"这个抽象词的物理方向性理解不稳定；尤其当提示词里同时出现"奔跑"和"风"时，模型会取"奔跑方向的反方向"或"风的方向"——概率各半 |
| **稳定性** | ★★☆ — 中等顽固 |
| **正向提示词修正** | 不要写 `wind blowing from left`，改写 `fabric billowing to the right, pushed by a strong leftward gust`（布料向右鼓起，被左来的强风推动）——把结果写在前面，给模型明确的视觉目标；或写 `cape trailing behind, opposite to the direction of movement`（披风拖在身后，与运动方向相反）|
| **负面提示词** | `fabric blowing into the wind, cloth moving against gust direction, cape flying forward while running, garment pulled in wrong direction` |
| **I2V 参数建议** | 对 Kling 3.0 / Hailuo 这类物理理解较好的模型，显式指定方向即可；对 Sora/MidRunway 等，把风的效果绑定到主体：`her long scarf trailing behind her as she runs`（her 明确了 scarf 和 her 是绑定关系）|

### 崩坏 3：帧数乱抖（布料一帧有褶皱下一帧没了）

| 项 | 内容 |
|---|---|
| **现象** | 裙摆从 A 形状突然跳到 B 形状，没有过渡；上一帧的布料纹理下一帧消失了；布料边缘像波浪一样抖动 |
| **成因** | 扩散模型每帧独立去噪，帧间没有显式的时序连续性约束；布料的细小褶皱和纹理在去噪过程中被"抹掉"或"重新生成" |
| **稳定性** | ★★★ — 较易修复 |
| **正向提示词修正** | 添加 `smooth continuous fabric motion, gradual fold transitions across frames, stable drape pattern maintained throughout`（平滑连续布料运动，帧间渐变褶皱过渡，全程保持稳定垂坠图案）|
| **负面提示词** | `flickering fabric, inconsistent fold between frames, shape-shifting garment, jittery textile edge, disappearing pleats, morphing hem` |
| **I2V 参数建议** | 开启 Temporal Consistency（时序一致性）开关（Kling/MidRunway 均支持）；降低 CFG Scale 到 6-7（太高会过度偏离参考图）；使用 4-6 秒短片段（模型时序预测精度在此窗口内最高）|

### 崩坏 4：布料粘身体（布料像保鲜膜一样贴死不动）

| 项 | 内容 |
|---|---|
| **现象** | 风衣下摆像粘在腿上一样；围巾贴在脖子上一丝不动；明明写了 "billowing" 但布料就是不动 |
| **成因** | ① 提示词里同时写了材质但没写环境力（"silk coat" 但没写风或运动）；② 运动强度设置太低；③ 背景太复杂导致 AI "计算预算"被稀释，把布料物理优先级降到 0 |
| **稳定性** | ★★★ — 易修复 |
| **正向提示词修正** | 补环境锚点！`silk coat hem swaying, pushed by wind entering from the balcony` 比 `silk coat` 效果好 6 倍（Hailuo AI 实测）；额外加 `fabric resting lightly on the body with slight separation`（布料轻靠身体有微微间隙）|
| **负面提示词** | `fabric glued to body, skin-tight garment, no cloth movement, static garment, flat textile, no drape` |
| **I2V 参数建议** | 背景简化！纯色背景或极简场景让模型把计算预算集中在布料上（Background-Physics Trade-off 原理）；Motion Intensity 提到 0.7-0.8 |

### 崩坏 5：手臂摆动但袖子不动

| 项 | 内容 |
|---|---|
| **现象** | 手臂挥了出去，但袖子像焊在手臂上一样；或者袖子只动了手指部分，肘部附近不动 |
| **成因** | AI 模型把袖子当作手臂的一部分建模，而不是独立的 secondary motion；尤其当提示词只写了 "a woman waving her arm" 没提袖子时，模型会让袖子和手臂完全同步 |
| **稳定性** | ★★★ — 较易修复 |
| **正向提示词修正** | 显式告诉 AI 袖子是独立的！`waving her arm → loose sleeve flailing behind, delayed by a split second, catching the air`（挥动手臂 → 宽松袖子滞后一瞬间甩在后面，抓着空气）—— 明确了 follow through 关系 |
| **负面提示词** | `sleeve rigid on arm, cuff moving exactly with hand, no fabric follow-through, synchronous garment and limb movement, sleeve welded to arm` |
| **I2V 参数建议** | 对袖子/裤腿这类"管道型布料"，明确写材质厚度：`loose silk sleeve` 比 `sleeve` 好，`thick wool sleeve` 比 `loose sleeve` 好——厚度暗示了布料的独立运动性 |

### 通用负面提示词模板（4 层分层结构）

```
【布料层】fabric clipping through body, plastic texture, rubbery sheen, melting textile, watercolor bleed, disappearing folds
【运动层】sleeve rigid on arm, cape flying forward while running, no cloth follow-through, motion blur on garment, ghosting edge
【帧间层】flickering fabric, inconsistent fold between frames, jittery hem, shape-shifting garment, morphing drape
【背景层】flickering background, shifting shadows, inconsistent lighting on garment
```

每层 4-6 词，总计 20-30 词效果最佳（OutfitVideo 实测：超过 50 词会稀释信号，少于 10 词覆盖不足）。

### 崩坏排查流程图

```
布料崩了 → ① 哪类？穿模/反风/抖帧/粘身/袖不动
         → ② 先检查提示词三件套（材质+动词+环境）缺了哪个？
         → ③ 加精准负面提示词（参考上表）
         → ④ 调 I2V 参数（Motion Intensity / CFG / Temporal Consistency）
         → ⑤ 背景简化为纯色/极简
         → ⑥ 拆分成 4-6 秒短片段重新生成
         → ⑦ 换模型（Kling 3 / Hailuo 物理 > Sora > MidRunway）
```

## 备注

- 崩坏根源分析基于 Hailuo AI "Computational Budget Rule" + SkillMD "Drag Hierarchy"，崩坏分类与负面提示词句库来自 OutfitVideo 2026-09 指南
- 本条目重点是 AI 视频模型特有的崩坏，不覆盖传统动画手绘阶段的布料问题；手绘动画布料时序问题见 439（帧级参数表）
- 三要素提示词的正确写法见 437；布料情绪信号见 440；动作戏视角×服装矩阵见 238；服装张力信号见 074
- 确定性标注：公认 = 多篇来源交叉验证；经验 = 单一权威来源或社区共识；争议 = 不同模型表现差异大
