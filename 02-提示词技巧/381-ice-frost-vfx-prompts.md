---
title: 技能魔法特效与提示词模板二十连④——冰霜与寒气：冰晶层级、冻结冲击波与折射率
category: 提示词技巧
tags: [冰霜, 冰冻, ice, frost, freeze, 提示词模板, VFX, AI视频, 寒气]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 冰霜特效的核心是折射率与层级：冰晶必须透明折射光线而非发光；冻结冲击波要写出"霜纹扩散→冰层生长→蒸汽凝结"的时间顺序；提供3套模板
related: [378, 379, 350, 355, 354]
---

# 技能魔法特效与提示词模板二十连④：冰霜与寒气

## 核心要点

- 冰与火的本质区别：**冰不发光，冰折射光**；AI常把冰画成"发光的蓝色塑料"，必须明写 `refracting light` / `translucent crystal` / `caustics`
- 冻结是一个**过程**而非状态：霜纹扩散→冰层生长→目标表面结晶→蒸汽凝结成雾，提示词需写时间顺序
- 寒气=**雾+慢动作**：冷雾向下沉（冷空气密度）、物体表面白霜蔓延、呼吸成霜——这些比蓝色光效更真实
- 冲击波型冰冻（冰霜新星）要约束范围：`radius of 15cm` / `perfect circle expanding outward`，避免AI无节制铺满全屏

## 详细内容

### 一、冰霜五层结构（与火焰五层对位）

1. **霜纹**：地面/物体表面白色分支纹路（frost patterns spreading like veins）
2. **冰晶**：透明小晶体生长，折射光线（tiny translucent crystals growing, refracting ambient light）
3. **冰层**：厚冰覆盖，表面有内部折射与气泡（thick ice layer with internal caustics and trapped air bubbles）
4. **冷雾**：贴地白色雾气，缓慢流动（low-lying cold mist hugging the ground）
5. **蒸汽**：暖物体遇冷产生白色蒸汽（steam rising from warm surfaces meeting cold）

### 二、三种冰霜攻击型态

| 型态 | 动作 | 提示词核心 |
|---|---|---|
| 冰锥/冰枪 | 发射尖锐冰体 | `razor-sharp icicle projectile, trailing glittering frost particles, comet-like tail` |
| 冻结冲击波 | 圆形扩散冻结一切 | `blast wave of frost expanding in perfect circle, enemies frozen mid-motion into ice statues` |
| 寒气领域 | 持续范围减速/冻结 | `pale blue mist spreading outward, frost creeping up walls, breath turning to ice crystals` |

### 三、AI生成常见穿帮

- **塑料冰**：无折射、无内部结构 → 必须写 `translucent, refracting light, internal bubbles`
- **无重量**：冰锥悬浮 → 写 `heavy ice projectile, drops slightly due to gravity`
- **无冷雾**：干巴巴的冻结 → 补 `cold mist rolling off the impact point`
- **过蓝**：像霓虹灯 → 限制 `pale blue, desaturated, winter ambient light`

### 四、制作路线

- **AI直出**：适合冻结冲击波、冰锥飞行（单镜头）
- **合成**：AI生成冰层/冰柱元素 → AE叠加冷雾（Fractal Noise+Evolution）→ 人物面部补白霜（局部调色+纹理叠加）
- 声音设计：冰层碎裂高频脆响+低频呻吟（接304声画帧同步）

## 关键参数 / 模板 / 清单

**模板A：冰锥术（发射/中景）**
```
35mm medium shot, slow motion. A razor-sharp icicle projectile
launches from the caster's palm, spinning slightly. It is translucent
crystal, refracting ambient light into faint rainbow caustics on
the ground. A glittering trail of frost particles follows behind
like a comet tail. The air around it shimmers with cold distortion.
It impacts a stone wall with a burst of ice shards and white cold
mist rolling outward. Cinematic, shallow depth of field, subtle
film grain.
Negative: anime, cartoon, glowing ice, opaque plastic, blue neon,
warm lighting, 3D render
```

**模板B：冰霜新星（冻结冲击波/广角）**
```
24mm wide angle, overhead drone shot looking down. A powerful
blast wave of frost and ice erupts from the caster's position,
rapidly expanding outward in a perfect circle. The wave freezes
everything it touches: charging enemies become detailed ice statues
mid-stride, ground frost patterns spread like white veins, cold
mist rolls across the battlefield. The circle has a clear radius
boundary — beyond it, the world remains unfrozen. Pale desaturated
blue tones, winter ambient light. Cinematic, epic scale, film grain.
Negative: anime, cartoon, glowing ice, neon blue, symmetrical spikes,
warm colors, unlimited spread
```

**模板C：寒气领域（近景/氛围）**
```
85mm close-up, locked camera. Pale blue-white cold mist spreads
outward from the caster's feet, hugging the ground and flowing
slowly like liquid. Frost creeps up nearby stone walls in branching
patterns. The caster's breath turns into visible white vapor that
crystallizes into tiny ice particles in the air. A warm torch nearby
dims and sputters as frost coats its metal bracket. Translucent
ice crystals form on the caster's fingertips, refracting the dim
light. Cinematic, cold color grading, shallow depth of field.
Negative: anime, cartoon, glowing aura, bright blue, warm breath,
dry surfaces, no mist
```

**模板D：元素板专用（黑底冰晶生长）**
```
Translucent ice crystals growing rapidly on a black background,
starting from a central point and branching outward in fractal
patterns. Each crystal refracts light into faint caustics. Cold
white mist rolls off the base. No person, no environment. Raw VFX
element, photorealistic, 4k detail.
Negative: anime, cartoon, colored lighting, opaque material, warm tones
```

**关键负向词（冰霜专用）**
```
anime, cartoon, glowing ice, neon blue, opaque plastic, warm lighting,
no mist, no refraction, symmetrical perfect circles, 3D render, CGI look,
dry surfaces, fire, orange
```

## 备注

- 海裂映射：弦音的"声弦操控"可借冰霜的"透明折射"逻辑，把冰晶改为"空气中的可见声波纹路"，保持透明感；深渊之核的静默领域可反向用冰霜模板：不是冷，是"声音被冻结"
- 与350（水特效）联动：冰是水的一种状态，同一角色水系能力进阶为冰系时，提示词从 `flowing water` 改为 `crystallizing water, slowing into ice`，保持元素连续性
