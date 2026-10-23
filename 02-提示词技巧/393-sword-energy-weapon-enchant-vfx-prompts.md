---
title: 技能魔法特效与提示词模板二十连⑯——剑气/武器附魔：五层结构、核心暗边缘亮与残留轨迹
category: 提示词技巧
tags: [剑气, 武器附魔, sword slash, weapon enchant, blade aura, energy slash, 提示词模板, VFX, AI视频]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 剑气第一死因是"纯亮核心"——核心暗+边缘亮=高级质感（如obsidian black core+white-silver edge）；剑气必须写五层（形状/能量色/粒子/质感/动态）；残留轨迹是灵魂（lingering trail after the slash）；武器附魔=武器表面持续发光的状态；提供3套模板
related: [378, 385, 380, 386, 276, 281]
---

# 技能魔法特效与提示词模板二十连⑯：剑气/武器附魔

## 核心要点

- **剑气第一死因：纯亮核心**——只写"bright slash"得到的是廉价光效；高级剑气=**核心暗+边缘亮**（如obsidian black core + white-silver edge），核心有"吸收光"的质感
- **剑气五层结构**：形状（jagged tear vs clean arc）→ 核心能量色（三层：core/transition/edge）→ 次级粒子（embers/smoke/wisps）→ 质感材质（crystal/liquid/gas）→ 运动动态（initial speed + lingering after-effect）——不写残留=没有重量
- **武器附魔≠剑气**：附魔是武器**表面持续发光**（`blade coated in flame`, `sword wrapped in lightning`），剑气是**挥砍轨迹**（`slash leaving energy trail`）——不要混写
- **剑气是光源**：slash itself is the primary light source，照亮人物脸部和周围环境——但核心暗的剑气会"吞噬"周围光，边缘亮则"照亮"
- **残留轨迹是剑气的灵魂**：`the central tear hangs in the air before slowly sealing`, `lingering scar of energy slowly fades over several seconds`——不写残留AI只画一帧

## 详细内容

### 一、剑气五层结构

```
LAYER 1 - 形状（Form）：
  → violent jagged reality tear / clean graceful arc / sweeping diagonal fissure
  → 形状即风格：jagged=混沌/邪恶，clean=神圣/精准，sweeping=宏大/史诗
LAYER 2 - 核心能量色（Color Palette）：
  → 三层：core（核心）→ transition（过渡）→ edge（边缘）
  → 例：obsidian black core → necrotic green veins → cold white-silver edge
  → 例：blinding solar white core → molten celestial gold → warm sunrise orange
LAYER 3 - 次级粒子（Secondary Effects）：
  → 碎片：sharp flakes breaking off and dissolving into ash
  → 烟雾：oily black smoke with green undertone
  → 光屑：golden embers floating like snowflakes
  → 羽毛：trailing edge dissolves into angelic feather wisps
LAYER 4 - 质感材质（Texture）：
  → sharp freshly broken obsidian / liquid gold / gaseous incandescent cloud
  → 质感=可触摸性，决定"这是真实的"还是"这是特效"
LAYER 5 - 运动动态（Motion）：
  → initial movement: incredibly fast, almost instantaneous
  → after-effect: lingers, hangs in air, slowly seals/fades
```

### 二、核心暗 vs 纯亮：质感分水岭

| 类型 | 核心 | 过渡 | 边缘 | 质感 |
|---|---|---|---|---|
| **暗核型**（高级） | obsidian black / void | necrotic green veins | cold white-silver | 吸收+释放双重光源 |
| **亮核型**（神圣） | blinding white | molten gold | warm orange | 纯释放光源 |
| **单色型**（廉价） | bright blue | brighter blue | white | 单一释放光源 |

暗核型的秘密：`the obsidian black core acts as negative light, absorbing ambient light`——剑气同时发光和吸光，形成高对比。

### 三、武器附魔三状态

