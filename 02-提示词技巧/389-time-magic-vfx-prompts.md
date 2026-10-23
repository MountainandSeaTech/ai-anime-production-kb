---
title: 技能魔法特效与提示词模板二十连⑫——时间魔法：六种类型、冻结语法与回溯三步骤
category: 提示词技巧
tags: [时间魔法, 时间冻结, 慢动作, 时间回溯, time stop, slow motion, rewind, 提示词模板, VFX, AI视频]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 时间特效第一死因是"写成慢动作"——冻结必须写`all motion completely frozen including eyes hair clothing`；时间回溯必须按三步骤写（什么逆转→回到哪里→什么改变）；六种时间类型各有独立视觉语法；提供3套模板
related: [378, 388, 380, 385, 375]
---

# 技能魔法特效与提示词模板二十连⑫：时间魔法

## 核心要点

- **时间冻结第一死因：AI把"冻结"理解成"慢动作"**——必须明确写 `time stops instantly`, `all motion becomes completely frozen including eyes, facial expressions, hair, clothing and body position`，否则角色还在眨眼呼吸
- **时间回溯三步骤**：什么在逆转（what reverses）→ 回到哪里（where it returns）→ 什么发生了改变（what changes）——缺一步回溯就没有叙事
- **六种时间特效类型**：局部膨胀（慢动作泡）、时空裂缝、时间回溯、时间卡顿/循环、加速衰老、预知 glimpse——不同类型视觉语法完全不同，不能混用
- **时间特效的视觉代理**：不写"时间"本身，写时间对**物质**的影响——`raindrops frozen as perfect spheres`, `debris pulled backward into the rift`, `ghost after-images trailing the subject`
- **时间卡顿≠循环**：卡顿是"同一帧重复"（glitching stutter），循环是"动作重复播放"（looping motion）——写法不同

## 详细内容

### 一、六种时间特效类型与视觉语法

| 类型 | 核心视觉 | 关键提示词 | 适用场景 |
|---|---|---|---|
| **局部膨胀** Localized Dilation | 泡状区域内一切变慢 | `shimmering refractive sphere of warped air`, `raindrops elongate into streaks inside the bubble` | 躲避/精密操作 |
| **时空裂缝** Chronal Rift | 现实撕裂+物质被吸入 | `sharp crystalline fractures in reality`, `debris pulled into the rift` | 危险/入侵 |
| **时间回溯** Temporal Rewind | 物质逆向重组 | `objects reassembling in reverse`, `chronon particles flowing backwards` | 修复/改写 |
| **时间卡顿** Time Stutter | 同一帧重复+数字故障 | `glitching digital artifacts`, `semi-transparent after-images` | 失控/干扰 |
| **加速衰老** Accelerated Decay | 物质快速风化 | `pavement cracking and aging rapidly`, `metal rusting in seconds` | 诅咒/毁灭 |
| **预知 glimpse** Precognitive | 未来影像叠加 | `faint future-images overlaid`, `ghostly preview of imminent impact` | 预警/闪避 |

### 二、时间冻结的精确语法

**必须同时写**：
1. **全局冻结**：`time stops instantly`, `all motion freezes completely`
2. **细节冻结**：`including eyes, facial expressions, hair, clothing, body position`——AI常漏这些
3. **环境冻结**：`raindrops hang suspended as perfect spheres`, `sparks frozen in mid-air`, `dust motes stopped`
4. **施法者例外**（如需要）：`only the caster moves freely through the frozen world`

**常见翻车**：
- 冻结后人物头发还在飘 → 没写`hair frozen`
- 冻结像慢动作 → 没写`stops instantly`
- 环境还在动 → 没写环境元素冻结

### 三、时间回溯三步骤模板

```
STEP 1 - 什么在逆转：
  → shattered glass fragments flying back together
  → a wound reopening in reverse (blood flowing back into the body)
  → debris returning to its original position
STEP 2 - 回到哪里：
  → glass reassembles into a complete window
  → the wound closes to unbroken skin
  → the battlefield returns to its pre-explosion state
STEP 3 - 什么改变（关键——回溯不是简单倒放）：
  → but this time the caster's hand is in a different position
  → but a golden sigil now glows on the reformed surface
  → but the enemy's expression shows they remember what happened
```

### 四、时间特效的视觉代理（写物质不写时间）

AI无法理解"时间"这个抽象概念，必须写时间对物质的具体影响：

- **冻结代理**：`raindrops as perfect spheres`, `sparks hanging motionless`, `dust frozen in sunbeams`
- **回溯代理**：`chronon particles flowing backwards`, ` shattered fragments reassembling`
- **膨胀代理**：`raindrops elongating into streaks`, `falling feathers drifting impossibly slow`
- **裂缝代理**：`crystalline fractures in reality`, `light bending around jagged edges`

### 五、常见翻车与修复

