---
title: 技能魔法特效与提示词模板二十连⑲——提示词模板工程：模块化结构、变量槽、负向词库与种子管理
category: 提示词技巧
tags: [提示词工程, 模板模块化, 变量槽, 负向词库, 种子管理, prompt engineering, 模板继承, VFX, AI视频]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 提示词模板必须工程化：拆为六模块（镜头/角色/特效/环境/风格/负向）自由组合；变量槽用[大写占位符]标记，5秒替换；负向词库按14类分类整理，调用时只取相关类；种子管理=同一特效固定seed保一致性；提供模块化骨架与变量字典
related: [378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395]
---

# 技能魔法特效与提示词模板二十连⑲：提示词模板工程

## 核心要点

- **提示词必须工程化**：将每条魔法提示词拆为六模块（LENS镜头 + CASTER角色 + FX核心特效 + LIGHT光效交互 + ENV环境 + STYLE风格画质 + NEG负向），模块之间用换行分隔，可自由组合复用
- **变量槽用[大写占位符]**：如`[ELEMENT]`、`[COLOR_CORE]`、`[CAMERA_ANGLE]`，替换只需5秒——不要每次重写整段提示词
- **负向词库按14类分类**：通用类（anime/cartoon/3D render）+ 元素类（火/水/雷/冰/风/岩/光/暗/治疗/空间/时间/护盾/变身/剑气），调用时只取相关类，避免堆砌
- **种子管理=一致性保险**：同一角色/同一法术的同一状态固定seed，确保跨镜头时脸部/特效颜色/粒子样式一致；不同状态用不同seed
- **模板继承**：基础模板（Base）+ 增量修改（Delta）= 变体模板——不要复制粘贴整段修改一个词

## 详细内容

### 一、六模块骨架（通用填空式）

```
[LENS]
[shot type], [camera angle], [camera movement].

[CASTER]
[A caster archetype] [action/stance].

[FX - CORE]
[Element] [erupts/flows/streams] from [source] — [form/shape],
[direction + speed], [secondary motion].

[FX - LIGHT]
The spell is the only light source: [color] glow on [face/hands],
the surroundings fall into [shadow level]. [Lens flare / Bloom].

[ENV]
[Environment description], [atmospheric conditions].

[STYLE]
[Photorealistic style tags], [film grain], [depth of field],
[lens type], [color grade].

[NEG]
[Negative words by category].
```

### 二、变量槽字典（可替换值清单）

| 变量名 | 可选值 | 默认值 |
|---|---|---|
| `[SHOT_TYPE]` | 24mm wide / 35mm medium / 85mm close-up | 35mm medium |
| `[CAMERA_ANGLE]` | low angle / eye level / high angle / Dutch angle | low angle |
| `[CAMERA_MOVEMENT]` | locked / slow push in / slight orbit / tracking | slow push in |
| `[CASTER_ARCHETYPE]` | warrior / mage / rogue / druid / paladin | warrior |
| `[ACTION_STANCE]` | thrusts both hands forward / kneels / raises weapon | thrusts hands |
| `[ELEMENT]` | fire / water / lightning / ice / wind / rock / light / shadow | fire |
| `[COLOR_CORE]` | amber / cyan / violet / white / black / green | amber |
| `[COLOR_AURA]` | pale gold / electric blue / sickly green / soft silver | pale gold |
| `[FORM_SHAPE]` | swirling vortex / concentrated beam / expanding sphere / jagged tear | swirling vortex |
| `[DIRECTION_SPEED]` | expanding outward rapidly / streaming upward / spiraling inward | expanding outward |
| `[SECONDARY_MOTION]` | trailing embers / ground ripples / settling dust / heat distortion | trailing embers |
| `[ENVIRONMENT]` | ruined temple / stormy battlefield / sunlit forest / dark catacomb | ruined temple |
| `[ATMOSPHERE]` | ominous / desperate / serene / chaotic / sacred | ominous |
| `[STYLE_TAG]` | photorealistic cinematic / dark fantasy / hyper-realistic | photorealistic cinematic |
| `[LENS_TYPE]` | 35mm film / anamorphic lens / 85mm portrait | 35mm film |

### 三、负向词库（14类分类表）

```
[通用类 - 所有特效必加]
anime, cartoon, 3D render, CGI look, game FX, flat lighting,
oversaturated, 2D, illustration, painting

[火系专用]
no smoke, no embers, clean fire, uniform flame, no heat distortion,
no sparks, cartoon fire

[水系专用]
glowing water, no reflection, no ripples, flat surface,
no depth, uniform blue, cartoon water

[雷电专用]
constant glow, no flicker, straight line, no branching,
no core halo, no wet reflection, cartoon lightning

[冰系专用]
glowing ice, no frost, no breath vapor, no cracks, smooth surface,
no refraction, cartoon ice

[风系专用]
no particles, no motion blur, static smoke, uniform fog,
no direction, cartoon wind

[岩系专用]
smooth plastic, floating rocks, instant appearance, no cracks,
no dust, no weight, cartoon rock

[光系专用]
no particles, constant glow, soft edges, no shadow contrast,
lens flare on everything, cartoon light

[暗系专用]
flat smoke, pure black, no texture, uniform fog, clean edges,
bright environment, cartoon dark

[治疗专用]
aggressive energy, harsh lighting, violent burst, dark shadows,
destructive, game FX, oversaturated green

[空间专用]
flat circle, no depth, no far side, uniform swirl, no spatial
distortion, clean edges, 2D

[时间专用]
slow motion, motion blur, people still moving, blinking,
no change at end, no particle detail

[护盾专用]
flat glass, no reaction to impact, no runes, no glow,
clean surface, game FX, 2D

[变身专用]
instant transformation, no process, no anchor, clean clothing,
flat lighting, game FX, 2D

[剑气专用]
pure bright core, no particles, no lingering trail, warm colors
(for dark slash), no motion blur, game FX
```

