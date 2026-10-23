---
title: 品牌→动效参数推导表（产品宣传片视觉节奏）
category: 张力与节奏
tags: [产品宣传片, 动效参数, 品牌性格, easing, 节奏预设, 能量轴, 调性轴]
source: GitHub-Vincentwei1021/video-shotcraft
created: 2026-10-21
updated: 2026-10-21
summary: 不凭手感挑 easing/时长——把品牌放到能量轴×调性轴两根轴上，从最近的预设起步；6 个品类预设含主时长/easing/过冲/squash
related: [452, 454, 023, 357, 260]
scope: 产品宣传片支线；参数为动画引擎级（easing/bezier），AI 生成需转译为定性描述
---

# 品牌→动效参数推导表（产品宣传片视觉节奏）

> 核心思想：**不凭手感挑 easing/时长，先把品牌放到两根轴上，再从最近的预设起步。**

## 两轴定位法

| 轴 | 低端 | 高端 | 决定什么 |
|---|---|---|---|
| **能量轴** | 沉稳/premium/机构感 | 运动/startup/娱乐 | 时长、过冲幅度、squash 幅度 |
| **调性轴** | 严肃（金融/医疗/enterprise） | 活泼（消费/社交/儿童） | 路径曲直、次级动作多寡 |

**定位证据**：产品视觉本身是证据（锐利几何形→工程感，圆角+亮色→柔和活泼）；用户口述的品牌词覆盖视觉推断。

## 6 品类预设表（@30fps）

| 预设（品类） | 主时长 | 入场 easing | 过冲 | squash |
|---|---|---|---|---|
| 专业信赖（fintech/enterprise/B2B） | ~21f | bezier(0,0,0.2,1) | 1.0 不弹 | 0 |
| 精致高端（奢侈品/时尚） | ~48f | bezier(0.4,0,0.6,1) | ≤1.02 | 0 |
| 活力大胆（体育/游戏/startup） | ~18f | bezier(0.16,1,0.3,1) | 1.12 | 0.25 |
| 活泼愉悦（消费/社交） | ~27f | bezier(0.34,1.56,0.64,1) | 1.08 | 0.18 |
| 平静关怀（健康/教育） | ~42f | ease-in-out 对称 | 1.0 | ≤0.04 |
| 亲和友好（小微/社区） | ~26f | bezier(0.25,0.46,0.45,0.94) | 1.04 | 0.08 |

**用法**：定预设 → 按两轴微调 → tokens 写进设计 spec。

**两条自检**：
1. 用三个词描述成片动效，与品牌词对得上吗？
2. 同一套 tokens 必须同时管入场/转场/hold 节奏——**一个品牌一种动效嗓音，混用两套读作拼盘**。

**注意**：预设值与硬判例冲突时判例赢。落地要弹的场合 y1 必须 >1；"专业信赖不弹"指的是无落地隐喻的淡入/推移类动作。

## AI 生成转译表

> 上表参数是动画引擎级（bezier/squash），WAN3 提示词无法精确控制，需转译为定性描述。

| 预设 | WAN3 定性描述 |
|---|---|
| 专业信赖 | `steady, deliberate motion, no bounce, clean linear easing, professional, restrained` |
| 精致高端 | `slow, elegant motion, minimal overshoot, premium, refined, smooth easing` |
| 活力大胆 | `fast, energetic, bouncy motion, strong overshoot, dynamic, punchy` |
| 活泼愉悦 | `playful, springy motion, gentle bounce, lively, casual, fun` |
| 平静关怀 | `gentle, calm motion, symmetrical ease, soothing, soft, caring` |
| 亲和友好 | `friendly, approachable motion, subtle bounce, warm, welcoming` |

## 备注

- 本参数表源自产品宣传片领域（UI 动效），动画引擎级参数需转译为定性描述才能用于 AI 生成
- 核心价值：**用两轴定位代替手感选参数**，保证全片动效嗓音统一
- 关联：452（总纲）、454（流水线与审美）、023（切换频率）、357（特效叙事）、260（惯性与重量感）
