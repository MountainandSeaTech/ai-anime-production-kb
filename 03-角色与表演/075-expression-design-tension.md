---
title: 表情设计张力（面部结构）
category: 角色与表演
tags: [张力, 表情, 面部结构, 设计, 表情库, 防同质化, 人脸描写, 角色锚定]
source: 拆解+联网学习
created: 2026-10-13
updated: 2026-10-23
summary: 表情设计靠面部结构夸张+表情库分层；防同质化靠"可画的几何结构"而非形容词，Bones·Marks·Anchor三锚法+特征维度速查表
related: [024, 030, 070, 072, 233, 424]
---

# 表情设计张力（面部结构）

## 核心要点
- 表情张力靠**面部结构夸张+表情库分层**——关键时刻用极端表情，日常用克制
- 反差定律：日常越克制，关键瞬间极端表情=反差=张力峰
- 表情是 024 微表情的"设计版"——本条讲怎么设计面部让表情更有力
- 表情库分层：日常克制 / 蓄势微变 / 峰值极端 / 失智空

## 表情库分层

### 1. 日常克制（面瘫基底）
- 日常/对峙用面瘫/克制=基底
- 越克制，反差越大（用户偏好的冷血风）
- 面瘫基底让"一瞬变化"更狠

### 2. 蓄势微变（024）
- 蓄势期用微表情——瞳孔缩/嘴角紧/眼睑颤
- 微变从面瘫基底"微微露出"=将动信号
- 见 024 微表情信号源

### 3. 峰值极端
- 关键瞬间用极端表情——瞪眼/咬牙/扭曲/狂笑
- 从面瘫→极端=最大反差=峰值
- 极端表情配冲击帧（059）

### 4. 失智空（055）
- 变身/暴走后用失智空表情——眼无神/嘴角歪
- 是"是人还是兽"的视觉悬念

## 面部结构的夸张设计

### 眼部放大
- 动漫把眼睛画大=表情可读性强
- 眼部是表情主战场（024）
- 大眼+瞳孔变化=微表情可见

### 嘴部简化/夸张
- 嘴可简化（一线）也可夸张（张到极致）
- 一线=克制，张大=爆发
- 嘴的简/张反差=情绪反差

### 面部形变（060）
- 关键瞬间面部形变——脸压扁/扭曲/拉长
- 形变=情绪极值的视觉化

## 防同质化：人脸结构描写维度表

### 核心原则：写"可画的几何结构"，不写形容词
- **同脸症的根源**：提示词全用 `beautiful/gorgeous/handsome/pretty` 这类无执行信息的形容词，模型只能套默认脸
- **解法**：让脸变得具体，只能靠**可被画出来的几何结构**——脸型、颌线、眉骨、颧骨、鼻梁、眼距、唇形
- 记忆口诀：**Bones（骨骼）· Marks（痕迹）· Anchor（锚点）**三锚法
- 若角色走**可爱/萌系**路线，把本节所有维度向"幼态圆润"统一偏置，见 424「可爱女生描写手法」

### Bones · Marks · Anchor 三锚法
| 锚层 | 内容 | 作用 |
|---|---|---|
| Bones 骨骼 | 脸型/颌线/眉骨/颧骨/鼻梁/眼距/唇形 | 决定面部骨架轮廓，同脸症主要靠这层破 |
| Marks 痕迹 | 肤色/肤质/年龄痕迹（皱纹/法令纹/雀斑/疤/痣/毛孔/胡茬） | 决定皮肤质感与真实年龄感 |
| Anchor 锚点 | 一个不可替代的识别物（左眼下痣、断眉、歪鼻梁、缺颗牙、耳洞） | 潜意识锁角色，见 233 |

### 特征维度速查（每项挑 1 个词写进提示词）
**脸型 Face shape**：oval / round / square / heart / diamond / rectangular-oblong / triangular / long / wide / narrow / broad
**颌线 Jawline**：sharp / soft / angular / square / rounded / pointed / wide / narrow / defined / weak
**下巴 Chin**：pointed / square / round / long / short / jutting-protruding / receding-weak / cleft / double
**颧骨 Cheekbones**：high / low / angular / chiseled / sharp / strong / prominent / sculpted / broad / wide / fine / delicate / hollow cheeks
**鼻子 Nose**：straight / aquiline-hooked / button-small / upturned-snub / flat / wide / bulbous / beak-shaped / crooked / long / narrow bridge
**眼睛 Eyes**：almond / round / hooded / monolid / deep-set / close-set / wide-set / upturned / downturned / large / small / narrow
**眉毛 Brows**：thick / thin / straight / arched / angled / bushy / sparse / high / low / furrowed
**嘴唇 Lips**：full / thin / wide / narrow / heart-shaped / bow-shaped / downturned / upturned / asymmetrical
**年龄/肤质 Age & skin**：freckles / acne scars / wrinkles / crow's feet / nasolabial folds / age spots / pores / stubble / five-o'clock shadow
**锚点 Anchor**：scar / mole / birthmark / tattoo / missing tooth / crooked tooth / piercing / burn mark

