---
title: Midjourney 张力分镜图生成
category: 提示词技巧
tags: [张力, Midjourney, 分镜图, 关键帧, 提示词]
source: 网络学习
created: 2026-10-13
updated: 2026-10-13
summary: MJ 先出关键帧锁定构图光影，再喂视频AI动起来；分镜图是张力骨架
related: [016, 024, 029, 084, 088]
---

# Midjourney 张力分镜图生成

## 核心要点
- MJ 先出**关键帧**锁定构图/光影/角色——是张力骨架
- 再喂 Gen3/Kling/即梦 图生视频=一致性+构图稳
- MJ 不生成视频，但定调最准
- 提示词=镜头词+光影词+角色词+风格词

## 工作流（关键）
```
1. MJ 出关键帧（build/peak/release 各一张）
2. 挑选/垫图修改至张力够
3. 关键帧喂 Gen3/Kling/即梦 图生视频
4. 拼接剪辑（见 090）
```
- 顺序不能反：先动再调=崩；先图后动=稳

## 分镜图提示词结构
```
[镜头词] + [光影词] + [角色动作/表情] + [场景] + [风格词] + [参数]
```

### 镜头词
- low angle shot / high angle shot / eye level
- extreme close-up / close-up / medium / wide / extreme wide
- dutch angle（倾斜）= 不安/失衡
- over the shoulder / POV

### 光影词
- side lighting, high contrast = 半明半暗
- backlight, silhouette = 剪影
- single overhead light = 顶光/审讯感
- cold blue tone / warm orange tone
- volumetric light（体积光）= 神圣/压迫

### 风格词
- cinematic, film still, 35mm, anamorphic
- anime keyframe, cel shading
- ink wash painting, Chinese painting
- cyberpunk, neon

### 参数
- `--ar 16:9` 横屏 / `--ar 9:16` 竖屏
- `--style raw` 减MJ美化倾向=更真实
- `--chaos 5-20` 增加变化（张力构图更多样）
- `--stylize 250-500` 风格化强度

## 张力关键帧模板

### build 段（建压）
```
wide shot, lone figure in vast empty corridor, cold blue tone,
single overhead light, long shadows, oppressive silence,
cinematic, film still, 35mm --ar 16:9 --style raw
```

### peak 段（爆点）
```
extreme close-up, character eyes wide, sweat dripping,
high contrast side lighting, motion blur background,
speed lines, impact frame, anime keyframe --ar 16:9
```

### release 段（释放）
```
wide pull back, character walking away, dusk warm tone,
figure becoming small, empty street, melancholy,
cinematic film still --ar 16:9 --style raw
```

## 构图张力法则
- **三分法+留白**：主体压边/角=失衡=张力
- **低角度仰拍**=压迫/威慑
- **倾斜构图**=不安/失衡
- **框中框**（门框/窗/阴影框）=困局
- **引导线**（走廊/柱列/铁轨）= 逼迫视线=压迫

## MJ → 视频AI 的衔接要点
- MJ 出图后**不要大幅改提示词**——视频AI按图生成
- 选张力最强的那帧（多 seed 抽）
- 角色定妆图固定一张，全片复用=一致性（见 088）
- 风格统一：全片同一 `--style` 同一风格词

## 常见坑
- **只出一张图直接动**：没分 build/peak/release→无节奏
- **MJ美化太重**：不加 `--style raw`→奶油感→张力散
- **构图太满**：主体居中填满→无留白→无张力
- **光影太平**：没光影词→均匀光→无对比→无张力

## 进阶
- 垫图（/blend 或 image prompt）锁角色/场景
- `--sref` 风格参考锁全片风格统一
- 多 seed 抽张力最强帧（同一提示词跑4次）
- MJ 出关键帧集（5-8张）= 整片分镜板

## 备注
- MJ 定调最准，但不生成视频
- 工作流：MJ出关键帧→喂视频AI→拼接
- 提示词=镜头+光影+角色+场景+风格+参数
- 构图张力：三分留白/低角度/倾斜/框中框/引导线
- `--style raw` 减美化=张力加分
- `--sref` 锁全片风格统一
