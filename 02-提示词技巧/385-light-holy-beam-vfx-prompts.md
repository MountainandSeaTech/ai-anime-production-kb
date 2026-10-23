---
title: 技能魔法特效与提示词模板二十连⑧——光效/圣光/能量束：体积光三要素与光束分层结构
category: 提示词技巧
tags: [光效, 圣光, 能量束, light beam, god rays, volumetric lighting, holy light, 提示词模板, VFX, AI视频]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 光效AI生成第一死因是"看起来像画上去的"——缺散射介质；体积光必须同时写光源+介质+遮挡三要素；光束分核心/光晕/内部粒子/环境影响四层；色温即情绪（2000K暖金=安全，6500K冷白=孤绝）；提供3套模板
related: [378, 380, 354, 379, 290, 304]
---

# 技能魔法特效与提示词模板二十连⑧：光效/圣光/能量束

## 核心要点

- **光效AI生成第一死因：没有散射介质**——只写"god rays"得到的是贴图滤镜，必须写 `fog / dust particles / incense smoke / pollen` 让光"有东西可散射"，这是体积光与假光束的分水岭
- **体积光三要素缺一不可**：光源（source, 方向明确如 camera-left）+ 介质（medium, 雾/尘/烟）+ 遮挡（gap, 林冠缝隙/破窗/云洞）；三者齐则光束自然成形
- **光束分层结构**：核心（intensely bright core）→ 光晕（ethereal aura, shimmering, dissolving）→ 内部粒子（swirling motes / feathers / crystal shards）→ 环境影响（contact点裂纹、冲击波、长阴影）——只写"bright beam"等于只写了第一层
- **色温即情绪**：2000-3500K暖金=怀旧/安全/神圣，6500-10000K冷白=孤独/现代/审判；写光必须写色温，不写色温等于放弃情绪控制
- **咒语即光源**铁律：`the spell itself is the key light`——写清二次光（照在脸上的反光、手上的辉光）与环境变暗的对比，光才有重量

## 详细内容

### 一、假光束 vs 真光束：介质决定一切

AI生成光效最常见的问题是"看起来像Photoshop画上去的"。原因只有一个：**提示词里没有散射介质**。

- 假光束：`bright light beam shining down` → AI输出一个半透明白色渐变图层
- 真光束：`morning sunlight breaking through gaps in forest canopy, three distinct god ray beams slicing diagonally through thick volumetric fog, beams catching floating dust and pollen particles` → AI激活物理散射理解

**介质清单（按场景选）**：
- 森林：pollen, morning mist, floating dust
- 教堂/圣殿：incense smoke, centuries-old dust, atmospheric haze
- 战场：smoke from fires, kicked-up dust, ash particles
- 室内：dust motes in still air, light haze, steam
- 深海/水下：suspended particles, marine snow, plankton

### 二、光束分层结构（四层全写才立体）

```
LAYER 1 - 核心（Core）：intensely bright [color], blinding, radiating power
    ↓ 圣光=holy gold / 天界=cyan / 审判=crimson / 奥术=violet
LAYER 2 - 光晕（Aura）：softer, ethereal [color], shimmering, dissolving into air
    ↓  pale golden haze / wisps of silver / iridescent shimmer
LAYER 3 - 内部粒子（Particulates）：swirling [feathers/embers/crystal shards/runes]
    ↓ 运动方向：gracefully floating up / violently churning / cascading down
LAYER 4 - 环境影响（Impact）：contact reaction + shockwave + lighting change
    ↓ ground vitrifying / long sharp shadows / shockwave rippling outward
```

只写LAYER 1 = 便宜页游光效；四层全写 = 电影级圣光。

### 三、光与材质交互（Material Awareness）

不同材质让光"落地"的方式完全不同，提示词必须明确写出：

| 材质 | 关键提示词 | 物理行为 |
|---|---|---|
| 皮肤 | `rim light turning ear edges translucent amber`, `warm golden halo around hair` | 次表面散射 |
| 金属 | `specular highlights moving as camera pans`, `brushed metal catching directional rim light` | 镜面反射 |
| 玻璃/水晶 | `light refracting, rainbow caustics on surrounding surface`, `light splitting into spectral components` | 折射色散 |
| 水面 | `caustic patterns on underwater floor`, `golden shimmer as ripples catch low sun` | 焦散 |
| 石面 | `texture visible in raking sidelight`, `moisture catching glare` | 漫反射 |

### 四、方向、数量、角度——光束的精确控制

AI对光束的方向和数量极其敏感，必须明确：