| 状态 | 描述 | 关键提示词 |
|---|---|---|
| **蓄力** | 能量聚集于武器 | `energy arcs swirl around the blade, building intensity`, `bright flash ignites at sword hilt` |
| **附魔** | 武器持续发光 | `blade coated in flame`, `sword wrapped in crackling lightning`, `edge dripping with molten energy` |
| **挥砍** | 剑气释放 | `slash leaving energy trail`, `trajectory leaves flowing light afterimages` |

### 四、剑气与材质交互

- **斩切硬物**：`slash cuts through stone, leaving black crystalline cracks`
- **净化邪恶**：`demonic entities seared by holy fire, turning to white ash`
- **空间撕裂**：`energy tearing through the fabric of space, dimensional distortion`
- **冻结轨迹**：`slash leaves a frozen ice trail in the air, frost spreading from impact`

### 五、常见翻车与修复

| 翻车 | 原因 | 修复 |
|---|---|---|
| 像光剑 | 纯亮核心无层次 | 补暗核+过渡+边缘三层 |
| 无残留 | 没写after-effect | 补`lingering trail`, `slowly fades` |
| 像2D特效 | 无粒子无质感 | 补碎片/烟雾/光屑+材质描述 |
| 武器不发光 | 附魔剑气混写 | 分开写`blade coated in`和`slash leaving` |
| 无空间感 | 无光照交互 | 补`slash is primary light source`, `shadows` |

## 关键参数 / 模板 / 清单

**模板A：暗核剑气（近景/追踪/死亡系）**
```
85mm extreme close-up, tracking shot following the leading edge
of the slash. An ultra-high-speed dynamic capture of a single
devastatingly powerful horizontal slash. The primary focus is
entirely on the Weapon FX.

FORM: The slash is a violent jagged reality tear — a line of
shattered obsidian momentarily fused by pure necrotic energy.
The leading edge is razor-thin and intensely bright. The main
body has fluctuating unstable width, with sharp crystalline
fragments breaking off its edges. Slightly curved horizontal
fissure in space.

COLOR: Core is deep light-absorbing obsidian black with a
polished reflective quality like volcanic glass. Pulsing through
this core are intricate vein-like tendrils of sickening ethereal
necrotic green. The very edge has a thin sharp corona of cold
white-silver light. Avoid warm colors entirely.

SECONDARY: Small sharp flakes of obsidian-black energy break
off and drift, slowly dissolving into fine black ash. Wisps
of oily black smoke with faint green undertone trail behind.
Fractal energy bursts flare along the length. Air around the
slash warps and distorts as if through intense heat haze.

TEXTURE: Sharp freshly broken obsidian + gaseous corrosive
energy + ethereal soul-like gas. Fusion of solid crystal,
liquid void, and gas.

MOTION: Initial movement incredibly fast, almost instantaneous.
After-effect lingers — the tear hangs in air before slowly
sealing. Smoke and particles drift in subtle slow motion.

Lighting: Slash itself is primary light source. Necrotic green
veins cast sickly glow. Obsidian core absorbs ambient light.
Cinematic, photorealistic, shallow depth of field, film grain.
Negative: anime, cartoon, clean arc, pure bright core, no
particles, no lingering trail, warm colors, flat lighting
```

