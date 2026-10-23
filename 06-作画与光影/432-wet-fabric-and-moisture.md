---
title: 沾水与潮湿布料物理
category: 作画与光影
tags: [布料物理, 湿衣, 动画参考, 水-布交互, 提示词工程]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 湿衣贴体、重心下坠、水痕分布与干燥过程的视觉与物理规律，以及湿布与风交互的摆幅差异。
related: [433, 434, 435, 436, 406, 074, 238, 225]
---

# 沾水与潮湿布料物理

## 核心要点

1. **增重与下垂（公认）**：棉麻吸水量可达自重的 200-300%，干重 100g 的棉 T 恤湿透后重约 250-350g。重力下垂力显著超过干布，衣角/下摆/袖口会出现额外的下坠褶皱。
2. **贴体与透明（公认）**：水填充纤维间隙后，布料折射率趋近皮肤（空气 n≈1.0，纤维 n≈1.5，水 n≈1.33，皮肤 n≈1.4），透光率从干布的 5-15% 提升至 30-60%（薄棉），紧身部位清晰透肤。
3. **颜色变深（公认）**：湿润状态下纤维-水界面减少了漫反射，同一块布湿后明度下降约 2-3 个色阶，饱和度略升（染料在水中扩散更均匀）。
4. **水痕与积水（经验）**：水沿纤维束（经/纬向）比斜向更容易渗透；重力导致水在领口、肩线、膝盖窝等低洼处汇聚成半透明水袋状凸起，边缘有水滴悬挂。
5. **干燥过程（公认）**：蒸发优先发生在布料边缘（表面积大、空气流通好）→ 中心区域后干；边缘颜色先变浅回到原色，形成从外向内的"干燥边缘"推进线。
6. **湿-风交互（公认）**：湿布密度高，风载引起的摆幅更小（约干布的 40-60%），摆动周期更长（约干布的 1.5-2 倍），频率更低；高频抖动消失，代之以沉重的低频摆动。
7. **不同材料差异（公认）**：棉麻吸水性 > 丝绸 > 合成纤维（涤纶仅吸自重 0.4%），因此棉麻湿态变化最剧烈；防水涂层或油性处理的布料沾水后呈水珠滚落而非渗透。

## 详细内容

### 材质吸水量对比表

| 材质 | 吸水能力 | 湿透后增重 | 透明化程度 | 干燥速度 | 确定性 |
|------|---------|-----------|-----------|---------|--------|
| 棉 Cotton | 极高（自重 200-300%） | 约 2.5× | ★★★★☆ | 中等慢 | 公认 |
| 亚麻 Linen | 高（自重 200%） | 约 2.0× | ★★★★★（薄） | 快于棉 | 公认 |
| 羊毛 Wool | 中（自重 150-180%） | 约 1.5× | ★★☆☆☆ | 极慢 | 公认 |
| 丝绸 Silk | 低（自重 100-120%） | 约 1.2× | ★★★★☆ | 快 | 公认 |
| 涤纶 Polyester | 极低（自重 0.4%） | 几乎不变 | ★☆☆☆☆ | 极快 | 公认 |
| 防水涂层布 | 近乎 0 | 几乎不变 | ☆☆☆☆☆ | 即时滚落 | 公认 |

### 湿布摆动参数（动画参考）

基于布料模拟文献（Forced-Driven Wet Cloth Simulation）和 Style3D 布料引擎参数：

- 干布密度 0.002 g/cm³ → 湿布有效密度 0.006-0.012 g/cm³（棉麻）
- 风载有效力 F_wind = 0.5 × ρ_air × v² × C_d × A，其中 C_d 阻力系数湿态略高（表面张力使布料更"展开"迎风）
- 摆动周期 T ∝ √(m/k)，质量 m 增大 → T 变长
- **视觉提示**：动画中湿布摆一次，干布要摆 1.5-2 次；湿布没有干布那种"啪"的高频抖动

### 干燥过程的四阶段帧级描写

