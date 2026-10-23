---
title: 裙摆与特殊结构：长/中/短裙摆 + 披风/斗篷/燕尾/长袍的独立动态公式
category: 作画与光影
tags: [布料物理, 裙摆, 披风, 特殊结构, 动画公式, AI视频]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 裙摆按长度分三级响应、披风 5-8 段骨链公式、燕尾不对称下摆、长袍下摆拖地的摩擦规则；裙摆"掀角"vs"贴腿"两态切换阈值
related: [406, 074, 427, 428, 429, 430]
---

# 裙摆与特殊结构：独立动态公式

## 核心要点

- 裙摆按长度分 3 级动态：**长摆（≥90cm）飘得远但慢、中摆（50-89cm）平衡、短摆（<50cm）摆得快但幅度小**（确定性：公认）
- 披风/斗篷的动态 = **5-8 段骨链**（Thirdrez jiggle bones 行业标准）——硬度 0.15-0.25（重披风）/ 0.4-0.5（轻披风）（确定性：经验）
- 燕尾/燕尾服下摆是**不对称结构**——短侧（前侧）几乎不动，长侧（后侧）跟披风一样飘（确定性：经验）
- 裙摆"掀角" vs "贴腿"是**风强度阈值切换**：风速 >3m/s（2级风）= 掀角；风速 <1.5m/s（1级风）= 贴腿（确定性：公认）
- 长袍拖地下摆有**摩擦阻力**——每步前进 1 步长，下摆后缘会被地面拖住 0.1 秒才跟上（确定性：经验）
- 所有特殊结构都是 427-430 的"叠加应用"——材质（427）+ 风（428）+ 动作（429）+ 宽松性（430）决定其动态，但结构本身给额外公式约束（确定性：公认）

## 详细内容

### 一、裙摆按长度分三级动态表

#### 核心逻辑

裙摆的"风响应" = 下摆面积 × 质量倒数。**越长面积越大，但质量也大**——所以中摆（及膝偏上）其实风响应最强（平衡态），长摆飘得远但整体慢，短摆摆得快但幅度有限。

| 裙摆类型 | 长度（腰围到下摆） | 材质/场景 | 风摆角（清风4级） | 滞后帧数 | 视觉效果 |
|---|---|---|---|---|---|
| **短摆（Mini）** | <40cm 大腿中部 | 运动/校园/战斗 | 40-50° | 2 帧（快摆快停） | 走路时快速前后晃动，显活泼 |
| **中摆（Midi）** | 50-89cm 膝盖上下 | 日常/职场/约会 | 50-65° | 3-4 帧（平衡） | 最显飘逸，风大时能看到腿部轮廓 |
| **长摆（Maxi）** | ≥90cm 脚踝/拖地 | 礼服/古风/婚纱 | 35-45°（因质量大） | 5-7 帧（慢摆慢停） | 飘得远但幅度不如中摆，拖地时带摩擦 |

#### 长度对 AI 提示词的影响

```
❌ 错误："Short skirt billows widely in wind"（短摆面积小，风摆有限）
✅ 正确："Mini skirt flutters rapidly back and forth with each step, fast 2-frame lag"

❌ 错误："Long silk skirt waves wildly in breeze"（长摆质量大，风摆不如中摆）
✅ 正确："Floor-length silk gown drifts slowly with the wind, 6-frame lag, hem glides just above the floor"
```

### 二、裙摆"掀角" vs "贴腿"两态

#### 物理阈值

| 风速 (m/s) | 蒲福级 | 裙摆状态 | 物理原因 | 视觉效果 |
|---|---|---|---|---|
| <1.0 | 0-1 无风/软风 | **完全贴腿** | 重力 > 风推力 | 裙摆沿着腿线，轮廓紧贴身体 |
| 1.0-2.5 | 2 轻风 | **半贴半掀** | 风推力刚刚超过重力 | 裙摆部分区域抬起 5-10°，大部分贴腿 |
| **>3.0** | 3+ 微风以上 | **掀角状态** | 风推力 > 重力 × sin(下摆面积) | 下摆明显抬起 >30°，露出腿部 |
| >8.0 | 5 劲风 | **大幅掀角** | 强风 | 裙摆被吹成水平，能看到内裤（"走光"风险） |

#### 特殊情况：跑/跳时的动态掀角

即使户外无风，相对风（跑步速度 >3m/s）也会让裙摆掀角——这就是 AI 视频中跑步女孩裙摆自动飞起来的原因（确定性：公认，428 相对风公式）。

#### 掀角 vs 贴腿 AI 提示词

```
掀角（风大/跑跳中）：
EN: Skirt hem lifts 30-45 degrees away from legs in the breeze, fabric billows outward
中: 裙摆被风吹离腿部 30-45°，面料向外膨胀

贴腿（无风/站立）：
EN: Skirt clings closely to legs, soft fabric follows body contour, no visible flutter
中: 裙摆紧贴腿部，柔软面料跟随身体轮廓，无明显飘动
```

### 三、披风/斗篷动态公式

#### 结构特征

披风（Cape）和斗篷（Cloak）是**从肩部或背部**延伸的独立织物，比躯干大 50-200%，下端完全自由。其动态类似旗帜，由 5-8 段物理骨链驱动。

#### Thirdrez Jiggle Bones 行业标准参数

| 披风类型 | 段数 | Stiffness（硬度） | Gravity Mul | Damping | 动态特征 |
|---|---|---|---|---|---|
| 重型披风（金属/厚布） | 5 段 | 0.15-0.25 | 1.0 | 0.6 | 厚重、缓慢、摆动幅度小 |
| 标准披风（风衣/斗篷） | 6 段 | 0.3-0.4 | 1.0 | 0.5 | 平衡、自然、像 Frozen 里的 |
| 轻量披风（丝绸/纱） | 7-8 段 | 0.4-0.5 | 0.8 | 0.3 | 轻盈、快摆、涟漪多 |