**模板B：神圣剑气（中景/慢动作/净化系）**
```
35mm medium shot, high-speed slow-motion capture. A Seraphim
warrior's greatsword completes a powerful downward diagonal
cleave. Focus entirely on the Weapon FX — the trail of solar
fire left by the blade's arc.

FORM: The slash is a perfect clean graceful arc of brilliant
energy. Smooth and fluid like a ribbon of liquid sunlight.
Leading edge blindingly sharp, trailing edge softer, breaking
apart into ethereal feathers of light.

COLOR: Core is blinding solar white with lens flare effect,
transitioning outward into vibrant molten celestial gold.
Outermost edges are soft warm sunrise orange. Entirely warm,
pure, overwhelming palette.

SECONDARY: A shower of soft glowing golden embers thrown from
the arc — they don't burn out but float gently like snowflakes
before fading into light. Billows of pure white sanctified steam
rise from the slash. Trailing edge dissolves into small wisps
resembling angelic feathers, ascending upward. Air shimmers and
warps from intense holy heat.

TEXTURE: Controlled solar flare — core is pure plasma, outer
layers have texture of liquid gold and gaseous incandescent
cloud. Intensely hot but pure and cleansing.

MOTION: Powerful yet elegant. Slow-motion allows appreciation
of fluid dynamics. Embers and feathered wisps float with gentle
anti-gravity quality, contrasting the fierce initial speed.

Aftermath: Purification and consecration. Demonic entities
seared by holy fire, turning to white ash. Arc leaves a
lingering brand of golden light in the air, slowly brightens
before fading peacefully.

Lighting: Overwhelming light source casting strong warm light
and sharp defined shadows. Cinematic, ethereal, photorealistic,
film grain, volumetric lighting.
Negative: anime, cartoon, dark colors, jagged edges, no embers,
no lingering trail, destructive aftermath, flat lighting
```

**模板C：武器附魔+蓄力斩（中景/战斗/东方）**
```
35mm medium shot, low angle. A lone swordsman draws their blade
from its scabbard. The torso twists — left shoulder drops forward,
right shoulder pulls back, weight loading into the rear hip.
Magenta energy arcs swirl around the torso and blade, building
intensity. A bright flash ignites at the sword hilt.

The blade itself is now coated in a thin layer of crackling
electric magenta energy, the edge sharper than physical steel.
Energy drips from the blade like liquid lightning, pooling and
evaporating on the ground. The sword is the primary light source,
casting sharp magenta shadows.

The body uncoils — explosive rush directly toward the camera
with heavy motion blur and diagonal speed streaks. The face
fills the frame for one instant, eyes locked forward. Then the
drawn blade sweeps past in a magenta flash, leaving a clean
graceful arc of energy suspended in the air.

The arc is a ribbon of liquid lightning: core is deep violet,
transitioning to electric magenta, edge a thin white-hot line.
Small sparks break off and drift. The arc hangs in the air for
a full second before slowly dissipating into particles. Where
the slash passed, a faint scar of ionized air remains.

Cinematic, photorealistic, film grain, shallow depth of field,
motion blur on the rush.
Negative: anime, cartoon, no energy coating, no flash at hilt,
no lingering arc, pure bright core, no motion blur, game FX
```

**关键负向词（剑气/附魔专用）**
```
anime, cartoon, clean arc (when wanting jagged), pure bright
core, no particles, no lingering trail, warm colors (for dark
slash), no motion blur, game FX, 2D, no lighting interaction,
flat lighting, no texture, 3D render
```

## 备注

- 海裂映射：岩骨的"地脉共鸣"武器附魔=`blade coated in gray-brown stone energy with grinding dust`; 弦音的"声弦"剑气=`slash leaving golden string-like afterimages that vibrate`; 白泽的"深渊共感"=`blade dripping with bioluminescent indigo ichor`
- 与276降龙掌联动：降龙掌=手掌版"剑气"，同样适用五层结构，但形状改为`dragon-shaped energy coil`而非slash arc
- 与281无形气刃联动：无形气刃=不可见的剑气，必须给环境显影（`air displaced in visible shockwave`, `grass bends in the slash's path`）
- 与183武器持久性联动：剑气生成时武器必须在画面中锚定（`sword visible in frame`），否则AI容易丢失武器连续性
- 与370升级觉醒联动：武器附魔是觉醒的"简化版"，用同样三层色板但量级缩小（从全身气场缩小到武器表面）
- 运镜建议：剑气最适合追踪镜头（tracking shot following the slash）和慢动作（slow-motion）；附魔最适合低角度+推近（low angle + push in）强调武器压迫感
- 声画对位：蓄力=低频嗡鸣渐强；闪光=瞬态高频（transient spike）；挥砍=撕裂声（tear）；残留=余韵衰减（reverb decay）
