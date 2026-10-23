---
title: AI微表情提示词工程——从面瘫到演技派
category: 角色与表演
tags: [AI提示词, 微表情提示词, 表情控制, 面部稳定性, 抽卡策略]
source: 网络学习
created: 2026-10-13
updated: 2026-10-13
summary: AI默认把"悲伤"画成嚎啕大哭；微表情提示词的核心是压低幅度、精确到肌肉、给足时间
related: [161, 162, 163, 164, 117]
---

# AI微表情提示词工程

## 核心要点
- AI的训练偏向**高辨识度表情**——写"sad"出痛哭，写"happy"出大笑；微表情是逆势操作
- 微表情提示词三原则：**幅度词压级、肌肉级描述、时长词约束**
- 主情绪+次微表情的双层公式是当前最稳的配方（Hailuo验证）
- 表情戏镜头越短越稳——2-4秒是微表情生成的安全区
- 关联 161 AU词汇、162 微表情、117 动作词汇库

## 核心公式

### 双层公式（主推）
```
[主情绪基底] + [次微表情触发]
"Contemplative" + "subtle squint"
"Relieved" + "lip corner twitch"

完整示例：
"a contemplative swordsman, subtle squint in his eyes,
 faint tension at the corner of his mouth, 
 rain light on his face, close-up"
```

### 五要素公式（精控版）
```
[状态] + [部位] + [幅度] + [时长] + [过渡]

示例：
"both eyes widen slightly (18% sclera exposure), 
 holds 0.35 seconds, then slowly returns to calm"
```
- 五要素给AI一张"时间表"——比单写状态稳定一个量级

## 幅度词分级表（压幅度是第一要务）

| 级别 | 词汇 | 效果 |
|---|---|---|
| 极微 | barely perceptible, faint, slight hint of | 微表情级 |
| 轻 | subtle, gentle, soft, mild | 克制的表演 |
| 中 | noticeable, clear, distinct | 常规表情 |
| 强 | intense, dramatic, pronounced | 爆点表情 |
| 爆 | explosive, exaggerated, extreme | 动漫颜艺 |

- **默认陷阱**：不写幅度词=AI按"中-强"处理
- 微表情场景永远从"极微/轻"起步

## 部位级动词库（161的AU翻译版）

### 眉区
```
brow lift / inner brow raise(八字眉) / brow furrow(皱眉) /
softening of the forehead(眉头舒展)
```

### 眼区
```
squint(眯眼) / eye-narrowing / eyes widen slightly /
steady gaze / gaze drops(视线下垂) / slow blink /
light reflection in eyes(高光)
```

### 嘴区
```
lip corner twitch(嘴角抽动) / corner-of-mouth lift /
lips pressed(抿嘴) / relaxed lips / 
slight parting of lips(嘴唇微张)
```

### 鼻/颌区
```
nostril flare(鼻翼扩张-愤怒) / nose wrinkle(皱鼻-厌恶) /
jaw tightens(下颌紧绷) / subtle swallow(吞咽-紧张)
```

## 面瘫修复清单（Stiff Face Checklist）
AI生成的脸像蜡像？逐项排查：
```
□ 眉区有没有动态？——加"subtle brow movement"
□ 有没有眨眼？——加"natural blinking, slow blink"
□ 视线有没有落点？——加"gaze fixed on frame left"
□ 嘴唇是不是焊死的？——加"relaxed lips, slight parting"
□ 有没有呼吸感？——加"chest rises subtly with breath"(167)
□ 皮肤是不是塑料？——加"natural skin texture, subtle facial muscle movement"
```

## 表情变化的时序描述
```
单镜头内的表情弧：
"starts with a neutral expression, 
 eyes narrow slowly as realization dawns, 
 ends with a faint bitter smile"

三段式：起点状态 → 变化过程(how) → 终点状态
```
- 关键连接词：as(随着) / gradually / slowly / then
- 变化过程给动词不给名词——AI对"变化动词"的响应好于"情绪名词"（146动词优先铁律）

## 镜头与表情的匹配
| 景别 | 表情策略 |
|---|---|
| 远景/全景 | 别写表情，写肢体语言(166) |
| 中景 | 写头部姿态+粗表情 |
| 近景 | 主情绪+1个微表情 |
| 特写 | 五要素公式全开，眼部细节(163) |
| 大特写(眼/嘴局部) | 单部位精写 |

## 抽卡与验收
```
微表情镜头：3-5次抽卡起步
验收三问：
  1. 表情变化在正确的时间点吗？（听到台词后，不是同时）
  2. 幅度够小吗？（能一眼看出=太大）
  3. 面部其他部位有没有崩？（微表情戏常伴随面部漂移）
```
- 失败品处理：放弃或缩短使用——微表情崩了没有修复价值，重抽

## 常见坑
- **情绪名词直给**："he is sad"=嚎啕大哭风险，改"tears well up but don't fall"(具体生理)
- **多情绪并列**："angry, sad, confused"=面部调色盘，用双层公式别用堆叠
- **特写里写动作**：大特写+手部动作=手糊在脸上，特写只写脸
- **时长贪多**：8秒表情戏=后4秒必崩，拆成两镜或接受漂移
- **忽视中性基线**：参考图用夸张表情=全程表情过火；角色设定图用严格中性表情(闭口/柔焦/平光)

## 进阶
- **表情差分生成**：同一提示词只改次微表情词→得到"同一场戏的多个表演版本"→选最对的
- **微表情接力**：特写镜头的首尾帧用不同微表情参考图=引导AI做表情过渡（144首尾帧联动）
- **负向提示词**："exaggerated expression, cartoonish, overacting, distorted face"进负向库(112)
- **声音先行**：表情变化镜头配呼吸声/轻气音(156)=观众对表情的感知被声音放大

## 备注
- 三原则：幅度压级/肌肉级描述/时长约束
- 双层公式保底，五要素精控
- 2-4秒安全区，3-5次抽卡，特写才写细节
- 关联：161 AU词汇、162 微表情、163 眼部、164 复合配方、117 动作词汇、146 通用铁律
