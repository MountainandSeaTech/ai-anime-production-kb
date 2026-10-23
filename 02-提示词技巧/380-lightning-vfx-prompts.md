---
title: 技能魔法特效与提示词模板二十连③——雷电与电弧：源-终点坐标、电流脉冲与湿面反光
category: 提示词技巧
tags: [雷电, 电弧, lightning, plasma, 提示词模板, VFX, AI视频, 电流]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 雷电特效的命门是"起点和终点"：AI必须知道电弧从哪里来、打到哪里，否则只会画天空闪电；用蓝白等离子+环境湿面反光+闪烁硬阴影制造高能感；提供3套模板
related: [379, 378, 354, 355, 304]
---

# 技能魔法特效与提示词模板二十连③：雷电与电弧

## 核心要点

- **电弧需要坐标**：AI不懂"闪电"这个词，要写明起点（手掌/乌云/电极）和终点（目标/地面/金属物），电弧才会定向
- 雷电的真实感来自**环境导电**：湿地面反光、金属物感应起弧、空气电离的辉光——干燥地面上的闪电永远是特效贴图
- 节奏必须是**脉冲**：不是常亮，是0.2s爆亮→暗→再爆亮，提示词用 `flickering intensely` / `rapid strobe` 而非 `constant glow`
- 声画同步：闪电帧与雷鸣帧对齐（接304），AI视频常音画脱节，需在提示词锁定 `thunder crack synchronized with flash`

## 详细内容

### 一、雷电三形态与写法

| 形态 | 特征 | 提示词关键词 |
|---|---|---|
| 天降雷 | 粗、分叉、落地烟尘 | `massive lightning bolt striking down, branching forks, impact crater with dust burst` |
| 手放电弧 | 细、扭曲、持续连接 | `thin electrical arcs crackling between fingertips, blue-white plasma tendrils` |
| 电网/雷域 | 多弧交织、环境覆盖 | `web of interlacing lightning covering the ground, ionized air glowing purple` |

### 二、源-终点公式（必写）

```
[Source] arcing a violent [color] electrical bolt toward [Target]
```
示例：`A single violent electrical arc jumping from the caster's palm to a grounded metal pipe`
- 无终点=AI只会画天空背景闪电，与剧情无关

### 三、环境交互四要素

1. **湿面**：`wet concrete floor reflecting the flash` / `rain-slicked surface`
2. **金属感应**：`nearby metal objects humming with residual charge` / `sparks jumping to railings`
3. **空气电离**：`ionized blue haze in the air` / `ozone glow`
4. **阴影**：`sharp hard shadows cast by the strobe light`（非柔和阴影）

### 四、AI直出vs合成

- **AI直出**：适合天降雷、风暴背景；手放电弧易断帧，需补合成
- **合成路线**：AI生成背景雷暴 → AE中做电弧遮罩（Saber插件或手动mask）→ 叠加环境闪光层（Adjustment Layer曝光脉冲）
- 颜色纪律：电光永远蓝白（`electric blue` / `violet-white`），禁橙红（那是火）

## 关键参数 / 模板 / 清单

**模板A：掌心电弧（近景/起手）**
```
85mm close-up, locked camera. A caster's hand clenches into a fist.
Thin blue-white electrical arcs crackle and jump between the knuckles
and a metal bracelet on the wrist — the source and termination points
are visible. The arcs flicker intensely in rapid pulses, casting sharp
hard shadows on the caster's face. Ionized blue haze fills the air
around the hand. Wet concrete floor below reflects the electric glow.
Cinematic, high contrast, subtle film grain.
Negative: anime, cartoon, constant glow, soft shadows, orange fire,
smooth curves, 3D render
```

**模板B：天降神雷（广角/打击）**
```
24mm wide angle, slight low angle. Massive storm clouds rotate
overhead. A thick lightning bolt strikes down from the cloud bank,
branching into violent forks. It impacts the ground with a burst of
white flash and upward dust explosion. The bolt terminates at a
specific cracked stone altar. Rain-slicked ground reflects the flash.
Nearby metal weapons hum and spark with residual charge. Thunder
synchronized with the flash. Cinematic, gritty, film grain.
Negative: anime, cartoon, clean lightning, no impact, constant light
```

**模板C：雷电变身/领域（全景/氛围）**
```
35mm cinematic shot, slow orbit. A figure stands in a dark field as
a web of interlacing purple-white lightning covers the wet ground
around them, spreading outward in pulses. Each pulse illuminates
the scene with strobe-like hard shadows. The air shimmers with
ionized particles. Rain freezes mid-air briefly with each flash.
The figure's hair stands on end from static. Storm clouds rotate
above, internal lightning flashing continuously. Cinematic, primal,
photorealistic.
Negative: anime, cartoon, smooth curves, soft lighting, constant glow
```

**关键负向词（雷电专用）**
```
anime, cartoon, 3D render, CGI, smooth curves, constant glow, soft shadows,
orange/yellow electricity, fire, clean sky, no impact, static lightning,
unrealistic fork symmetry
```

## 备注

- 海裂映射：弦音的"声弦操控"可借电弧模板改色（金色弦波），但需把 `crackle/jump` 改为 `resonate/vibrate` 以区分电与声
- 与379联动：雷火双修法=火球+雷击复合技，提示词中需明确主光源（雷蓝白压制火橙红），防止AI混成"橙色电"这种四不像
