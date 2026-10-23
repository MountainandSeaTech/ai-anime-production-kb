---
title: 技能魔法特效与提示词模板二十连⑨——暗影/黑雾/诅咒：吸收光、触须活体感与腐败分层
category: 提示词技巧
tags: [暗影, 黑雾, 诅咒, shadow, dark magic, curse, 烟雾, 触须, 提示词模板, VFX, AI视频]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 暗影特效第一死因是"像黑色烟雾贴图"——必须写核心色（深紫靛而非纯黑）+内部纹理+行为动词（clinging/writhing/solidifying）；黑雾要分层（核心色/纹理/行为/内光/内部元素）；触须必须像活物（liquid smoke/resisting/writhing）；提供3套模板
related: [378, 385, 348, 349, 370, 368]
---

# 技能魔法特效与提示词模板二十连⑨：暗影/黑雾/诅咒

## 核心要点

- **暗影特效第一死因：纯黑+无纹理 = 像烟雾贴图**——必须写核心色为深紫/靛蓝（`deep royal purple, abyssal indigo, black-violet ink`），而非纯黑；并加accent色（`sickly chartreuse, blood-red, spectral white`）形成内部纹理
- **黑雾五层结构**：核心色（深紫靛）→ 纹理（dense smoke / inky liquid / spectral mist）→ 行为（clinging / writhing / solidifying）→ 内光（sinister glow / pulsating heartbeat）→ 内部元素（runes / sigils / spectral faces）——少一层就平
- **触须必须像活物**：`slowly spiraling around his legs like living smoke`, `writhing and resisting as she seizes it`, `climbing his body`——黑雾的核心魅力是"它有意志"
- **暗影与圣光物理对立**：光向外辐射（radiating outward），暗影向内吞噬（absorbing surrounding light）；光照亮环境，暗影让周围变暗（`the world becomes darker`）
- **贴地感是暗影的重量**：`clinging to the ground like heavy poison`——黑雾比空气重，沿地面流动，不是均匀飘在空中

## 详细内容

### 一、暗影≠纯黑：核心色板与accent色

| 核心色（Core） | 语义 | accent色（Veins） | 语义 |
|---|---|---|---|
| deep royal purple | 皇室腐败 | electric cyan | 奥术污染 |
| corrupting magenta | 肉体变异 | sickly chartreuse | 剧毒/疾病 |
| abyssal indigo | 深海恐惧 | blood-red | 嗜血/诅咒 |
| black-violet ink | 墨染深渊 | spectral white | 亡魂/灵界 |

纯黑=无信息=死。深紫靛+accent静脉=活。

### 二、黑雾五层结构（缺一不可）

```
LAYER 1 - 核心色：deep [purple/indigo/ink], shot through with veins of [accent]
LAYER 2 - 纹理：dense billowing smoke / inky liquid suspended in air
                    / ethereal wisps and tendrils / churning spectral mist
LAYER 3 - 行为：clinging to ground like heavy poison / writhing / solidifying
                into crystalline shards / crackling with chaotic lightning
LAYER 4 - 内光：glows with sinister internal light / pulsates with heartbeat
                / absorbs surrounding light / casts volumetric shadows
LAYER 5 - 内部元素：glowing fractured arcane runes / spectral screaming faces
                    / floating sigils / chains of pure shadow
```

### 三、触须/阴影活物化四步法

暗影与光效最大不同：光效可以"发射"，暗影必须"生长"和"纠缠"。

1. **起源**：`his shadow begins moving independently` / `stretching unnaturally across the ground`
2. **涌现**：`black tendrils emerge from the darkness` / `slowly spiraling around his legs and armor`
3. **攀附**：`the shadow climbs his body` / `black energy spreads across his skin`
4. **实体化**：`forming intricate dark patterns that pulse with ancient power` / `solidifying into crystalline shards`

触须运动必须用**抗拒感动词**：`writhing, resisting, twisting, churning`——活着的东西不会服从指令。

### 四、暗影环境互动（制造恐怖或威慑）

- **吞噬光**：`absorbs surrounding light leaving only its own glow` / `candles extinguish as the fog approaches`
- **腐蚀物质**：`rain vaporizing as it hits the energy` / `stone cracks and darkens where the shadow touches`
- **扭曲影子**：`shadows twisting into unnatural shapes` / `the ground seems to shift under the darkness`
- **零重力场**：`floating debris caught in a zero-gravity magical field`

### 五、常见翻车与修复

