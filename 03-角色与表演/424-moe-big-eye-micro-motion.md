---
title: 萌系大眼微动专篇——眼越大，动作越小
category: 角色与表演
tags: [萌系, 大眼, 高光, 双层高光, 星形高光, 虎牙, 眯眼]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 萌系大眼把表情符号化：微动幅度与眼睛尺寸反相关；高光有无/形状=情绪开关（高光消失=黑化）；虎牙只跟微笑眯眼同框
related: [163, 162, 165, 422, 423, 425, 426, 254]
---

# 萌系大眼微动专篇——眼越大，动作越小

## 核心要点
- **幅度缩放第一定律：眼大→动作小**（经验）：萌系大眼的虹膜占画面像素是真人的 3-5 倍，同样的位移在大眼上被等比放大——虹膜位移按"眼宽的 1/8~1/6"封顶，再大=眼球乱飞的惊恐感
- **大圆眼的表情靠"符号"不靠"肌肉"**（公认）：萌系作画把眼部简化为三变量——高光(有无/形状)、瞳孔(大小/形状)、眼睑线(开/眯/垂)，写实系的眼轮匝肌表演不适用于这个画风
- **高光是萌系情绪的仪表盘**（公认）：有光=活，无光=死/黑化——"with no highlights in eyes"一词即可让 AI 生成绝望脸，是回报最高的单词提示词
- **双层高光=标准萌，星形高光=情绪峰值**（公认）：双点是日常可爱基准线，星形/十字=感动/憧憬的顶点符号（香菇纹/四点星为日漫公认画法）
- **虎牙仅微笑时露出**（库内规则·公认惯例）：虎牙是"开口笑的副产品"——闭嘴露出=违和，大哭/生气时露出=人设崩；联动动作是"眯眼+虎牙"的微笑套餐
- **眯眼是萌系的第一表情**（公认）：弯弯眼(にこにこ目)=开心到眼睛装不下的符号化表达，萌系眯眼的使用频率远高于写实系

## 详细内容

### 1. 幅度缩放原则（经验）

```
比例尺换算（以虹膜直径 D 为基准）：
  真人比例角色：虹膜位移上限 ≈ D × 1/4（163/165 标准）
  萌系大眼角色：虹膜位移上限 ≈ D × 1/8 ~ 1/6
  Q版/chibi：  虹膜位移上限 ≈ D × 1/10，且只允许水平向

眨眼同样缩放：
  真人：全闭眼 3-5 帧
  萌系：全闭眼 3-5 帧不变，但"半眨/颤睑"幅度减半
```
- 原因：大眼把每个微动的像素距离放大，观众对"眼球位置异常"的敏感度同步放大——小幅=灵动，同比例=失控（经验）
- **瞳孔缩放反而可以用大**：瞳孔直径变化 30-50% 在萌系是合法大动作（虹膜够大才看得见），这是大眼画风特有的红利（经验）

### 2. 高光画法与情绪对照（公认+AI 提示词实测）

| 高光状态 | 情绪语义 | 英文提示词 | 确定性 |
|---|---|---|---|
| 双层/双点高光 | 标准萌、日常可爱（基准线） | feature double highlights | 公认（作画惯例） |
| 明亮大高光 | 活泼、积极、元气 | bright highlights in eyes / feature large highlight | 公认 |
| 星形/四点星 | 感动、憧憬、发现宝物（峰值） | star-shaped highlights in the eyes | 公认（香菇纹惯例） |
| 心形 | 恋爱、心动 | heart-shaped highlights in the eyes | 公认 |
| 十字形 | 神秘、圣性 | cross-shaped highlights in the eyes | 公认 |
| 菱形 | 知性、高贵 | diamond-shaped highlights in the eyes | 公认 |
| 月牙形 | 夜、神秘系角色 | crescent-shaped highlights in the eyes | 公认 |
| 柔化模糊高光 | 温柔、治愈 | with softly blurred highlights | 公认 |
| **高光消失** | **黑化/绝望/虚无（一键变脸）** | with no highlights in eyes / lifeless eyes / dull eyes | 公认（163 黑化符号） |
| 金色/虹色高光 | 高贵、幻想系 | with golden highlights in the eyes | 经验 |