> 来源：Thirdrez 2026 Jiggle Bones 指南。段数越多，涟漪越丰富；Stiffness 越低越软；Damping 越低停得越慢。

#### 披风动态 = 4 个叠加因子

1. **身体方向改变**：披风滞后 4-6 帧（429 转身规则）
2. **风速**：决定披风摆角（428 蒲福级表）
3. **角色速度**：相对风叠加
4. **重力**：下端始终有向下的拉力（所以披风不会完全水平，除非暴风）

#### 披风 AI 提示词

```
重型披风（骑士/战士）：
EN: Heavy leather cape swings 30 degrees behind him as he walks, lags 5 frames after each turn, settles slowly
中: 重型皮革披风随行走后摆 30°，每次转身滞后 5 帧，缓慢落回

标准披风（英雄/法师）：
EN: Hero's standard cape billows 45 degrees with each stride, ripples cascade down the fabric, 6-frame lag when he pivots
中: 英雄的标准披风每步后摆 45°，涟漪从上往下传递，转身时滞后 6 帧

轻量披风（仙子/公主）：
EN: Silk cape flutters rapidly in gentle breeze, ripples travel down fabric faster than the hero can move her shoulders
中: 丝绸披风在微风中快速飘动，涟漪传递速度比英雄耸肩更快
```

### 四、燕尾/燕尾服（Tuxedo/Coat Tail）

#### 不对称结构特征

燕尾下摆分为两部分：
- **前侧（短）**：腰部到大腿中部，**几乎没有独立动态**（因为靠近身体，且剪裁贴合）
- **后侧（长）**：从腰部延长到小腿/脚踝，**和披风一样是独立微动体**

#### 燕尾下摆动态

```
角色静止站立时：
  - 前侧：贴身，下垂 0-5°
  - 后侧：垂落 + 轻微风摆 5-10°（像小披风）

角色行走时：
  - 前侧：随骨盆摆动，几乎同步（1 帧滞后）
  - 后侧：滞后 4-5 帧，摆幅 30-40°，涟漪从上往下传递

角色转身时：
  - 前侧：和身体同步转
  - 后侧：滞后 6-8 帧！（比披风还慢，因为更重更长）
```

#### AI 提示词

```
EN: Elegant man in tuxedo walks with short front coat tails swinging slightly with hips, long back tails billow 35 degrees 5 frames behind torso motion
中: 穿燕尾服的优雅男士行走，前短摆随髋部轻微摆动，后长摆比躯干滞后 5 帧后摆 35°
```

### 五、长袍/和服下摆拖地的摩擦规则

#### 物理公式

```
下摆前进量 = 身体前进量 - 地面摩擦延迟量
地面摩擦延迟 ≈ 0.08-0.12 秒（2.4-3.6 帧 @30fps）
```

#### 拖地下摆 3 种状态

| 状态 | 条件 | 动态描述 | 提示词 |
|---|---|---|---|
| **拖地静态** | 站立静止 | 下摆摊在地面形成 10-20cm 宽扇形 | "hem spreads flat on floor, no lift" |
| **拖地行走** | 走路 | 下摆被地面"拖住" → 每步前进后缘比身体慢 3 帧跟上，摩擦产生轻微"拖痕" | "floor-length hem drags 3 frames behind, faint trail on ground" |
| **离地飘动** | 跑步/强风 | 下摆离开地面 → 变成长摆类型（见上表），不再受摩擦 | "running fast, hem lifts 15cm off ground, billows freely with no drag" |

#### 拖地 vs 离地的风场阈值

| 风速 + 角色速度 | 下摆状态 |
|---|---|
| 风速 <2m/s + 走 <2m/s | **拖地**（摩擦 > 风推力） |
| 风速 >3m/s 或 跑 >4m/s | **离地**（风推力 + 相对风 > 摩擦 + 重力） |

### 六、特殊结构动态稳定性评级（AI 视频还原率）

| 特殊结构 | 稳定性 | 常见穿帮 | 修复关键词 |
|---|---|---|---|
| 披风 Cape | ★★★★☆ | 披风消失（太复杂） | 显式写 "cape billows behind, fabric visible" |
| 长裙摆 Maxi Skirt | ★★★★★ | 裙摆像筒一样直 | 写 "ripples and folds cascade down" |
| 燕尾 Coat Tail | ★★★☆☆ | 前后摆一样长 | 显式写 "short front tails, long back tails" |
| 拖地长袍 | ★★★★☆ | 要么一直拖地要么一直飘 | 写 "drags on ground when walking, lifts when running" |
| 和服广袖 | ★★★☆☆ | 袖子变成圆柱体 | 写 "wide kimono sleeve flutters like a flag, 3 frames behind arm" |
| 披帛/长丝带 | ★★☆☆☆ | 像绳子一样僵 | 写 "long silk ribbon flutters in gentle waves, 0.5-second lag" |

## 备注

- 披风/斗篷数据来源：Thirdrez 2026 Jiggle Bones 技术文档、Style3D 虚拟秀场实践
- 裙摆掀角/贴腿阈值来自 Bournemouth University 2024 风洞实验（布料在 <1.5 m/s 风下几乎不抬起）
- 本条目与 427-430 形成"材质→风场→动作→贴身性→特殊结构"的完整知识链
- 争议点：披风段数——不同工作室用 5-8 段都是合理范围，但 6 段是行业默认值
- 披帛/长丝带稳定性最低（★★☆☆☆），建议配合"像旗帜一样飘"（like a flag fluttering）的类比写法
