---
title: AI 提示词布料动态写法库——30+ 条中英对照按材质分组
category: 作画与光影
tags: [布料动态, AI提示词, 材质分组, 中英对照, 图生视频, 稳定性评级]
source: 网络学习（Hailuo AI Knowledge + Sora Motion Catalogue + OutfitVideo）
created: 2026-10-20
updated: 2026-10-20
summary: 按 7 种常见材质分组的 30+ 条 AI 视频布料动态提示词，每条附适用场景与稳定性评级，可直接复制进 Sora/MidRunway/Kling/Vidu 等模型
related: [406, 074, 438, 439, 440, 441]
---

# AI 提示词布料动态写法库

## 核心要点

- 布料动态提示词 = **材质词 + 动作动词 + 环境锚点** 三要素，缺任何一个 AI 就塌成"塑料"
- 不同材质有专属"触发动词"：silk 配 swish/rippling，denim 配 heavy creasing，硬配错动词会让 AI 困惑
- 按材质分组给提示词，能显著提升布料物理稳定性（Hailuo AI 实测：材质+动词+环境三件套比纯材质描述崩坏率降 62%）
- 每条提示词标注**稳定性评级**（★低 ★★中 ★★★高），反映当前主流 AI 视频模型（2026 Q4）对该动态的还原可靠度
- 环境锚点是隐形关键：写 "breezy veranda" 比写 "wind blowing" 更能让 AI 生成自然飘丝
- 短片段（4-6 秒）内布料稳定性远高于长片段，复杂动态建议切段生成再拼接

## 详细内容

### 写法公式

`[主体/动作] + [布料材质] + [布料动态动词] + [环境锚点]`

示例：`a samurai walking steadily → hakama of heavy cotton → hem swaying in a low arc → temple courtyard with soft wind`

### 丝绸/缎面组（Silk / Satin）

| # | 中文提示词 | 英文提示词 | 适用场景 | 稳定性 | 确定性 |
|---|---|---|---|---|---|
| 1 | 丝绸袖子在微风中像水一样流淌 | silk sleeve flowing like water in a gentle breeze | 古装/晚礼服慢镜头 | ★★★ | 公认 |
| 2 | 丝绸长裙拖在地面上泛起涟漪 | silk train rippling across the marble floor | 红毯/宫廷场景 | ★★★ | 公认 |
| 3 | 缎面裙摆随转身像花朵一样绽开 | satin skirt blooming like a flower during a pivot turn | 舞蹈/转场镜头 | ★★★ | 公认 |
| 4 | 丝绸围巾在风中打着旋儿 | silk scarf swirling in the wind | 户外特写/情绪镜 | ★★ | 经验 |
| 5 | 丝绸和服下摆轻轻划过榻榻米 | silk kimono hem brushing lightly across tatami mats | 和服室内镜 | ★★★ | 经验 |
| 6 | 绸缎面料被光一照泛起波浪般的光泽 | satin catching light in undulating waves | 布料特写/商业镜 | ★★ | 经验 |
| 7 | 丝绸披风在高速奔跑时贴紧背部然后向后甩开 | silk cloak clinging then flinging backward during a sprint | 动作戏/追逐 | ★★ | 经验 |

### 雪纺/薄纱组（Chiffon / Organza）

| # | 中文提示词 | 英文提示词 | 适用场景 | 稳定性 | 确定性 |
|---|---|---|---|---|---|
| 8 | 雪纺披肩像云一样漂浮在身后 | chiffon shawl floating like a cloud behind | 仙女/精灵角色 | ★★ | 公认 |
| 9 | 薄纱裙摆被风吹得向内凹陷又鼓起 | organza skirt billowing inward then puffing out in wind | 婚纱/夏日裙装 | ★★ | 经验 |
| 10 | 雪纺上衣被微风掀起一角露出肌肤 | chiffon blouse lifted at one corner by a breeze | 性感暗示/夏日 | ★★ | 争议 |
| 11 | 面纱随头部转动轻轻飘动 | veil drifting gently as the head turns | 宗教/婚礼场景 | ★★★ | 公认 |
| 12 | 透明薄纱披风在奔跑中像翅膀一样展开 | sheer organza cape spreading like wings while running | 奇幻/飞行 | ★ | 经验 |

### 羊毛/针织组（Wool / Knit）

| # | 中文提示词 | 英文提示词 | 适用场景 | 稳定性 | 确定性 |
|---|---|---|---|---|---|
| 13 | 厚羊毛大衣下摆沉重地摆动 | heavy wool coat hem swaying with weight | 秋冬/大衣角色 | ★★★ | 公认 |
| 14 | 针织衫袖口随手臂弯曲堆成褶皱 | knit sweater cuff bunching into folds as arm bends | 日常/慵懒场景 | ★★★ | 公认 |
| 15 | 长毛衣下摆随步伐轻轻晃动 | oversized knit hem swaying softly with each step | 时尚/街头 | ★★★ | 经验 |
| 16 | 羊毛围巾一圈圈盘绕在脖子上末端被风吹起 | wool scarf coiled at the neck with the tail lifted by wind | 冬季/户外 | ★★★ | 公认 |
| 17 | 针织连衣裙被风吹得轻微贴住身体然后弹回 | knit dress clinging slightly then bouncing back in wind | 贴身/曲线感 | ★★ | 经验 |

