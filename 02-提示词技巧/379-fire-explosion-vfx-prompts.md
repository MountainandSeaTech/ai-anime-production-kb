---
title: 技能魔法特效与提示词模板二十连②——火焰与爆炸：冲击波层级、热量光效与模板
category: 提示词技巧
tags: [火焰, 爆炸, fireball, 提示词模板, VFX, 热量, 冲击波, AI视频]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 火焰特效的核心不是"颜色"而是层级：核心→焰舌→余烬→热浪扭曲→地面烟尘；爆炸要写出冲击波速度曲线+次生尘雾；提供3套直接复制的英文提示词模板
related: [349, 353, 354, 355, 378, 376]
---

# 技能魔法特效与提示词模板二十连②：火焰与爆炸

## 核心要点

- 火焰可信度的来源是**层级**：白炽核心 → 橙红焰舌 → 升腾余烬 → 热浪空气扭曲 → 地面落灰，缺一层就显得像贴图
- 爆炸不是"轰"一下：要有**冲击波速度曲线**（fast spherical burst then slow billow）和**次生尘雾**（debris→smoke→settling dust）
- 火光是最好的面部主光源：用"fire illuminates the caster's face"绑定人物与特效；但AI容易过曝，需要"flicker not blowout"
- 与349（火爆特效可信度）互补：那里讲"为什么不像真火"，这里给"可直接贴的英文模板"

## 详细内容

### 一、火焰五层结构

1. **核心**：白炽白/蓝白点，密度最高（core of white-hot material）
2. **焰舌**：橙红向外翻卷，速度中等（violent orange-red flame licks）
3. **余烬**：升到空中后减速飘散（slow-rising embers）
4. **热浪**：空气扭曲置换，不写则无（heat distortion shimmer in the air）
5. **地面落尘**：火星落到地面弹起/布料被烧出飞灰（settling ash on the floor）
- AI生成最易丢3/5层：在提示词里明写 `ember trail` 和 `settling dust` 来补

### 二、爆炸四段速度曲线

| 阶段 | 时间 | 英文关键词 | 作用 |
|---|---|---|---|
| 起爆 | 0-0.5s | rapid burst, flash of white | 峰值帧 |
| 扩张 | 0.5-1.5s | expanding outward, spherical shockwave | 体量感 |
| 烟柱 | 1.5-3s | thick black smoke plume, billowing upward | 重量 |
| 沉降 | 3s+ | slow-settling dust, drifting embers | 真实尾迹 |
- 提示词中明确写出 `rapid burst then slow billow` 让AI理解速度变化

### 三、制作注意事项

- **AI直出**：适合单一火球/施法手焰；多镜复用需同seed+固定色板
- **合成路线**：AI生成火焰层（黑色背景isolate）→ AE混合模式Screen/Add → 加热浪置换 → 余烬粒子补一层（Trapcode Particular）
- **穿帮点**：火焰不照脸（光照缺失）、余煤不落地（悬浮）、冲击波把人物衣服吹反（需写 `cloth whips from shockwave`）

### 四、提示词六段式模板（专化版）

火焰填入 `[Element]`：intense fire / roaring flame / concentrated arcane fire
爆炸填入：massive explosion / controlled detonation / spherical fireball

## 关键参数 / 模板 / 清单

**模板A：施法者手焰（近景）**
```
85mm close-up, slight slow push in. A mage extends a palm upward.
Concentrated arcane fire erupts from the hand — white-hot core
surrounded by violent orange-red flame licks that spiral upward.
Slow-rising embers drift into the dark air. Heat distortion shimmers
above the flames. The fire is the only light source, casting flickering
amber on the mage's face and collar. The surroundings fall into deep
shadow. Cinematic, shallow depth of field, subtle film grain.
Negative: anime, cartoon, flat lighting, oversaturated, 3D render, CGI
```

**模板B：火球术（中景/发射）**
```
35mm medium shot, locked camera. A fireball rapidly forms between
the caster's palms — white-hot core, surrounded by roiling orange
flame licks, leaving a trail of embers and sparks. It launches forward
in a fast spherical shockwave. The air shimmers with heat distortion.
Thick black smoke billows upward behind the projectile. Ground dust
blasts away from the launch point. Cinematic motion blur on the
fireball's leading edge. Photorealistic, film grain.
Negative: anime, cartoon, static fire, symmetrical explosion, game FX
```

**模板C：爆炸冲击（广角）**
```
24mm wide angle, heavy camera shake. A massive explosion erupts
from ground level — intense flash of white at the core, followed by
a fast spherical shockwave of fire and debris expanding outward.
Thick black smoke plumes roll upward and toward camera. Flying
sparks and debris hit the lens. Slow-settling dust drifts down
afterward. Dynamic lighting from the blast flickers across nearby
surfaces. Gritty, cinematic, high contrast, shallow depth of field.
Negative: clean explosion, symmetrical, anime, cartoon, CGI render
```

**模板D：元素板专用（黑底isolate）**
```
Massive roiling fireball explosion, isolated against solid black
background, wide angle, intense flickering light with thick black
smoke plumes rising upward. Heavy ember trail. No ground, no person,
no environment. Raw VFX element, photorealistic, film grain.
Negative: anime, cartoon, background, person, environment
```

**关键负向词（火焰专用）**
```
anime, cartoon, 3D render, CGI look, flat lighting, oversaturated glow,
symmetrical explosion, static fire, clean edges, game VFX, watermarked
```

## 备注

- 海裂映射：深渊之核的静默领域=光被吃掉（反过来：这里写"光"，但海裂需要"无光"提示词；可用 `light is swallowed by darkness, embers dying mid-air` 处理失能态）；岩骨的地脉共鸣可用模板B改元素为"裂岩火星"
- 与376（召唤驯驭）交叉：驭火兽喷火=模板C+生物运动力学（260），人兽同框按345处理
