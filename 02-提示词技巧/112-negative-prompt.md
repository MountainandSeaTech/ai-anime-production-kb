---
title: 负向提示词（negative prompt / --no）
category: 提示词技巧
tags: [提示词, 负向, 排除, 崩坏, 一致性]
source: 网络学习
created: 2026-10-13
updated: 2026-10-13
summary: 告诉AI别生成什么=主动排除崩坏；SD 用 negative 字段，MJ 用 --no
related: [087, 111, 113, 114, 088]
---

# 负向提示词（negative prompt / --no）

## 核心要点
- 正向告诉AI"要什么"，负向告诉AI"**不要什么**"
- SD 系：独立 negative prompt 字段，权重语法 `(term:1.4)`
- MJ 系：`--no term1, term2` 参数（无权重，整词排除）
- 视频 AI（Gen3/Kling）：多数无负向字段→靠正向提示词精炼+MJ 先出干净关键帧
- 负向=主动排除崩坏，比事后修图快十倍

## SD 系权重语法
```
(term:1.4)   强排除
(term:1.2)   中等
(term:0.8)   弱排除（边缘抑制）
```
- 权重>1.5 容易翻车——画面整体崩
- 权重<0.8 接近无效

## 通用负向清单（基础包）
```
(worst quality:2), (low quality:2), (normal quality:2),
lowres, watermark, signature, username, artist name,
bad anatomy, bad hands, error, missing fingers, extra digit,
fewer digits, cropped, jpeg artifacts, blurry
```
- 这是几乎所有 SD 出图都该加的"安全网"

## 分部位崩坏排除（动漫人物）

### 手部（最高频翻车）
```
(bad hands, poorly drawn hands, malformed hands:1.4),
(wrong number of fingers, too many fingers, missing fingers:1.4),
(fused fingers, merged fingers, webbed fingers:1.3),
(extra fingers, fewer fingers, four fingers, six fingers:1.4),
(deformed fingers, twisted fingers, bent fingers:1.2)
```
- 手是动漫出图崩坏重灾区——权重给到 1.4

### 面部
```
(asymmetrical face, deformed eyes, crossed eyes:1.3),
(mutated hands, poorly drawn eyes, bad face:1.4),
(long neck, malformed limbs:1.2)
```

### 身体
```
(bad proportions, extra limbs, missing limbs, fused limbs:1.4),
(torso too long, disfigured, malformed:1.3)
```

## MJ 的 --no 用法
```
/imagine prompt: [正向词] --no text, watermark, blur, signature
```
- MJ 的 --no 不支持权重，只能整词排除
- 多个用逗号分隔
- 适合排除：文字水印、模糊、签名、logo
- 不适合排除：复杂结构（手、脸）——MJ v6+ 手已经稳，加 --no 反而易翻

## 视频AI的"伪负向"
视频 AI 没有 negative 字段，但有三种等效做法：
1. **MJ 先出干净关键帧**→图生视频带过崩坏（最稳，见 087）
2. **正向精炼**：只写想要的动作，别提"不要抖"——AI 听不懂"不"
3. **seed 锁定**：同一 seed 多次抽→选最干净那版（见 114）

## 张力场景的负向补充

### 战斗/动作场景
```
(motion blur errors, duplicate limbs, extra arms:1.4),
(weapon fusion, merged weapon, deformed weapon:1.3),
(static pose, stiff movement:1.0)
```

### 静态张力场景
```
(busy background, cluttered scene:1.2),
(flat lighting, evenly lit:1.3),
(centered composition, symmetrical:1.0)
```
- 静态张力靠"留白+失衡"——负向帮排除均匀光/居中

## 常见坑
- **负向堆太多**：>20 词→画面整体变弱，色彩发灰
- **权重给太高**：`(term:2.0)`→崩
- **MJ --no 加复杂词**："--no bad hands"→MJ 反而乱画
- **视频AI写"不要抖"**：AI 听不懂否定→反向加强抖动
- **复制别人的负向清单**：不同模型需要的负向不同——要试

## 进阶
- **按场景定制负向包**：战斗/特写/群像分别存不同 negative
- **动态调权重**：先 1.2 试，崩了再加到 1.4
- **正负协同**：正向写"dynamic pose"，负向写"static pose"=双向夹击
- **Embedding 负向**：SD 用 textual inversion（如 EasyNegative）省词

## 备注
- SD 负向是核心机制，MJ --no 是辅助
- 视频 AI 靠正向精炼+关键帧过滤=等效负向
- 手部权重 1.4 是动漫出图黄金值
- 关联：087 MJ分镜、088 角色一致性、111 公式