### 牛仔/帆布组（Denim / Canvas）

| # | 中文提示词 | 英文提示词 | 适用场景 | 稳定性 | 确定性 |
|---|---|---|---|---|---|
| 18 | 牛仔夹克下摆硬挺地摆动着没有褶皱 | denim jacket hem swinging stiffly without creasing | 街头/休闲 | ★★★ | 公认 |
| 19 | 帆布包带子随步伐上下弹跳 | canvas tote strap bouncing up and down with each step | 日常/通勤 | ★★★ | 经验 |
| 20 | 硬牛仔帽檐被风吹得轻微震动但不变形 | stiff denim hat brim vibrating slightly in wind but holding shape | 西部/农场 | ★★★ | 公认 |
| 21 | 牛仔裤膝盖处布料在行走时绷紧又放松 | denim jeans knee fabric taut then slack with each stride | 腿部特写/行走 | ★★★ | 经验 |

### 棉质组（Cotton / Linen）

| # | 中文提示词 | 英文提示词 | 适用场景 | 稳定性 | 确定性 |
|---|---|---|---|---|---|
| 22 | 亚麻衬衫在夏日微风中鼓起又塌下 | linen shirt puffing then deflating in a summer breeze | 夏日/度假 | ★★★ | 公认 |
| 23 | 棉T恤下摆随跑步卷起又落回 | cotton tee hem rolling up then falling back down during a run | 运动/日常 | ★★★ | 经验 |
| 24 | 和服腰带末端在行走中轻柔地摆动 | obi sash tail swaying gently while walking | 和服/日式 | ★★★ | 公认 |

### 披风/斗篷组（Cape / Cloak）

| # | 中文提示词 | 英文提示词 | 适用场景 | 稳定性 | 确定性 |
|---|---|---|---|---|---|
| 25 | 厚重披风在风暴中猛烈地向后扬起 | heavy cloak billowing violently backward in storm winds | 英雄/王者登场 | ★★ | 公认 |
| 26 | 披风在奔跑中像旗帜一样啪啪作响 | cape flapping like a flag while running at full speed | 高速追逐/战斗 | ★★ | 经验 |
| 27 | 站立时披风在身后缓缓展开像一朵花 | cape unfurling slowly behind like a blooming flower when standing still | 定格/蓄势待发 | ★★★ | 经验 |
| 28 | 披风在跳跃中先向上飘然后重重落下 | cape flying upward during a jump then crashing down on landing | 战斗/落地 | ★★ | 经验 |

### 战斗服/盔甲布料组（Combat Cloth / Armor Skirt）

| # | 中文提示词 | 英文提示词 | 适用场景 | 稳定性 | 确定性 |
|---|---|---|---|---|---|
| 29 | 武士袴在出刀前衣角先微微动一下 | hakama hem twitching slightly one split second before the sword draw | 战斗预判信号 | ★★ | 经验 |
| 30 | 忍者面罩布条在快速移动中向左后方拖曳 | ninja mask cloth trailing to the left rear during a dash | 忍者/隐身 | ★★ | 经验 |
| 31 | 盔甲内衬在挥剑时从缝隙中甩出 | armor under-cloth whipping out from gaps during a sword swing | 重装/战斗 | ★★ | 争议 |
| 32 | 格斗短裤腰带在踢腿时松了又系紧 | martial arts gi belt loosening then retightening during a high kick | 武术/擂台 | ★★ | 经验 |

### 通用环境锚点词库

| 环境类型 | 锚点词（写进提示词比直接说 "wind" 更有效） |
|---|---|
| 户外有风 | `on a cliff in storm winds` / `along a breezy coastal path` / `atop a grassy hill with gusts` |
| 室内微风 | `through a half-open sliding door` / `from a slowly spinning ceiling fan` / `entering from an open window` |
| 高速运动 | `created by forward momentum` / `dragging behind at speed` / `pushed by the wake of movement` |
| 静止蓄力 | `during a held breath` / `in the stillness before a strike` / `settling after sudden motion` |

### 三要素完整示例

**差**：`a woman in a silk dress walking` → 缺环境，AI 默认塑料静止
**好**：`a woman in a silk dress walking slowly → hem rippling softly → along a breezy stone path at golden hour` → 材质+动词+环境三件套

## 备注

- 本条目由 Hailuo AI Knowledge（2026 Q3）"Materiality Prompt Formula" + QubitFlow Sora Motion Catalogue + OutfitVideo 服饰 AI 实战条目整合提炼，稳定性评级基于 2026 Q4 主流 AI 视频模型（Sora 2 / Kling 3 / MidRunway 3 / Vidu 2）的综合表现
- 相关条目：438（崩坏防治——布料写对了但 AI 还是崩怎么办）、439（帧级参数表——布料动几帧才自然）、440（布料情绪信号——动的形态=情绪）、441（布料战斗节奏——布料=战斗节拍器）
- 通用环境生机见 406（场景生机法则）；服装张力信号见 074；动作戏视角×服装矩阵见 238；线条方向塑体积见 225
