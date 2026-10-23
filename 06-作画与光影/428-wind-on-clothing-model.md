---
title: 风对衣服的作用模型：风向/风速/阵风/旋风的动态规则与延迟
category: 作画与光影
tags: [布料物理, 风场, 动画延迟, 裙摆, 提示词, AI视频]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 风向与摆向相反、风速决定摆幅（微风15°/强风45°/暴风90°+抽打）、衣摆追风延迟0.1-0.3秒、阵风与旋风的特殊动态
related: [406, 427, 429, 430, 431]
---

# 风对衣服的作用模型

## 核心要点

- **风向→摆向：反方向法则**（Newton 第三定律）。风从左吹来，衣角摆向右边；角色向前跑，"相对风"从前方来，衣摆向后摆（确定性：公认，物理公式）
- **风速→摆幅：蒲福风级直接对应角度**。无风=垂落、微风(2级)=15°、清风(4级)=45°、强风(6级)=90°水平、暴风(10级)=90°+抽打（确定性：公认）
- **衣摆追风延迟 0.1-0.3 秒（3-9 帧 @30fps）**：轻薄材质延迟短（0.1s）、厚重材质延迟长（0.3s）；披风 3-6 帧，大衣 2-4 帧（确定性：经验，RebusFarm + 动画师共识）
- 阵风（gust）是风速在 0.5-2 秒内突发变化，表现为**衣角突然加速摆过去再弹回**——区别于持续风的稳态摆动（确定性：公认）
- 旋风（vortex/whirlwind）不是单方向摆，是**衣角绕一个看不见的轴打转**——尤其长披风/长袍下摆最明显（确定性：经验）
- AI 视频写风时，必须同时写**风向 + 强度 + 材质响应 + 延迟**，只写 "windy" 会让 AI 乱加飘动（确定性：经验）
- 风场交互遵循 406 场景生机法则——风是环境微动的"驱动力"，风不写方向，衣角就瞎飘（确定性：公认）

## 详细内容

### 风向→衣角摆向：反方向法则

| 风的来源方向 | 衣角摆向 | AI 提示词写法 |
|---|---|---|
| 左风 | 右摆 | "wind blows from left, fabric billows to the right" |
| 右风 | 左摆 | "wind from right pushes garment leftward" |
| 前风（顶风） | 向后摆 | "headwind pushes coat hem backward" |
| 后风（顺风） | 向前盖 | "tailwind flips scarf forward over shoulders" |
| 上升气流 | 向上飘 | "updraft lifts skirt hem upward" |
| 下沉气流 | 向下压 | "downdraft presses fabric flat against body" |

> 物理本质：空气分子撞击布料表面，转移水平动量给布料——所以布料运动方向 = 风的反方向。动画中如果风从左来但衣角也向左摆，AI 视频观众瞬间感到"不真实"。

### 风速→摆幅：蒲福风级对应角度表

| 蒲福风级 | 风速 (m/s) | 通俗名称 | 衣角摆角（典型材质） | 视觉描述 | AI 提示词写法 |
|---|---|---|---|---|---|
| 0 | 0 | 无风 | 0° 完全垂直 | 衣服仅自然下垂褶皱 | "fabric hangs still, no wind" |
| 1 | 0.3-1.5 | 软风 | 5° 微抖 | 领口/袖口轻微颤动 | "very subtle fabric tremble at cuffs" |
| 2 | 1.6-3.3 | 轻风 | **15°** | 丝绸开始飘，皮革不动 | "gentle breeze, silk shifts about 15 degrees" |
| 3 | 3.4-5.4 | 微风 | **30°** | 棉布明显飘，麻布微动 | "light wind lifts fabric 30 degrees, visible sway" |
| 4 | 5.5-7.9 | 清风 | **45°** | 裙摆明显向外展开 | "moderate wind, skirt billows 45 degrees outward" |
| 5 | 8.0-10.7 | 劲风 | 60° | 头发乱、裙摆飘得远 | "stronger wind, hair flies, skirt billows steeply" |
| 6 | 10.8-13.8 | 强风 | **90°（水平）** | 衣角几乎水平，皮革也飘 | "strong wind, coat flutters almost horizontally" |
| 7 | 13.9-17.1 | 疾风 | 90°+ 抽打 | 衣角拍打身体/腿 | "near-gale wind, fabric slaps against legs" |
| 8+ | >17.2 | 大风/暴风 | 90°+ 猛烈抽打+飘带断裂 | 衣物被撕碎风险 | "violent storm wind, fabric rips and tears" |