| 阶段 | 含水率 | 视觉表现 | 时间参考（室内 20°C） |
|------|--------|---------|----------------------|
| 刚湿透 | 100% | 全片深色、完全贴体、边缘挂水珠 | t=0 |
| 边缘蒸发 | 70% | 边缘 1-2cm 浅化、边缘微抖但仍贴体 | t≈10-15 分钟 |
| 中心干燥 | 40% | 中心出现不规则浅色块、整体不再贴体 | t≈30-45 分钟 |
| 半潮状态 | 20% | 仅褶皱深处仍深、手感微潮、摆幅恢复 70% | t≈60-90 分钟 |

### AI 视频提示词（中英对照）

#### 场景：雨中角色，棉衬衫湿透

```
[中文提示词]
角色穿白色棉衬衫，暴雨中全身湿透。衬衫因吸水变重向下垂坠，衣角明显拉长；胸口和肩线紧贴皮肤，隐约透出肤色；领口和膝盖窝处有水袋状隆起，边缘悬挂着即将滴落的水珠。布料颜色比干时深两档，呈半透明感。风很大但衬衫摆幅很小、摆动缓慢沉重，没有干布的高频抖动。背景有雨水打在地面的涟漪。风格：写实动画，电影级光影。

[English Prompt]
Character in white cotton shirt, fully soaked in heavy rain. The shirt hangs heavily downward with elongated hem; chest and shoulder line cling tightly to body, skin tone subtly visible through wet fabric. Water-pouch bulges at neckline and knee creases, droplets hanging at edges about to fall. Fabric color 2 shades darker than dry state, semi-translucent. Strong wind but shirt flutters with small amplitude and slow heavy period, no high-frequency jitter of dry cloth. Rain ripples on ground. Style: photoreal animation, cinematic lighting.
```

#### 场景：干燥推进中的湿袍（边缘先干）

```
[中文提示词]
角色穿深蓝色亚麻长袍，正在快速干燥中。长袍下摆边缘已变浅回到原深蓝，但中心区域仍有不规则的湿深色斑块，像从外向内推进的干燥边界线。整体已经脱离贴体状态，但下摆因残留水分还略有下坠。微微飘动，摆幅比干布略小。背景是晴朗的晴天，阳光强烈。

[English Prompt]
Character in dark blue linen robe, drying rapidly. Robe hem edges have lightened back to original dark blue, but center area still has irregular wet dark patches forming a drying boundary line advancing inward. Overall no longer clinging to body, but hem still slightly drooping from residual moisture. Gentle fluttering with slightly smaller amplitude than dry cloth. Bright sunny day, strong sunlight background.
```

#### 提示词稳定性技巧

| 技巧 | 说明 | 确定性 |
|------|------|--------|
| 指定材质 | 写清楚 `cotton shirt` / `silk scarf` / `polyester jacket`，不同材质湿态差异极大 | 经验 |
| 量化深色程度 | `2 shades darker` 比 `darker` 更稳定 | 经验 |
| 周期对比提示 | `flutters once while dry cloth flutters twice` 给 AI 时间参照 | 经验 |
| 规避矛盾词 | 不要同时写 `soaked` 和 `flutters wildly`（湿布摆幅应小） | 公认 |

## 备注

- 关联 [406-场景生机法则]：湿布动态是环境"生机"的一类——水-布-风三者的耦合比单独任何一种都更有叙事张力。
- 关联 [074-服装/道具张力信号]：湿布贴体暴露身形常作为"脆弱"或"受伤后"的视觉信号，下垂作为"无力"信号。
- 物理来源：布料模拟领域的 mass-spring 模型（Matt Fisher, Stanford）和顶点粘附力模型（Wet Cloth Animation with Vertex Based Adhesion Force, Semantic Scholar 2021）。
- 争议点：湿布摆幅与干布摆幅的精确比例不同文献给出 0.3-0.7 范围，动画创作中取中间值 0.5 即可。
