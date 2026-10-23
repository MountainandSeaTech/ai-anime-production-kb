---
title: Runway Gen3 张力镜生成技巧
category: 工具与模型
tags: [张力, Runway, Gen3, AI视频, 运镜, 提示词, WAN3]
source: 网络学习
created: 2026-10-13
updated: 2026-10-13
summary: Gen3 善运镜不擅动作；用运镜建张力而非堆动作；锁定机位+缓推拉+单主体=稳
related: [016, 018, 024, 029, 081]
---

# Runway Gen3 张力镜生成技巧

## 核心要点
- Gen3 善**运镜**不擅复杂动作——用它建张力而非堆打戏
- 锁定机位 + 缓推拉 + 单主体 = 最稳产出
- 提示词要"摄影机语言"而非"角色动作"——扬长避短
- 5-10s 短镜拼接优于单镜长动作

## Gen3 的张力强项

### 1. 运镜张力（最强）
- 缓推（slow push-in）= 压迫/逼近/聚焦，张力直接拉满
- 缓拉（slow pull back）= 抽离/孤独/揭示，余韵强
- 环绕（orbit）= 包围/审视/压迫，反派/诡秘专用
- 低角度仰推（low angle push）= 压顶/巨物/威慑

### 2. 光影张力
- 高对比侧光（side lighting, high contrast）= 脸半明半暗
- 逆光剪影（backlight silhouette）= 神秘/未明
- 单色冷光（cold single tone）= 冷峻/死亡气息

### 3. 定格/慢镜
- bullet time / slow motion = 时间拉长=张力
- freeze frame = 凝固（但 Gen3 易抖，用短）

## Gen3 的短板（要避开）

| 弱项 | 表现 | 规避 |
|---|---|---|
| 复杂动作 | 多人打斗/换位→崩 | 拆成单主体单镜 |
| 手部细节 | 持物/手势易畸 | 避开特写手 |
| 长动作连贯 | 超5s动作→漂移 | 单镜≤5s拼接 |
| 表情微变 | 细微表情→糊 | 用大表情/侧脸 |

## 张力镜提示词模板

### 压迫推镜
```
cinematic slow push-in, low angle, lone figure standing in dim corridor,
single key light from above, high contrast shadows, shallow depth of field,
tense atmosphere, 24fps, anamorphic lens
```

### 抽离拉镜
```
slow pull back, character walking away down empty street at dusk,
camera retreating, figure becoming small, cold blue tone,
melancholy isolation, handheld subtle
```

### 反派环绕
```
slow orbit around standing villain, low angle, backlit rim light,
face half in shadow, cold expressionless, oppressive silence,
vertigo dolly zoom hint
```

### 慢镜张力
```
slow motion 120fps, debris floating mid-air, character turning head,
single overhead light, particles suspended, frozen moment of tension
```

## 拼接策略（关键）
- 单镜 5-8s 为单位，按 014 build-peak-release 编排
- build：缓推/环境镜（5s）
- peak：慢镜/特写/冲击帧（3-5s）
- release：拉远/空镜（3-5s）
- 镜间用剪映/达芬奇硬切或叠化，见 090

## 常见坑
- **提示词堆动作**：写"两人对打翻滚"→必崩；改成"两人对峙特写+切手部特写"
- **不写机位**：Gen3 随机机位→散；务必写明 push-in/pull back/orbit
- **过长**：单镜超 10s→漂移；拆短拼接
- **无光影词**：缺光影→平；必加 side light/backlight/contrast

## 进阶
- Gen3 + 参考图（image-to-video）锁构图：先 MJ 出关键帧，再 Gen3 动起来
- 多 seed 试抽：同一提示词跑 3-4 次选张力最强那条
- motion brush 局部动：只让某处动（眼睛/烟雾/衣角），其他静止=静中微动=张力顶配

## 备注
- Gen3 扬长：运镜/光影/慢镜/单主体
- Gen3 避短：复杂动作/手部/长连贯/微表情
- 提示词要"摄影机语言"不是"动作剧本"
- 单镜≤8s，拼接优于长镜
- 与 088 一致性配合：先锁角色图再 Gen3 动

## WAN3.0 校准（2026-10-20）
- 本条目基于旧模型参数（5-10s / 24fps / 纯视频），保留为旧模型参考
- WAN3.0 已替代为基准模型：30s原生 / 30fps原生 / 原生音画 / 10图多模态参考 / 本地编辑
- 如需适配 WAN3，请参照 447-wan3-calibration-baseline.md