| 翻车 | 原因 | 修复 |
|---|---|---|
| 冻结像慢动作 | 没写stops instantly | 补`time stops instantly`, `all motion completely frozen` |
| 冻结后人物还在动 | 没写细节冻结 | 补`eyes, hair, clothing frozen` |
| 回溯像倒放视频 | 没写第三步改变 | 补`but this time...` |
| 时间特效看不见 | 没写物质代理 | 补`raindrops frozen`, `debris reassembling` |
| 像数字故障滤镜 | 没写物理边界 | 补`refractive sphere`, `crystalline fractures` |

## 关键参数 / 模板 / 清单

**模板A：时间冻结（中景/战斗瞬间）**
```
35mm medium shot, Dutch angle. A crowded battlefield at the peak
of chaos — explosions, flying debris, sparks, smoke, soldiers
mid-leap. Time stops instantly. All motion becomes completely
frozen: soldiers hang in mid-air with weapons raised, mouths
open in silent screams, eyes fixed. Individual raindrops hang
suspended as perfect spheres, some elongated into streaks by
their last momentum. Sparks frozen in mid-air like a constellation
of orange stars. Smoke plumes solidify into sculptural clouds.
Only the caster moves freely through the frozen world, walking
slowly between the suspended chaos. Their cloak drifts gently
(only moving thing). The frozen scene is lit by the warm glow
of halted explosions, casting impossible static shadows. Cinematic,
photorealistic, shallow depth of field, film grain.
Negative: anime, cartoon, slow motion, motion blur, people still
moving, blinking, hair moving, fluid smoke, game FX
```

**模板B：时间回溯（广角/修复/改写）**
```
24mm wide angle, locked camera. A ruined cathedral interior after
a devastating explosion — shattered stained glass, collapsed
pillars, dust everywhere. The caster extends both hands and
golden chronon particles begin flowing backwards through the air,
like luminous dust reversing its path. Shattered glass fragments
lift from the floor and fly back together, reassembling into
complete windows shard by shard. Collapsed stone blocks rise
and slot back into pillars. Dust is sucked back into solid walls.
The destruction rewinds in accelerated reverse — 5 seconds of
destruction undone in 2 seconds. At the climax, the cathedral
stands fully restored. But this time, a glowing golden sigil
now burns on the restored floor where there was none before —
the caster has changed the outcome. Cinematic, awe-inspiring,
photorealistic, volumetric lighting, film grain.
Negative: anime, cartoon, simple reverse playback, no change at
end, no particle detail, flat lighting, instant restoration,
game FX
```

**模板C：时间卡顿/残影（近景/失控/干扰）**
```
85mm close-up, slight handheld shake. A cybernetic warrior is
caught in a temporal stutter. The space around them fractures
into transparent ghost-like frames of their recent movement.
Three faint semi-transparent after-images are visible — one
a step behind, one at current position, one a step ahead —
creating a visual echo of their motion. The effect has sharp
geometric edges like broken glass suspended in air. Glitching
digital artifacts flicker at the edges of the temporal fractures.
Tiny shimmering cyan data-motes drift erratically within the
affected zone. The warrior's face shows disorientation, their
eyes shifting between the ghost frames. Background neon lights
split and glitch as they pass through the anomaly. Cinematic,
gritty, photorealistic, film grain, shallow depth of field.
Negative: anime, cartoon, smooth motion, no after-images, no
glitch artifacts, clean edges, flat lighting, game FX
```

**关键负向词（时间系专用）**
```
anime, cartoon, slow motion, motion blur, people still moving,
blinking, hair moving, fluid smoke, simple reverse playback,
no change at end, no particle detail, flat lighting, instant
restoration, clean edges, game FX, 3D render, no physical
manifestation
```

## 备注

- 海裂映射：白泽的"深渊共感"时间感知变体——不操控时间但"看见"时间的物质痕迹（加速衰老模板用于感知巨兽经过后的地质年代变化）；弦音的声波共振可制造局部时间膨胀泡（慢动作泡=声速区域内的相对时间差）
- 与388传送门联动：时间裂缝=传送门+时间维度，写`the portal's event horizon is not spatial but temporal — years compressed into seconds visible in the throat`
- 与380雷电联动：时间卡顿+闪电=冻结的闪电分支，`lightning frozen mid-strike, its branches suspended like a fractal sculpture`
- 与375现代异能联动：现代时间系异能=数字故障+物理扭曲的混合，参考模板C的glitch artifacts写法
- 声画对位：时间冻结的"寂静"是最大音效——冻结瞬间所有声音戛然而止，只剩低频嗡鸣；回溯时用反向音效（reverse reverb）强化"倒放"感
- 帧率提示：写慢动作时明确给帧率 `120fps slow motion` / `240fps high frame rate` ——AI对帧率词汇有latent理解
