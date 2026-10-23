---
title: 技能魔法特效与提示词模板二十连⑰——粒子系统概念→AI替代：从发射器思维到提示词翻译
category: 提示词技巧
tags: [粒子系统, 粒子特效, particle system, Trapcode Particular, 发射器, AI替代, 提示词模板, VFX]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 粒子系统核心概念（发射器/生命周期/物理/父子级）可直接翻译为AI提示词；AI替代不是复制粒子系统而是翻译其思维；减法提示（Subtractive Prompting）一次只加1-2个粒子描述；提供粒子类型→提示词映射表与3套模板
related: [378, 348, 355, 356, 349]
---

# 技能魔法特效与提示词模板二十连⑰：粒子系统概念→AI替代

## 核心要点

- **粒子系统四概念可直接翻译为AI提示词**：发射器（Emitter）→ 源头描述（`erupting from palms`）；生命周期（Life）→ 粒子状态（`birth → drift → fade`）；物理（Physics）→ 运动动词（`swirling / drifting / suspended`）；父子级（Parent/Child）→ 主次粒子分层（`main burst + trailing embers`）
- **减法提示（Subtractive Prompting）是粒子AI的关键**：一次只加1-2个粒子描述词，让AI把"渲染预算"集中在这些粒子的清晰度和运动上——加太多粒子类型=全部糊成噪声
- **具体名词优于抽象名词**：`dust motes dancing` > `particles`；`fine atmospheric haze` > `fog`；`suspended particulates` > `debris`——AI对具体名词有latent理解，对抽象名词会乱画
- **焦点分层制造深度**：`some bright and in focus near camera, others soft and blurred in background`——不写焦点=全部清晰=平面感
- **AI粒子≠传统粒子**：AI生成的是"看起来像粒子系统"的效果，帧级不可控、跨镜漂移；传统粒子系统（Trapcode Particular等）帧级可控、可复用——严肃项目用混合流（AI出主料+AE补交互）

## 详细内容

### 一、粒子系统四概念→AI提示词翻译表

| 粒子系统概念 | 传统定义 | AI提示词翻译 | 示例 |
|---|---|---|---|
| **发射器 Emitter** | 粒子生成位置和速率 | 源头+速率描述 | `erupting from their palms, a steady stream` |
| **生命周期 Life** | 出生→存活→死亡的时间曲线 | 粒子状态描述 | `glowing brightly at birth, drifting for 3 seconds, fading into nothing` |
| **物理 Physics** | 重力/风力/湍流/碰撞 | 运动动词+环境交互 | `swirling upward on air currents, bouncing off the ground` |
| **父子级 Parent/Child** | 父发射器发射子发射器 | 主次粒子分层 | `main burst of sparks, trailing smaller embers behind` |

### 二、粒子类型→提示词映射

| 粒子类型 | 具体名词 | 运动动词 | 生命周期描述 | 适用场景 |
|---|---|---|---|---|
| 火花/余烬 | glowing embers | drifting upward / floating sideways | bright at birth, fade as they rise | 火焰/爆炸后 |
| 魔法尘 | golden motes of light | suspended / dancing in air | appear slowly, drift, fade | 治疗/神圣 |
| 烟雾 | thick billowing smoke | rolling outward / clinging to ground | dense at source, thinning as it spreads | 暗影/诅咒 |
| 能量粒 | incandescent particles | flowing backwards / spiraling | pulsing with light, then gone | 时间/传送门 |
| 数据片 | cascading binary code | falling upward / glitching | flicker in and out | 科技/赛博 |
| 花粉/孢子 | glowing pollen / spores | rising gently / floating on wind | appear, drift, settle | 自然/德鲁伊 |
| 灰烬 | fine black ash | swirling downward / settling | float slowly, land, disappear | 毁灭/死灵 |

### 三、减法提示清单（Subtractive Prompting）

```
STEP 1 - 先确定光源：
  → `sunlight streaming through broken window` / `the spell itself is the key light`
STEP 2 - 只加1-2个粒子描述：
  → 好：`dust motes dancing in the light beam`
  → 坏：`dust motes, pollen, sparks, ash, smoke, embers, debris`（太多，全部糊掉）
STEP 3 - 给焦点分层：
  → `some bright and in focus near camera, others soft and blurred in background`
STEP 4 - 给运动方向：
  → `floating upward on gentle air currents` / `swirling in a slow vortex`
```

### 四、AI粒子 vs 传统粒子系统：决策流程