### Seedance / WAN3 必写公式
- **Facial Details 至少写 3–4 项**（眼形 + 眉骨 + 鼻梁 + 唇形 + 颌线），这几项一起决定辨识度
- 完整公式：`[Subject] + [Facial details 3-4项] + [Age/Ethnicity] + [Hair] + [Expression] + [Art style] + [Lighting] + [Camera angle]`
- 年龄/族裔线索必须写：East Asian / Caucasian / African / South Asian；28yo / 55yo；模型靠这些锁定默认脸分布

### 反例 vs 正例
```
Bad（全形容词，必同脸）：
"a beautiful young woman, gorgeous face"

Good（全可画结构，唯一脸）：
"a 28yo East Asian woman, elongated oval face, sharp defined jawline, high angular cheekbones,
 straight narrow nose bridge, narrow deep-set monolid eyes, thin lips with closed-mouth smile,
 thick straight eyebrows, a mole under the left eye"
```

### 防同质化自检清单
- [ ] 脸型不与其他角色重复？
- [ ] 至少 3 项面部几何结构被点名（眼/眉/鼻/唇/颌/颧）？
- [ ] 有一个不可替代的锚点？
- [ ] 没用 pretty/beautiful 当唯一描述？
- [ ] 写了年龄+族裔线索？
- [ ] 锚点已写入资产表"专属识别物"字段？

## 表情反差定律
- 日常面瘫 → 关键极端=最大反差=最强峰
- 日常夸张 → 关键也夸张=无反差=平
- 所以高级角色=面瘫基底+一瞬极端

## 表情设计的用法

### 1. 面瘫→极端峰值
```
面瘫日常（1s）→ 蓄势微变瞳孔缩（0.5s）→ 峰值极端瞪眼扭曲+冲击帧（0.3s）→ 回面瘫（0.5s）→ 定格（1s）
```

### 2. 失智空（变身）
```
变身前面瘫（0.5s）→ 变身后失智空眼无神特写（0.8s）→ 暴起（0.3s）→ 定格（1s）
```

### 3. 反派冷笑一瞬
```
反派面瘫（1s）→ 一瞬冷笑特写（0.3s，将出手）→ 出手必杀（0.3s）→ 回面瘫（0.5s）→ 定格（1s）
```

## 表情设计的常见坑
- **日常太夸张**：基底就夸张=无反差=峰值弱
- **峰值不极端**：关键也克制=无峰=平
- **表情无递进**：从面瘫直接跳极端=无微变=突兀
- **失智不空**：变身后表情正常=无失控悬念

## 表情与其他工具配合
- 表情+微表情（024）=面部信号系统
- 表情+冲击帧（059）=极端表情凝固
- 表情+形变（060）=面部形变极值
- 表情+配角反应（072）=主角极端+配角惊愕=双放大

## 经典表情张力场景

### 面瘫→极端峰
```
面瘫（1s）→ 微变（0.5s）→ 极端+冲击帧（0.3s）→ 回面瘫（0.5s）→ 定格（1s）
```

### 失智空变身
```
面瘫（0.5s）→ 失智空特写（0.8s）→ 暴起（0.3s）→ 定格（1s）
```

### 冷笑一瞬
```
面瘫（1s）→ 冷笑特写（0.3s）→ 必杀（0.3s）→ 回面瘫（0.5s）→ 定格（1s）
```

## AI 提示词
- 面瘫基底：`deadpan expression, neutral face, restrained, minimal emotion`
- 微变：`subtle micro-expression, pupils contracting, lips pressing, slight tension`
- 极端峰值：`extreme expression, wide eyes, clenched teeth, distorted face, intense`
- 失智空：`blank feral eyes, empty stare, lost sanity, unsettling transformation face`

## 备注
- 表情设计是 024 微表情的设计版——分层+反差
- 核心：面瘫基底+微变蓄势+极端峰值+失智空
- 反差定律：日常越克制，峰值越狠
- 用户偏好的冷血风=面瘫基底+一瞬极端=最寒
- AI 视频表情靠 prompt+大特写，极端表情比微表情稳