- 渐变黑化的写法（经验）：
```
  三段渐变：double highlights → softly blurred highlights → no highlights
  每段给一个镜头，共 1.5-3 秒——光是一点一点灭的，不是开关跳的
  提示词时序："the light in her eyes dims gradually, highlights fading frame by frame"
```
- 副作用警告（实测经验）：star-shaped 提示词会让**背景也长星星**；限定写法 "star-shaped highlights only inside the irises"，或改用 double highlights 保底（副作用最小）
- 提示词权重：高光类词权重 1.2-1.5 区间有效，超 2.0 全脸崩坏（AI 插画社区实测经验，视频模型同理降档用）

### 3. 虎牙×眯眼联动规则（库内规则·公认惯例）

```
铁律：虎牙仅微笑时露出
  ✅ 眯眼弯月 + 开口笑 + 单侧虎牙尖 = 萌系招牌（にぱー顔）
  ✅ 大笑张口 + 虎牙 = 活泼
  ❌ 闭口 + 虎牙 = 穿帮（牙从哪伸出来的？）
  ❌ 生气/大哭 + 虎牙 = 除非角色设定是"凶萌"，否则违和
```
- 生理逻辑（公认）：八重歯是视觉上的"咧嘴副产品"——嘴角大幅上扬才带得上唇露尖牙；八九寺真宵等角色的手办/官图全部遵守"虎牙配笑颜"（公认商品化惯例）
- 眯眼联动（经验）：虎牙微笑的官配眼型是**眯眼或半眯**——眼睛笑得眯起来，嘴才张得开，牙才露得出；三者是同一个肌肉联动的符号化
```
中文分镜句：
  她眼睛眯成两道弯月，嘴一咧，左边虎牙尖闪了一下。
英文提示词：
  eyes squeezed into happy crescent moons, big open smile, 
  a single fang peeking from the corner of her mouth — peak moe
```

### 4. 萌系眼部微动的合法清单（经验）

大眼画风"合法"与"违禁"动作：

| 动作 | 萌系判定 | 说明 |
|---|---|---|
| 虹膜小幅位移 | ✅ 合法 | ≤1/8 眼宽，灵动来源 |
| 瞳孔缩放(30-50%) | ✅ 合法且推荐 | 大眼红利，情绪直达 |
| 瞳孔地震 | ✅ 合法 | 萌系震惊标配(163) |
| 眨眼(全/半) | ✅ 合法 | 帧数同真人，频率可略高 |
| 高光有无/形状变化 | ✅ 合法 | 萌系专属通道 |
| 眯成弯月 | ✅ 合法 | 第一表情 |
| 眼轮匝肌细纹/眼袋 | ❌ 违禁 | 画风不兼容，出细纹=变老 |
| 写实的半闭眼+眼神涣散 | ⚠️ 慎用 | 改用"高光消失+瞳孔失焦"的符号方案 |
| 三白眼式瞪眼 | ⚠️ 慎用 | 萌系用"虹膜缩小+眼白增加"的简化版 |

### 5. 萌系眼神微动的提示词配方（经验）

```
日常灵动感（基准配方）：
  large round eyes with feature double highlights, 
  iris drifting subtly (no more than 1/8 of eye width), 
  natural blinking every 3-4 seconds, gentle eye movements

开心峰值：
  eyes sparkling with star-shaped highlights, pupils slightly enlarged, 
  lower lids lifting into a happy squint

失落/黑化渐变：
  highlights in her eyes fading, pupils losing focus, 
  iris drifting downward — the light going out of her eyes

震惊（萌系版）：
  pupils contracting then trembling (eye trembling), 
  iris shrinking, highlights quivering — classic anime shock
```
- 负面词库：realistic eyes, detailed eye muscles, wrinkles around eyes, small irises（萌系生成时压写实倾向）

## 备注
- 高光提示词表来自 AI 插画社区实测（manga.jpn.org 整理），视频模型权重需降档；虎牙规则为库内既有规则+官方商品化惯例
- 争议点：萌系眨眼频率——有派别认为大眼角色眨眼应更频繁（眼表面积大=易感干涩的拟真联想），本条目按"同真人 3-4 秒，情绪场景另调"处理
- 幅度缩放系数（1/8~1/6）为经验值，眼睛占脸比例越极端（chibi）系数越小
- 关联：163 眼神总纲（三变量/黑化符号）、162 微表情、165 AI 提示词、422 战斗眼神（杀气高光压制共用）、423 面瘫克制、425 帧级参数表、426 拆解方法论、254 待机微动（小动物角色的同类缩放逻辑）