> 角度数据：2/3/4/6 级为动画师通用参考（来源：Style3D 2026 风场模拟实验），0/1/8+ 为安全边界。皮革在 6 级以下仍不明显，金属甲仅发出哗啦声。

### 三种风的动态区别

| 风类型 | 定义 | 动态特征 | 提示词关键词 |
|---|---|---|---|
| **持续风 Steady Wind** | 方向/速度稳定（如户外恒风、风扇） | 衣角达到固定角度后小幅摆动振荡 | "steady wind, consistent billow angle" |
| **阵风 Gust** | 速度在 0.5-2 秒内突增/突降 | 衣角**突然加速大幅摆过去→弹力弹回→再回到稳态**（像被推了一下的秋千） | "sudden gust, fabric jerks then settles, snap-back motion" |
| **旋风 Vortex/Whirlwind** | 空气绕垂直轴旋转（如龙卷风/空调出风口） | 衣角**绕一个不可见轴打转**，长裙摆会螺旋向上卷 | "swirling vortex wind, skirt spirals and twists around invisible axis" |

#### 阵风 vs 持续风：关键动画区别

```
持续风（steady）：摆幅达到 45° → 小幅振荡 ±5°  → 保持
阵风（gust）：    摆幅达到 45° → 突然加速到 75° → 弹力弹回到 35° → 回到 45° 持续振荡
```

### 衣摆"追风延迟"（Lag/Follow-Through）

| 材质/结构 | 延迟时间（秒） | 延迟帧数（30fps） | 典型例子 |
|---|---|---|---|
| 丝绸/薄纱 | 0.1 | 3 帧 | 和服广袖被风推动比风到达晚 3 帧 |
| 棉布/毛衣 | 0.15-0.2 | 5 帧 | T 恤下摆滞后 |
| 麻布 | 0.25 | 7 帧 | 古风襦裙滞后明显 |
| 皮革 | 0.3 | 9 帧 | 皮衣下摆慢慢跟上 |
| 披风/斗篷 | 0.15-0.25 | **4-6 帧** | Elsa 的披风比躯干慢 5 帧（Frozen 参考） |
| 大衣下摆 | 0.2-0.3 | **6-9 帧** | Incredibles 超人披风滞后 |

> 数据来源：RebusFarm Follow-Through 指南、迪士尼动画师实践共识。**核心物理**：布料的"自由端"（远离身体的那一端）比"固定端"（领口/肩线）延迟更长——离重心越远，滞后越大。

#### AI 提示词中的延迟写法

```
EN: Cape lags 4 frames behind the hero's movement, fabric catches up a split second after he turns
中: 披风比主角动作滞后 4 帧，布料在他转身一瞬间才跟上
EN: Skirt hem trails behind 0.2 seconds after torso changes direction
中: 裙摆比躯干改变方向滞后 0.2 秒
```

### 相对风（Relative Wind）：角色运动产生的"假风"

角色跑步时，即使户外无风，相对于身体前方也有一股"顶风"——速度 = 跑步速度。

| 跑步速度 | 相对风速 (m/s) | 等效蒲福级 | 衣摆摆角 |
|---|---|---|---|
| 慢走 1 m/s | 1 | 1级 | 0-5° 微抖 |
| 快走/慢跑 2-3 m/s | 2.5 | 2级 | 15° |
| 跑步 4-5 m/s | 4.5 | 3级 | 30° |
| 冲刺 6-7 m/s | 6.5 | 4级 | 45° |
| 高速奔跑 8+ m/s | 8+ | 5+级 | 60-90° |

> 这是 AI 视频中角色奔跑时衣摆"自动向后飘"的物理依据——别忘记写"running fast, headwind from motion pushes coat hem backward"

## 备注

- 429 将详细展开"动作拉扯"场景（跑步/挥刀/摔倒/转身），包含相对风 + 惯性拉扯的叠加效果
- 430 讨论贴身 vs 宽松在风中的表现差异（紧身衣风响应 <5°，宽松衣按本表）
- 431 讨论裙摆/披风/长袍等特殊结构的独立动态公式
- 风场方向必须与 406 场景生机法则的环境微动统一——树叶往右边晃，衣角不能往左边飘
- 争议点：关于"延迟帧数"，不同动画工作室有 ±1 帧的容忍差，但 4-6 帧披风延迟是行业共识
