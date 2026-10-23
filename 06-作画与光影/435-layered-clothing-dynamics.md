---
title: 层次叠穿布料动态
category: 作画与光影
tags: [布料物理, 叠穿, 层次动态, 阻尼梯度, 内外层独立运动, 提示词]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 内衫/外袍/披风三层各自独立的动态规律，内层动小外层动大的阻尼梯度机制，叠穿时外层遮内层的节奏。
related: [432, 433, 434, 436, 406, 074, 238, 225]
---

# 层次叠穿布料动态

## 核心要点

1. **阻尼梯度模型（公认）**：叠穿的核心物理机制是"约束阻尼梯度"——从内到外，身体约束递减、空气阻力递增 → 运动自由度递增。这不是简单的"三层同时动"，而是每层有独立的频率、周期和滞后相位。
2. **内层动小外层动大（公认）**：内层紧贴身体，受身体摩擦约束 + 外层空气遮挡，摆幅约为外层的 20-40%，频率与身体运动基本同步（滞后 < 0.1s）；外层摆幅是内层的 2-5 倍，滞后约 0.3-0.6s；披风作为"第三层"摆幅最大，滞后 0.8-1.2s。
3. **外层遮内层（经验）**：正常站立或慢走时，外层下摆覆盖内层 1-2cm（内衬通常设计短于外壳）；身体大幅度弯曲或快速转向时，外层上甩露出内层 3-5cm，形成"色彩闪现"节奏（如红色内衬从黑色外袍下摆闪现）。
4. **层间摩擦（公认）**：相邻层之间的摩擦力取决于材质组合——丝/丝摩擦系数低（0.15，层间容易滑动），棉/棉摩擦系数高（0.55，层间几乎不滑动）。摩擦系数直接影响层间相对运动幅度。
5. **D-LAYERS 数据集结论（公认）**：多层布料动画研究（arXiv 2305.10418，UC Berkeley）表明内层质量通常更大（厚实贴身），外层质量更小（轻薄飘逸），这种质量差加剧了"内稳外飘"的视觉效果。
6. **Maya/Blender 模拟经验（经验）**：工业级布料模拟需内层设高阻尼（0.5-0.8）、外层设低阻尼（0.05-0.2），且内层作为外层的碰撞体。忽略层间摩擦的模拟会导致穿模和运动不自然。
7. **仪式袍服的"防漂移"结构（经验）**：正式礼服常在内层与外层之间设 2-3 组暗扣（thread chains 或 lingerie guards），限制层间相对滑动在可控范围内（< 3cm），这也影响动画时层间位移的上限。

## 详细内容

### 三层叠穿——典型参数对比表

| 参数 | 内层（贴身衫/衬裙） | 中层（外袍/马甲） | 外层（披风/斗篷） | 确定性 |
|------|-------------------|-----------------|-----------------|--------|
| 质量 g/m² | 200-300（厚实） | 150-200 | 80-150（轻薄） | 公认 |
| 摆幅（相对身体） | 5-10cm | 15-30cm | 30-60cm | 公认 |
| 滞后身体相位 | < 0.1s | 0.3-0.6s | 0.8-1.2s | 公认 |
| 阻尼系数（模拟） | 0.5-0.8 | 0.2-0.4 | 0.05-0.2 | 公认 |
| 层间摩擦约束 | 极强（贴身） | 中 | 弱（独立） | 公认 |
| 空气阻力系数 | 低（被遮挡） | 中 | 高（全暴露） | 公认 |
| 弯曲刚度 | 高（不易弯折） | 中 | 低（易弯折） | 公认 |

### 层间摩擦系数表

| 材质组合 | 摩擦系数 μ | 层间相对滑动 | 动画表现 |
|---------|-----------|------------|---------|
| 丝 × 丝 | 0.15-0.25 | 大（易滑动） | 内层几乎不动、外层独立飘 |
| 棉 × 棉 | 0.5-0.65 | 小（黏在一起） | 内外层摆幅接近、相位差小 |
| 丝 × 棉 | 0.3-0.45 | 中 | 内层小幅度、外层比内层多 1.5× |
| 皮革 × 布料 | 0.4-0.55 | 中偏小 | 皮革层带动布料层 |