```
这个粒子效果全剧出现几次？
├─ 1-2次（剧情奇观）→ AI直出 + 轻微合成（AE补交互光）
├─ 3次以上（招牌技粒子）→ 做元素板/正典帧（374/356），批次复用
├─ 每集都用（环境氛围粒子）→ 固化提示词模块+种子（396），绝不重写
└─ 需要精确控制（UI粒子/数据流）→ 传统粒子系统（AE/Blender），AI只做底图
```

### 五、常见翻车与修复

| 翻车 | 原因 | 修复 |
|---|---|---|
| 粒子糊成噪声 | 太多粒子类型 | 减法提示，只留1-2种 |
| 粒子像贴纸 | 无光源交互 | 补`dancing in the light beam`, `catching the glow` |
| 无深度 | 全部清晰 | 补`some in focus, others blurred in background` |
| 粒子不动 | 无运动动词 | 补`drifting / swirling / suspended` |
| 跨镜粒子漂移 | AI不可控 | 做正典帧锁定（374），或换传统粒子 |

## 关键参数 / 模板 / 清单

**模板A：魔法尘粒子（治疗/神圣场景）**
```
35mm medium shot, slow push in. A healer kneels in a sunlit
forest clearing. Golden motes of light appear around their
hands, suspended in the air like dust caught in a sunbeam.
Some motes are bright and in focus near the camera, others
soft and blurred in the background. The motes dance and drift
on gentle air currents, slowly rising upward. As they rise,
they fade from bright gold to transparent. The healer's face
is lit from below by the soft glow of the particles. Cinematic,
photorealistic, shallow depth of field, film grain.
Negative: anime, cartoon, too many particles, all in focus,
no motion, flat lighting, game FX, 2D
```

**模板B：火花余烬粒子（爆炸/战斗后）**
```
24mm wide angle, locked camera. The aftermath of a massive
explosion on a battlefield. Thousands of glowing orange embers
drift through the dark smoky air, floating upward and sideways
on gentle thermal currents. Some embers are bright and sharp
in the foreground, others soft and blurred in the background.
The embers are brightest at their birth near the blast point,
fading to dull red as they rise and cool. Smoke billows slowly,
catching the light from the embers. The ground is littered with
debris, some still glowing. Cinematic, gritty, photorealistic,
film grain, volumetric lighting.
Negative: anime, cartoon, no depth, all particles same size,
no fade, no smoke, flat lighting, game FX
```

**模板C：能量粒子流（时间/传送门场景）**
```
85mm close-up, slight slow motion. A time mage extends their
hand toward a swirling temporal rift. Streams of incandescent
gold chronon particles flow backwards from the rift into their
palm — a reverse river of light. The particles spiral around
their arm, pulsing with light, then vanish as they touch the
skin. Some particles are sharp and in focus, others blurred
in the background. The particles leave faint trails of light
in the air that slowly fade. The mage's face is illuminated
by the flowing particles, casting upward shadows. Cinematic,
photorealistic, film grain, shallow depth of field.
Negative: anime, cartoon, forward flow, no pulse, no trails,
flat lighting, game FX, 2D
```

**关键负向词（粒子系专用）**
```
anime, cartoon, too many particle types, all in focus, no motion,
flat lighting, game FX, 2D, no depth, uniform particles, no fade,
no source, no interaction, 3D render
```

## 备注

- 海裂映射：岩骨的"地脉共鸣"粒子=`gray-brown dust motes rising from the ground, pulsing with faint orange inner light`; 弦音的"声弦"粒子=`golden string-like particles vibrating in the air, humming at visible frequencies`; 白泽的"深渊共感"粒子=`bioluminescent indigo plankton-like motes drifting downward like marine snow`
- 与348特效可信度总纲联动：粒子是"世界交互"的最小单位——`smoke curling around objects`, `dust motes in light beams`让特效"存在"于空间中
- 与355特效×人物联动：粒子与人物的交互是关键——`particles clinging to armor`, `dust settling on shoulders`, `embers caught in hair`
- 与356后期合成联动：AI粒子做"主料"（氛围/环境粒子），AE粒子做"交互"（接触面/跟踪）——混合流标准分工
- 与374视觉开发管线联动：粒子正典帧=锁定粒子类型/颜色/密度/运动方向，确保跨镜一致性
- 运镜建议：粒子镜头最适合慢推（slow push in）或锁定（locked camera）——运镜越快粒子越糊；粒子是"氛围主角"时，人物可以是剪影
- 声画对位：粒子有声——`embers crackling softly`, `dust motes humming`, `energy particles buzzing`——声音让粒子"活"起来
