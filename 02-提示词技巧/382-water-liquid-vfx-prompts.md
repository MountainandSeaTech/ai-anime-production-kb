---
title: 技能魔法特效与提示词模板二十连⑤——水流与液体魔法：高光衰减、粘性控制与慢动作皇冠
category: 提示词技巧
tags: [水, 液体, water, liquid, splash, 提示词模板, VFX, AI视频, 流体]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 液体特效真实度70%取决于静态帧的高光衰减而非运动提示词；水系魔法要区分清水/粘稠液/蒸汽三态；慢动作液体皇冠是最高性价比镜头；提供3套模板
related: [378, 381, 350, 354, 355]
---

# 技能魔法特效与提示词模板二十连⑤：水流与液体魔法

## 核心要点

- **液体真实度的秘密在静态帧**：高光衰减（specular roll-off）决定质感，运动反而次要——先确保单帧看起来像水，再让它动
- 水系魔法必须区分**三态**：清水（transparent, fast, splash）、粘稠液（viscous, slow, heavy）、蒸汽/雾（mist, diffuse, volumetric）——AI常混为一谈
- 慢动作是液体的朋友：AI生成慢动作液体皇冠（crown splash）比实时流体更稳定；但人物动作会连带变慢，需分离处理
- 水不发光：禁止 `glowing water`，除非明确是魔法附魔水（且需写 `subtle inner glow, not neon`）

## 详细内容

### 一、水系三态与提示词

| 形态 | 物理特征 | 提示词关键词 |
|---|---|---|
| 清水 | 透明、快、溅射、表面张力 | `crystal clear water, sharp specular highlights, surface tension, fast splash dynamics` |
| 粘稠液 | 蜂蜜/油质感、慢、拉丝 | `viscous liquid, slow motion, thick strands, heavy dripping, glossy sheen` |
| 雾/蒸汽 | 弥散、体积光、无固定形 | `volumetric mist, diffused light rays, floating water droplets, atmospheric haze` |

### 二、五种经典水系魔法镜头

1. **水鞭**：`water whip lashing through air, maintaining surface tension until impact`
2. **水弹**：`compressed water sphere, rotating slightly, trailing droplets`
3. **巨浪**：`massive wave rising, curling at the crest, foam and spray`
4. **治愈水**：`gentle floating water orbs, soft caustic light patterns on skin`
5. **血/毒液**（变体）：`dark viscous liquid, unnatural movement, subtle iridescent sheen`

### 三、AI生成穿帮清单

- **果冻水**：无高光、无折射 → 补 `sharp specular highlights, refraction through droplets`
- **无重量**：水悬浮不落 → 写 `gravity pulling water down, splashing on ground`
- **断流**：水鞭中途断裂 → 写 `continuous stream, maintaining cohesion until impact`
- **干燥**：水打在人身上不湿 → 写 `clothing soaking wet, water dripping from chin and fingers`

### 四、制作路线

- **AI直出**：慢动作液体皇冠、水鞭、巨浪（单镜头）
- **合成**：AI生成水花元素（黑底）→ AE Screen模式叠加 → 人物衣服补湿（深色贴图+高光增强）→ 地面补涟漪（Displacement Map）
- 声音：高频水花声+低频涌动声分层（接304）

## 关键参数 / 模板 / 清单

**模板A：水鞭攻击（中景/动作）**
```
35mm medium shot, slight slow motion. A whip of crystal clear water
lashes through the air from the caster's hand, maintaining surface
tension as a continuous stream. Sharp specular highlights reflect
off its curved surface. It strikes a wooden training dummy with a
heavy splash — water droplets fly outward in all directions, gravity
pulling them down immediately. The caster's sleeve is soaked and
dripping. Ground puddles ripple from the impact. Cinematic, natural
lighting, film grain.
Negative: anime, cartoon, glowing water, jelly texture, static water,
dry clothing, floating droplets, 3D render
```

**模板B：慢动作液体皇冠（特写/美学）**
```
100mm macro lens, extreme slow motion (Phantom camera style). A
drop of water falls into a still pool, creating a perfect crown-shaped
splash that rises upward in slow motion. Sharp specular highlights
glint off each water spike. The background is dark, making the
crystal-clear water stand out. Tiny droplets separate from the
crown tips, suspended in air with surface tension visible. Deep
shadows, high contrast, luxurious commercial aesthetic.
Negative: anime, cartoon, fast motion, choppy, glowing, colored liquid,
plastic texture
```

**模板C：巨浪术（广角/史诗）**
```
24mm wide angle, low angle looking up. A massive ocean wave rises
from the ground in front of the caster, curling at the crest with
white foam and spray. The wave is ten meters tall, blocking out
the sky. Water cascades down its face in sheets. The caster stands
small at its base, arms raised, controlling it. The air is thick
with mist and spray. Cinematic, epic scale, overcast lighting,
photorealistic.
Negative: anime, cartoon, calm water, small wave, dry ground, sunny,
glowing water
```

**模板D：治愈水球（近景/柔和）**
```
85mm close-up, soft lighting. A gentle orb of water floats above
the caster's palm, rotating slowly. It is crystal clear with subtle
internal caustic light patterns dancing on the caster's skin below.
Tiny air bubbles are suspended inside. The surface tension is perfect,
not a single drop falls. Soft ambient light, warm skin tones contrasting
with cool water. Cinematic, intimate, shallow depth of field.
Negative: anime, cartoon, glowing orb, neon, splashing, dripping,
harsh lighting
```

**关键负向词（水系专用）**
```
anime, cartoon, glowing water, neon blue, jelly texture, plastic,
dry clothing, floating droplets, no gravity, choppy motion, 3D render,
CGI, thick oil (unless specified), mud
```

## 备注

- 海裂映射：白泽的"深渊共感"可借水系模板的"柔和漂浮"版本，把清水改为"深渊幽蓝液体光"，但保持 `subtle inner glow` 克制；深渊之核苏醒时的水墙用模板C的巨浪逻辑
- 与381冰霜联动：水→冰的转化提示词 = `water slowing, crystallizing at edges, surface tension hardening into ice`，保持连续运动
- 与379火焰联动：水火相碰时蒸汽爆炸 = `steam explosion from water meeting fire, white vapor bursting outward`