### 叠穿动画的"闪现节奏"（24fps）

以角色快速向右转身为例：

| 帧 | 身体角度 | 内层下摆 | 中层下摆 | 披风 | 内层露出 |
|----|---------|---------|---------|------|---------|
| 0 | 0° 静止 | 自然下垂 | 自然下垂 | 自然下垂 | 无 |
| 6 | 向右转 45° | 身体同步偏转，摆幅小 | 滞后 15°，摆幅中 | 还在原位！ | 下摆露出 1cm |
| 12 | 向右转 90° | 跟随身体到 90° | 到 60° | 到 20° | 露出 3cm（红色内衬闪现） |
| 18 | 向右转 135° | 身体到 135° | 到 110° | 到 60° | 露出 2cm |
| 24 | 稳定在 90° 新位置 | 稳定跟随 | 摆动衰减中 | 继续摆到 110° 然后回来 | 无 |

**关键**：披风在第 12 帧才刚到 20°，而身体已经到 90°——这个 70° 的相位差是叠穿动画"呼吸感"的核心。

### AI 视频提示词（中英对照）

#### 场景：古风长袍叠穿（三层）

```
[中文提示词]
武侠角色穿三层古风长袍：内层是深红色厚棉衫（贴身，随身体运动几乎无滞后，摆幅仅 5-8 厘米），中层是白色亚麻外袍（滞后身体半秒，摆幅 20-25 厘米，在转弯时下摆被内层顶着略向外鼓出），外层是淡青色丝绸披风（滞后身体约一秒，摆幅 40-50 厘米，完全独立地随风摆动）。角色快速转身时，红色内层衬里从白色外袍下摆下方闪现一瞬间，然后收回。背景是竹林，风从左向右吹。电影画面，三层布料各有独立的动态。

[English Prompt]
Wuxia character in three-layered traditional robe: inner layer deep red thick cotton shirt (body-hugging, almost no lag with body, swing only 5-8cm), middle layer white linen robe (lags body by half a second, swing 20-25cm, slightly bulges outward at hem when turning, pushed by inner layer), outer layer pale cyan silk cape (lags body by about one second, swing 40-50cm, flutters completely independently in wind). When character turns fast, red inner lining flashes briefly from under white robe hem, then retracts. Bamboo grove background, wind blowing left to right. Cinematic shot, three cloth layers each with independent dynamics.
```

#### 场景：西式宫廷礼服叠穿

```
[中文提示词]
贵族女性穿维多利亚时代礼服：内层是白色蕾丝衬裙（紧贴身体，轻微摆动），中层是紫红色缎面紧身胸衣和拖地长裙（裙摆 3 米长，缓慢沉重摆动，层间因摩擦几乎不与内层滑动），外层是黑色蕾丝披肩（轻薄，独立飘动，搭在手臂上时随手臂晃动，但大部分时候自由飘浮在空中）。当她行屈膝礼时，三层裙摆依次落下：内层先落、中层紧接着、披肩最后才慢慢垂下。灯光是烛光，背景是大理石宴会厅。

[English Prompt]
Noblewoman in Victorian era gown: inner layer white lace petticoat (body-hugging, subtle swing), middle layer purple satin corset and floor-length gown (3-meter train, slow heavy swing, barely slides against inner layer due to friction), outer layer black lace shawl (lightweight, independent fluttering, dangles when on arm but mostly floats freely in air). When she curtsies, three layers fall in sequence: inner first, middle immediately after, shawl last slowly drops. Candlelight, marble ballroom background.
```

## 备注

- 关联 [434-金属甲与硬质结构]：铠甲本身是"刚性外壳 + 内衬 + 可能的披风"三层——内衬是内层（贴身棉甲），铠甲是中层（刚性），披风是外层（完全独立）。
- 关联 [432-沾水与潮湿]：湿布阻尼增大 → 层间相对滑动减小 → 三层摆幅趋近，像黏在一起。
- 物理来源：UC Berkeley D-LAYERS 数据集（arXiv 2305.10418）、布料模拟摩擦参数（Measurement of Viscosity Damping Parameters of Fabric, Charfi 2006）。
- 争议点：层间摩擦系数的精确值不同实验给出的范围较宽，动画中以材质类型定性区分即可。
