---
title: 技能魔法特效与提示词模板二十连⑦——岩石与大地：裂纹路径、重量感与尘雾层级
category: 提示词技巧
tags: [岩石, 大地, earth, rock, stone, 提示词模板, VFX, AI视频, 地震]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 大地魔法的核心是重量与裂纹：石柱必须缓慢升起+地面开裂+尘雾滚落，不能轻飘飘；裂纹要有方向性路径；提供3套模板
related: [378, 379, 383, 355, 260]
---

# 技能魔法特效与提示词模板二十连⑦：岩石与大地

## 核心要点

- **重量是大地系的灵魂**：石柱/石墙/巨石必须缓慢、沉重、有惯性——`slowly rising, grinding, seismic movement`，禁 `floating, light, quick pop-up`
- **裂纹有方向**：从施法者脚下向外辐射（radial cracks），或沿目标路径推进（advancing fracture line），AI常画成随机碎裂
- 尘雾是第二主角：每个岩石动作都伴随 `dust rolling off, debris scattering, ground trembling`
- 岩石表面必须有纹理：`weathered stone, cracked surface, moss in crevices`——光滑石头像泡沫道具

## 详细内容

### 一、大地系五形态

| 形态 | 动作 | 关键提示词 |
|---|---|---|
| 石柱突起 | 防御/障碍 | `stone pillar erupting from ground, slow grinding ascent, radial cracks spreading outward` |
| 地裂波 | 攻击/控制 | `fracture line advancing rapidly toward target, ground splitting open, dust bursting upward` |
| 石甲/石肤 | 变身/防御 | `rock armor forming on skin, stone plates interlocking, cracks glowing with inner heat` |
| 落石/山崩 | 范围攻击 | `boulders tumbling down slope, dust cloud billowing, ground shaking with each impact` |
| 沙土操控 | 软性地系 | `sand swirling into shapes, granular texture, particles falling and reforming` |

### 二、重量感三要素

1. **速度**：慢——`slow, grinding, laborious movement`
2. **声音**：低频——`deep rumbling, grinding stone friction, heavy thud on impact`
3. **环境反应**：`ground trembling, dust rising in sheets, loose stones bouncing`

### 三、AI生成穿帮

- **轻飘飘**：石柱瞬间升起 → 补 `slow, heavy, seismic`
- **无裂纹**：地面完好但石头冒出来 → 补 `radial cracks from the base, ground splitting`
- **无尘**：干净得像塑料 → 补 `thick dust rolling off, debris scattering`
- **无阴影**：石头像贴图 → 补 `casting long shadows, harsh directional light`

### 四、制作路线

- **AI直出**：石柱升起、地裂、山崩（大场面）
- **合成**：前景人物 + AI背景地裂 → AE匹配震动（Camera Shake）→ 尘土层叠加 → 地面裂纹遮罩
- 接260重量惯性原则：岩石动作必须符合物理惯性，启动慢、停止慢

## 关键参数 / 模板 / 清单

**模板A：石柱防御（中景/保护）**
```
35mm medium shot, locked camera. A massive stone pillar erupts from
the ground in front of the caster, rising slowly with a deep grinding
sound. Radial cracks spread outward from its base across the stone
floor. Thick dust rolls off its weathered surface. Loose pebbles
bounce from the tremor. The pillar is rough-hewn, cracked, with
moss in its crevices. It casts a long sharp shadow in the directional
light. Cinematic, gritty, film grain.
Negative: anime, cartoon, smooth plastic, fast pop-up, no cracks,
no dust, floating, clean edges
```

**模板B：地裂攻击（广角/追踪）**
```
24mm wide angle, tracking shot following the fracture line. A crack
in the earth advances rapidly from the caster's position toward the
target, splitting the ground open with a burst of dust and debris.
The crack is jagged and irregular, not straight. Stones and dirt
erupt upward along its path. The target scrambles backward as the
ground opens beneath them. Deep rumbling bass. Cinematic, gritty,
photorealistic.
Negative: anime, cartoon, straight clean line, no dust, no debris,
ground resealing, slow crack
```

**模板C：石甲变身（近景/细节）**
```
85mm close-up, slight slow motion. Stone armor forms across the
caster's forearm: rough granite plates slide up from beneath the
skin and interlock with a grinding sound. Cracks between plates
glow with faint orange inner heat. Dust and small pebbles fall
from the forming armor. The texture is weathered and ancient.
The caster's expression strains from the weight. Cinematic, harsh
side lighting, film grain.
Negative: anime, cartoon, smooth armor, glowing neon, instant
transformation, no weight, clean surface
```

**关键负向词（大地系专用）**
```
anime, cartoon, smooth plastic, floating rocks, instant appearance,
no cracks, no dust, clean surfaces, lightweight, fast movement,
glowing stone (unless specified), 3D render, CGI look
```

## 备注

- 海裂映射：岩骨的"地脉共鸣"核心模板——但需加入"石化代价"（皮肤逐渐变石，用模板C的慢速版本）；深渊之核的巨兽移动直接适用"seismic movement, each step cracking stone"
- 与379火焰联动：岩浆系=岩石+火，提示词写 `molten rock, cracked surface with orange glow from within, dripping lava`
- 与383风联动：沙尘暴=沙土操控+风，写 `sand swirling in vortex, granular texture, particles stinging skin`
