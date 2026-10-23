---
title: Runway Gen-3 视频生成使用要点
category: 工具与模型
tags: [runway, gen3, 视频生成, 图生视频, WAN3]
source: 实测
created: 2026-10-13
updated: 2026-10-13
summary: Gen-3 图生视频的提示词结构、参数控制与动漫短剧适配要点
related: [003, 004]
---

# Runway Gen-3 视频生成使用要点

## 核心要点
- Gen-3 Alpha 支持 text-to-video 与 image-to-video，动漫短剧主用 image-to-video 锁定首帧构图
- 提示词遵循「镜头运动 + 主体动作 + 环境/氛围 + 风格」四段式
- 单段 5-10 秒，长动作需切片分段生成再拼接

## 提示词结构
```
[镜头运动], [主体] doing [动作], in [环境], [光照/氛围], [风格关键词], [负面约束]
```
示例（动漫短剧打戏）：
```
slow dolly in, anime girl with white hair doing iaido slash draw motion, in moonlit courtyard, dramatic rim light, cel-shaded anime style, 24fps, no morph, no extra fingers
```

## 关键参数
- motion brush：可画运动区域引导局部动作，适合衣摆/头发飘动而身体不动
- camera motion：宋移/推拉/横摇二选一，组合运动容易导致主体畸变
- seed：固定 seed 便于复现与微调，改提示词保留 seed 可做对比
- 时长：5s / 10s，10s 段尾部易崩，建议优先 5s 拼接

## 动漫短剧适配
- 锁首帧：先用 SDXL/Flux 产出角色卡作为 image-to-video 输入，保证一致性
- 动作幅度小：居合一斩这类瞬发动作，给「准备姿势 → 出刀瞬间」即可，不要让模型脑补完整挥砍
- 负面词必备：`no morph, no extra fingers, no face distortion, no background melt`
- 多次生成取优：同提示词跑 4-6 次，挑最稳的一版

## 备注
- Gen-3 对写实强、对纯动漫线稿易过曝/糊，建议输入图带轻度渲染质感
- 10s 段第 7 秒后常出现手指融合，长段优先拆 5s
- 复杂多人交互（如背靠背双角色）成功率高不了，建议分角色单独生成再合成

## WAN3.0 校准（2026-10-20）
- 本条目基于旧模型参数（5-10s / 24fps / 纯视频），保留为旧模型参考
- WAN3.0 已替代为基准模型：30s原生 / 30fps原生 / 原生音画 / 10图多模态参考 / 本地编辑
- 如需适配 WAN3，请参照 447-wan3-calibration-baseline.md