- **方向**：`from camera-left` / `diagonal from upper-right` / `vertical column` / `raking at 15-degree angle`
- **数量**：`three distinct beams` / `a single column` / `a fan of five shafts`——不给数量AI就给随机数
- **角度**：`low 15-degree angle`（晨光/暮光）/ `near-vertical`（正午/天罚）/ `horizontal`（特殊戏剧效果）

### 五、常见翻车与修复

| 翻车 | 原因 | 修复 |
|---|---|---|
| 像画上去的 | 无介质 | 补 `volumetric fog / dust particles / incense smoke` |
| 平淡过曝 | 光源模糊 | 补具体光源+方向+色温 |
| 只有光没有影 | 没写对比 | 补 `surroundings fall into deep shadow`, `chiaroscuro contrast` |
| 颜色单薄 | 只写"bright" | 补 core+aura+ambient 三层色板 |
| 光不"动" | 无运镜交互 | 补 `camera slowly entering the light`, `dust swirling in the beams` |

## 关键参数 / 模板 / 清单

**模板A：天罚圣光（广角/审判感）**
```
24mm wide angle, low angle shot looking up. A wrathful, pulsating
celestial beam of molten holy gold strikes down from a churning
storm sky onto a corrupted battlefield. The beam's core is blinding
white-gold; its outer aura is a pale golden haze with crackling
energy arcs. Swirling within the column are ethereal feathers and
spiraling ribbons of pure light, violently churning upward.
Thick smoke and dust fill the air, making the beam sharply visible.
Where the beam contacts the ground, the earth cracks and vitrifies
into glass. A ring of fire and light ripples outward as a shockwave.
The surrounding darkness is pushed back, casting long sharp shadows.
Harsh chiaroscuro contrast, divine judgment mood. Cinematic, film
grain, 35mm, anamorphic lens flare.
Negative: anime, cartoon, flat lighting, no particles, constant
glow, soft edges, painting, illustration, 3D render
```

**模板B：治愈圣光（中景/神圣宁静）**
```
35mm medium shot, slow push in. A serene, perfectly-formed column
of soft silver-cyan light gently descends upon a wounded knight
kneeling in a ruined chapel. The core is intense pearl white,
the aura a shimmering iridescent mist. Billions of tiny dust
motes and faint angelic runes float gracefully upward through
the beam. Incense smoke drifts through the light, catching it.
Where the light touches the knight's wounds, a soft golden glow
spreads and the air shimmers. The surrounding stone is bathed
in cool ambient light, deep shadows in the corners. Sacred,
tranquil mood. Photorealistic, shallow depth of field, film grain.
Negative: anime, cartoon, harsh shadows, aggressive energy,
neon colors, game FX, oversaturated
```

**模板C：能量束攻击（近景/手持施法）**
```
85mm close-up, slight slow motion. A lone caster thrusts both
hands forward, palms open. A concentrated energy beam erupts
from their palms — intense sapphire core with a crackling
electric-blue aura, heat haze distorting the air around it.
The beam is the only light source: sharp blue-white highlights
on the caster's face and hands, deep cool shadows behind.
Miniature lightning arcs spiral along the beam's length.
The air smells of ozone. At the beam's terminus, a blinding
impact flash and a ring of compressed air expanding outward.
Cinematic, photorealistic, film grain, shallow depth of field.
Negative: anime, cartoon, constant glow, soft edges, no heat
distortion, flat lighting, CGI look
```

**关键负向词（光效专用）**
```
anime, cartoon, flat lighting, no particles, constant glow,
soft edges, painting, illustration, 3D render, CGI look,
game FX, oversaturated glow, neon cyberpunk (unless specified),
lens flare on everything, no shadow contrast
```

## 备注

- 海裂映射：白泽的"深渊共感"视觉化可用冷调能量束变体——核心青紫、光晕幽蓝、内部粒子为缓慢下沉的发光微生物，接触点无声吸收而非爆炸（静默领域）；与弦音的金色弦波形成色温对立
- 与380雷电联动：雷电+圣光=审判系，提示词写 `lightning wrapped around a column of holy light, electric arcs dancing across the beam's surface`
- 与354光效方法论联动：354讲"光为什么这么打"，本条讲"具体怎么写"；354的廉价发光病表在本条负向词中全部落地
- 色温速查：神圣/治愈=2700-3500K（金白），天界/奥术=5000-6500K（青白），审判/毁灭=6000K+偏蓝白，深渊/诅咒=向青紫偏移但压暗亮度
- 运镜交互：光效镜头最忌静态——`camera slowly entering the light` / `dolly through the god rays` / `crane up as light intensifies` 让光有体积感