### 四、种子管理规则

```
RULE 1 - 角色种子：
  → 同一角色半身主图 = Seed A（固定）
  → 同一角色全身版 = Seed B（固定，独立）
  → 同一角色三视图 = Seed C（固定，独立）
  → 同一角色表情组 = Seed D（固定，独立）

RULE 2 - 特效种子：
  → 同一法术同一状态 = Seed E（固定）
  → 法术升级/变体 = Seed E+1（基于E微调）
  → 不同角色同类型法术 = 不同种子（避免串色）

RULE 3 - 环境种子：
  → 同一场景不同镜头 = Seed F（固定）
  → 场景时间变化（日/夜）= Seed F+1

RULE 4 - 记录：
  → 所有种子记录在资产表（seed log）
  → 格式：角色/特效/场景 → Seed编号 → 用途
```

### 五、模板继承系统

```
BASE TEMPLATE（基础模板）
  ↓ 继承 + Delta
VARIANT A（变体A：改变元素类型）
  → 只改[ELEMENT]和[COLOR_*]变量
VARIANT B（变体B：改变镜头角度）
  → 只改[SHOT_TYPE]和[CAMERA_ANGLE]变量
VARIANT C（变体C：改变环境）
  → 只改[ENVIRONMENT]和[ATMOSPHERE]变量

EXAMPLE:
Base: 火焰爆炸中景（379模板A）
  → Delta: [ELEMENT]=lightning, [COLOR_CORE]=electric cyan
  → Result: 雷电中景（380模板A）
  → Delta: [SHOT_TYPE]=85mm close-up
  → Result: 雷电近景
```

### 六、常见翻车与修复

| 翻车 | 原因 | 修复 |
|---|---|---|
| 模板越写越长 | 模块边界不清 | 严格六模块骨架，每模块≤3行 |
| 变量替换出错 | 变量名不统一 | 全用大写+下划线，建立字典 |
| 负向词堆砌 | 不加分类全部复制 | 只取相关类，≤10个负向词 |
| 跨镜不一致 | 没固定seed | 建立seed log，同特效同seed |
| 模板太多难找 | 无编号/无分类 | 按378-397编号+分类归档 |

## 关键参数 / 模板 / 清单

**模块化快速构建示例**
```
[LENS]
35mm medium shot, low angle, slow push in.

[CASTER]
A battle-hardened warrior thrusts both hands forward,
channeling immense energy.

[FX]
Raw [ELEMENT] energy erupts from their palms —
[FORM_SHAPE], [DIRECTION_SPEED], [SECONDARY_MOTION].

[LIGHT]
The spell is the only light source: [COLOR_CORE] glow
on their face and hands, the surroundings fall into shadow.

[ENV]
[ENVIRONMENT], [ATMOSPHERE] atmosphere.

[STYLE]
Photorealistic cinematic, film grain, shallow depth of field,
35mm aesthetic.

[NEG]
[通用类] + [[ELEMENT]系专用]
```

**模板工程检查清单**
```
□ 六模块骨架已建立
□ 变量槽字典已建立（≥20个变量）
□ 负向词库已分类（14类）
□ Seed log已建立
□ 模板继承关系已记录
□ 版本号已标注（v1.0 / v1.1）
□ 模板已编号归档（378-397）
□ 测试运行：变量替换后AI输出质量合格
```

## 备注

- 海裂映射：三主角特效模板工程——岩骨基础模板（灰褐/岩/尘）→ Delta1（地脉共鸣升级）→ Delta2（石化代价显现）；弦音基础模板（金色/弦波/发丝光）→ Delta1（声波共振升级）→ Delta2（失声代价显现）；白泽基础模板（青紫/深渊/凝滞）→ Delta1（共感深化）→ Delta2（神经污染显现）
- 与378总纲联动：378讲"五锁层"是提示词的内容纪律，396讲"六模块"是提示词的结构纪律——内容+结构=可复用模板
- 与374视觉开发管线联动：374的"正典三帧"=模板工程的视觉锚点；396的"seed管理"=模板工程的数据锚点
- 与377全剧能力圣经联动：能力圣经定义"什么能力存在"，模板工程定义"怎么生成这些能力的视觉"——二者咬合
- 工具建议：Markdown文件 + 简单的文本替换脚本（Python/Shell）即可实现模板继承和变量替换——无需专用软件
- 维护规则：每新增一个特效类型（如新增"毒系"），同步更新负向词库+变量字典+种子log
