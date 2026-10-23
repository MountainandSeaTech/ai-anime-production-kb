---
title: 技能魔法特效与提示词模板二十连①——总纲：特效制作全景与提示词五锁层结构
category: 提示词技巧
tags: [特效制作, 提示词模板, 总纲, 五锁层, 物理词汇, AI视频, VFX]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 技能魔法特效的两条生产线（传统VFX概念→AI直接生成）；优质提示词=镜头/光效/运镜/元素色板/主体克制五锁层+方向速度次生交互物理词汇；一条咒语一个元素一个峰值帧
related: [348, 354, 355, 356, 290, 304]
---

# 技能魔法特效与提示词模板二十连①：总纲

## 核心要点

- 特效制作有**两条生产线**：传统管线（AE/Blender/Houdini粒子合成，可控可复用）与AI生成管线（提示词直出视频，快但需模板纪律）；实战是**AI出主料+合成补交互**的混合流
- 优质魔法提示词=**五锁层**：镜头焦段、光效（咒语本身就是光源）、运镜（缓慢可控）、元素绑定色板、主体克制（一个施法者、一个元素、一个峰值帧、5-8秒）
- 特效可信度的秘密在**物理词汇四件套**：方向与扩散（expanding outward/rising）、速度变化（rapid burst then slow drift）、次生运动（embers/ripples/settling dust）、世界交互（smoke curling around objects）
- 本系列与特效十连（348-357）互补：那边讲"可信度方法论"，这边讲"怎么制作+可直接复制的提示词模板库"

## 详细内容

### 一、特效制作的三条路线对比

| 路线 | 工具 | 优点 | 缺点 | 适用 |
|---|---|---|---|---|
| 传统合成 | AE+Trapcode/Blender粒子 | 帧级可控、可复用资产 | 学习成本高、周期长 | 签名技、反复出现的招式 |
| AI直出 | Wan/H3/可灵等 | 快、质感电影级 | 不可控、跨镜漂移 | 一次性奇观、氛围性法术 |
| 混合流 | AI元素板+AE合成 | 兼得 | 需两头都会 | 严肃项目的默认路线（接356） |

### 二、五锁层结构（每条魔法提示词的骨架）

```
1. LENS 镜头：35mm / 85mm close-up / low angle wide
2. LIGHT 光效：the spell itself is the key light（咒语是唯一主光源）
   → 写清：光色、强度、照在脸上/手上的二次光、环境变暗的对比
3. CAMERA MOTION 运镜：slow push in / static locked / slight orbit
   （禁 whip pan/handheld shake——运镜越慢特效越贵气）
4. PALETTE 元素色板：一个咒语绑一套色（fire=amber+orange core+white-hot edge）
5. RESTRAINT 克制：one caster, one element, one peak frame, 5-8s
```

### 三、物理词汇四件套（特效"像真的"的关键）

写特效不是写"什么样"，是写"**怎么动**"：
- **方向/扩散**：expanding outward, spiraling upward, rolling toward camera
- **速度曲线**：rapid burst, then slow drift / accelerates on release
- **次生运动**：trailing embers, ground ripples, settling dust, heat distortion
- **世界交互**：smoke curls around the pillar, light catches floating dust, cloth whips from the shockwave

### 四、提示词六段式模板（本系列统一格式）

```
[镜头+运镜] + [施法者动作/来源] + [核心特效：元素+形态+物理运动]
+ [光效与交互光] + [环境氛围] + [风格与画质标签]
+ 负向：anime, cartoon, CGI look, game VFX, oversaturated glow
```

### 五、制作决策流程

```
这个特效全剧出现几次？
├─ 1-2次（剧情奇观）→ AI直出 + 轻微合成（394/395）
├─ 3次以上（招牌技）→ 做元素板/正典帧（374/356），批次复用
└─ 每集都用（普攻/气焰）→ 固化提示词模块+种子（396），绝不重写
```

## 关键参数 / 模板 / 清单

**通用起手模板（填空式）**
```
35mm cinematic shot, slow push in. A lone caster thrusts both hands forward.
[Element] erupts from their palms — [form/shape], [direction + speed],
[secondary motion]. The spell is the only light source: [color] glow
on their face and hands, the surroundings fall into shadow.
[Environment atmosphere]. Photorealistic, film grain, shallow depth of field.
Negative: anime, cartoon, 3D render, CGI, game FX, flat lighting, oversaturated
```

## 备注

- 海裂映射：三主角特效各绑一套五锁层（岩骨=灰褐岩纹+尘粒、弦音=金色弦波+发丝级光丝、白泽=青紫眼内异象+空气凝滞），全剧锁死不换色
- 武侠映射：降龙掌等已有276/281/290方案，本系列补"施法瞬间"的通用模板，二者按镜头类型选用