| 翻车 | 原因 | 修复 |
|---|---|---|
| 像黑色烟雾贴图 | 纯黑+无纹理 | 补深紫核心色+accent静脉+内光 |
| 看不清施法者 | 黑雾浓度无梯度 | 补 `thick in foreground, thinner near caster's face` |
| 没有活物感 | 缺少抗拒动词 | 补 `writhing, resisting, churning, clinging` |
| 与背景糊在一起 | 无内光/无对比 | 补 `casts volumetric shadows`, `absorbs light` |
| 像卡通黑暗 | 太均匀太干净 | 补 `dense, billowing`, `floating debris`, `rain vaporizing` |

## 关键参数 / 模板 / 清单

**模板A：黑雾召唤（广角/威慑）**
```
24mm wide angle, dramatic low angle. A shadowy archmage stands at the
center of a crumbling gothic cathedral. From their outstretched palms,
a thick roiling miasma of dark magic energy fog erupts and expands.
The fog's core is deep royal purple, shot through with veins of
sickly chartreuse. The texture is like dense billowing smoke mixed
with inky liquid suspended in air. It clings to the ground like
heavy poison, writhing and forming spectral screaming faces within
its mass. The entire fog glows with a sinister internal light that
absorbs surrounding light, leaving the edges of the frame in near
total darkness. Floating fractured arcane runes and chains of pure
shadow drift within the fog. Rain lashes down and vaporizes as it
hits the energy. Candles extinguish one by one. Cinematic, ominous,
chiaroscuro contrast, film grain.
Negative: anime, cartoon, flat smoke, pure black, no texture,
uniform fog, clean edges, bright environment, 2D, oversaturated
```

**模板B：暗影触须缠绕（中景/变身/侵蚀）**
```
35mm medium shot, camera pushes closer. A warrior stands frozen.
Their shadow begins moving independently across the stone floor,
stretching unnaturally. Then black tendrils emerge from the darkness,
slowly spiraling around their legs and armor like living smoke.
The tendrils have a sinuous serpentine quality, writhing and
resisting as they climb the body. The shadow spreads across the
warrior's skin, forming intricate dark patterns that pulse with
ancient power. The tendrils' core is black-violet ink with faint
blood-red veins. Where they touch the armor, frost forms and the
metal darkens. The surrounding world becomes darker with every
second. Chiaroscuro lighting, deep shadows, only the tendrils' faint
glow and the warrior's eyes provide light. Cinematic, photorealistic,
film grain.
Negative: anime, cartoon, smooth tendrils, instant transformation,
no movement, bright environment, flat shadows, clean surface
```

**模板C：诅咒印记爆发（近景/技能释放）**
```
85mm close-up, slight slow motion. A witch extends a palm forward.
From her hand erupts a concentrated burst of corrupting dark energy:
a churning vortex of spectral mist centered on deep magenta core
with veins of spectral white. The mist behaves like inky liquid
suspended in air, swirling and crackling with chaotic miniature
lightning. Within the vortex, barely-visible spectral faces scream
and dissolve. Floating sigils burn in the air around the spell.
The spell absorbs surrounding light: the background falls into deep
shadow while the curse itself is the only illumination. The witch's
face is lit from below by the sinister glow, casting upward shadows.
Dust motes caught in the magical field float in zero gravity.
Cinematic, harsh lighting, film grain.
Negative: anime, cartoon, constant glow, no internal detail,
flat black, uniform purple, no sigils, bright background, smooth
surfaces, 3D render
```

**关键负向词（暗影系专用）**
```
anime, cartoon, flat smoke, pure black, no texture, uniform fog,
clean edges, bright environment, 2D, oversaturated, smooth tendrils,
instant transformation, no movement, flat shadows, glowing neon
(unless specified), 3D render, CGI look
```

## 备注

- 海裂映射：深渊之核巨兽的"静默领域"直接用暗影模板A变体——去掉sigils/runes，改为深海生物发光质感（bioluminescent indigo core + dark abyssal tendrils），保留"吸收声音与光线"的物理描述
- 与385圣光联动：光vs暗对打时，提示词必须**交替写两者的物理交互**——`the beam of holy light pushes back the darkness, steam rising where they meet` / `the shadow tendrils wrap around the light and extinguish it segment by segment`
- 与349火焰联动：暗影+火=地狱系，提示词写 `black smoke shot through with veins of burning orange, embers glowing within the darkness`
- 与370升级觉醒联动：暗影变身=从"自我意志"到"被侵蚀"的弧光，提示词按触须四步法写（起源→涌现→攀附→实体化），每一阶段对应角色一个情绪转折点
- 画幅建议：暗影系多用低角度+荷兰角（Dutch angle）强化不安；choker close-up（卡脖子特写）强化窒息感
