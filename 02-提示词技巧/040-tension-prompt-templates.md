---
title: 张力构建提示词模板汇总
category: 提示词技巧
tags: [张力, 提示词, 模板, 汇总, 综合]
source: 原创
created: 2026-10-13
updated: 2026-10-13
summary: 汇总前29条张力技法的可复用提示词模块，按蓄势/峰值/释放三段拼接即用
related: [011, 014, 016, 018, 024, 025]
---

# 张力构建提示词模板汇总

## 核心要点
- 本条是 30 条张力课的**提示词版毕业汇总**——把前 29 条技法浓缩成可拼接的 prompt 模块
- 按 014 张力曲线三段组织：**蓄势模块 / 峰值模块 / 释放模块**
- 用法：从三段各选 1-2 个模块+场景主体+风格词，拼接成完整 prompt
- AI 视频生成张力镜优先：static 机位 + 大特写 + 短时长 + 单一动作

## 通用结构模板
```
[景别+角度] [主体+姿势/动作] [张力信号] [镜头运动] [景深/构图] [风格/速度]
```
例：`extreme close-up, hand on sword hilt, knuckles white, static, shallow depth of field, anime style, tense`

## 蓄势模块（Build-up）

### 待机姿势（025）
- `iaido stance, hand on sword hilt, blade sheathed, side-on, low center of gravity, tense`
- `combat ready stance, side profile, hand near weapon, coiled tension`
- `crouched ready pose, hand on ground, about to dash, spring coiled`

### 微表情信号（024）
- `extreme close-up of eyes, pupils contracting, breath held, intense stare`
- `close-up, lips pressed tight, suppressed emotion, micro tension`
- `macro shot, eyes narrowing, locking gaze`

### 手部前摇（026/030）
- `extreme close-up, hand slowly moving to sword hilt, gradual grip`
- `macro close-up, white knuckles gripping hilt, intense grip`
- `close-up, trembling hand, suppressed emotion`

### 凝视对峙（027）
- `two characters facing each other, intense gaze, eye contact, close-up, static`
- `character gazing intently, eyes locked, unblinking stare`

### 逼近步法（028）
- `character stepping forward, closing distance, slow approach, combat footwork`
- `gliding step, low stance advance, coiled tension`

### 构图加压（020）
- `negative space, character in lower corner, vast empty space, minimalist`
- `symmetrical composition, centered, bilateral symmetry, ritualistic`
- `character pushed to frame edge, small in corner, oppressive`

## 峰值模块（Peak）

### 出刀/爆发（升格）（021）
- `2x slow motion, sword draw slash mid-action, extreme close-up, static camera`
- `slow motion, strike impact moment, 4x, freeze mid-action`
- `fast slash, motion blur, extreme close-up, energy burst`

### 闪白瞬爆（036）
- `light burst, white flash, energy explosion, lens flare, overexposed instant`
- `freeze frame, flash white, peak impact moment`

### 多角度爆发
- `same strike from multiple angles, rapid cuts, impact montage`
- `slash close-up, impact close-up, reaction close-up, rapid`

## 释放模块（Release）

### 收刀定格（029）
- `full body, sheathing sword, back turned, slow pull back, still final pose`
- `holding final pose, motionless, wide shot, aftermath`

### 拉远揭示（018/020）
- `slow dolly out, pull back to reveal, wide shot, isolation`
- `slow pull back, character small in vast environment, negative space`

### 余韵静默（033）
- `static, motionless, silence, held breath, aftermath, still frame`
- `freeze frame, quiet, empty, lingering tension`

## 完整拼接示例

### 居合斩杀（全流程）
```
[蓄势] extreme close-up, hand on sword hilt, knuckles white, breath held, static, shallow depth of field, anime style, tense
[峰值] 2x slow motion, sword draw slash, extreme close-up, static camera, energy burst, flash white
[释放] full body, sheathing sword, back turned, slow pull back, still final pose, negative space
```

### 对峙对白
```
[蓄势] two characters facing, intense gaze, eye contact, close-up, static, eye level, tense
[峰值] extreme close-up, eyes narrowing, realization, slow push in, determined
[释放] wide shot, slow pull back, both characters, final standoff pose, still
```

### 追逐逃亡
```
[蓄势] character running, back view, tracking shot, full body, frantic / pursuer closing in, tracking, deep focus
[峰值] close-up, runner looking back, terrified, static, freeze
[释放] wide shot, final moment, slow pull back, static final pose
```

## 通用风格/修饰词库

### 张力修饰
`tense, coiled, ready to strike, low center of gravity, muscles tensed, suppressed, intense, gripping, breath held`

### 速度
`slow motion, 2x, 4x, freeze frame, still, static, sudden, fast`

### 景别
`extreme close-up, macro, close-up, medium close-up, full body, wide shot`

### 角度
`eye level, low angle, high angle, dutch angle, top-down`

### 景深/构图
`shallow depth of field, strong bokeh, deep focus, negative space, symmetrical, asymmetric`

## 提示词避坑速查
- 镜头运动越复杂越崩→张力段优先 static
- 手部/多角色易崩→大特写+短镜+多备选
- 升格帧率不稳→升格段时长略短
- 视线方向不稳→大特写+明确方向词+多生成选最佳
- 复杂动作跳过前摇→前摇镜单独生成（带 about to/winding up）

## 自检：prompt 是否服务张力
- [ ] 蓄势段有没有微表情/手部/凝视信号词？
- [ ] 峰值段有没有升格/flash/static 机位？
- [ ] 释放段有没有定格/拉远/负空间？
- [ ] 镜头运动是不是优先 static？
- [ ] 景别是不是从紧到松有变化？

## 备注
- 本条是 30 条张力课的总出口——把理论变成可直接喂给 AI 的 prompt
- 用法：按场景选三段模块拼接，每镜一个 prompt，逐镜生成再剪辑
- 动漫短剧张力镜的 AI 生成黄金组合：static + 大特写 + 单一动作 + 浅景深 + 短时长
- 30 条课到此完结，检索界面可按"张力"标签筛选全部 30 条
