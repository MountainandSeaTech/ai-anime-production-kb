---
title: 贴身 vs 宽松：紧身衣不写布料动，宽松衣必须独立微动体
category: 作画与光影
tags: [布料物理, 贴身衣, 宽松衣, 服装设计, 提示词, AI视频]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 紧身衣是身体轮廓的第二层（零布料动态），宽松衣是独立微动体（必须写摆动）；战斗穿紧身/日常穿宽松的场景配置表
related: [406, 074, 238, 427, 428, 429, 431]
---

# 贴身 vs 宽松：紧身衣不写布料动，宽松衣必须独立微动体

## 核心要点

- **紧身衣 = 身体轮廓的第二层皮肤**：不写额外布料动态，布料动 = 身体动的结果（确定性：公认）
- **宽松衣 = 独立微动体**：必须写摆动/褶皱/滞后——遵循 427-429 的材质/风/动作拉扯参数（确定性：公认）
- 区分标准：**布料与身体之间是否有间隙**——间隙 > 5cm 属于宽松衣，需要独立动态（确定性：经验）
- AI 视频最常犯错误：紧身衣也加飘动（穿帮），宽松衣没写飘动（僵硬）——用本条目做配置清单秒解决（确定性：经验）
- 场景配置铁律：**战斗/竞技/高动作用紧身**（减少布料干扰）、**日常/仪式/氛围用宽松**（增加画面层次）（确定性：经验）
- 过渡型（半贴身/微宽松）：只写**局部布料微动**（袖口/下摆/领口），主体仍按紧身衣处理（确定性：经验）

## 详细内容

### 三大类型定义与 AI 处理规则

| 类型 | 布料-身体间隙 | 动态强度 | AI 提示词规则 | 典型服装 |
|---|---|---|---|---|
| **紧身衣（Fitted/Tight）** | 0-2cm | 零动态（布料 = 身体轮廓） | 不写任何 fabric flutter/sway；仅在关节处写微小褶皱 | 战衣、赛车服、潜水服、瑜伽裤、紧身T恤、机甲服 |
| **半贴身（Semi-fitted）** | 2-5cm | 局部微动 | 只写袖口/下摆/领口的小幅度摆动（<15°），主体忽略 | 修身衬衫、直筒牛仔裤、西装外套（不系扣） |
| **宽松衣（Loose/Oversized）** | >5cm | 独立微动体 | **必须写**摆动角度、滞后帧数、overshoot | 卫衣、长袍、和服广袖、斗篷、宽腿裤、公主裙 |

### 贴身衣（紧身衣）详细规则

#### 物理基础

紧身衣（Skin-tight garment）如运动服、机甲服、潜水服：布料被身体曲线**完全贴合**，没有"自由端"暴露在风中或拉扯中——所以布料本身**没有独立运动**。

#### 动画处理

```
❌ 错误写法："Hero in tight black suit, suit fabric flutters in wind"（紧身衣不会飘！）
❌ 错误写法："Spandex bodysuit ripples as hero moves"（除非写"随肌肉收缩的布料变化"）
✅ 正确写法："Hero in form-fitting black tactical suit, fabric stretchs slightly across shoulders when he raises arms"
✅ 正确写法："Skin-tight suit shows muscle definition through fabric, subtle creases at elbows and knees"
```

#### 紧身衣 AI 提示词模板（直接可抄）

```
EN: Form-fitting [color] tactical suit, fabric shows muscle contours underneath, slight stretch marks at shoulders and elbows, no loose fabric
中: 贴身 [颜色] 战术服，布料透出肌肉轮廓，肩肘处轻微拉伸痕迹，无松散布料
EN: Skin-tight spandex bodysuit, fabric stretches with body movement, minimal creasing only at joints
中: 贴身氨纶紧身衣，布料随身体拉伸，仅关节处有极少褶皱
```

#### 特殊例外：紧身衣也有动态的情况

| 情况 | 动态描述 |
|---|---|
| **被拉扯**（如被敌人抓住衣角） | 布料出现紧绷直线条 + 拉扯点向身体方向的应力褶皱 |
| **破裂/破损** | 破口边缘会随身体运动**轻微晃动**（小碎布条 = 宽松衣逻辑） |
| **沾水** | 布料颜色变深 + 更加贴肤（更显身体轮廓） |

---

### 宽松衣详细规则

#### 核心原则

宽松衣是**独立于身体的微动体**——有自己的重心、摆幅、滞后时间。必须在 AI 提示词里显式写出来，否则 AI 会：
- 要么给宽松衣加夸张飘动（像布料特效一样乱飞）
- 要么完全忽略（宽松衣像紧身衣一样贴死）

#### 宽松衣 AI 提示词 4 要素（按优先级）

1. **身体主运动**（告诉 AI "人在做什么"）
2. **宽松部位 + 摆幅角度**（coat hem 45° / loose sleeve 60°）
3. **滞后/overlap**（lags 2 frames / overshoots 20°）
4. **材质特定表现**（silk ripples / leather barely moves）

#### 宽松衣提示词模板

```
EN: [Character action], [garment part] billows [angle] [direction], lags [N frames] behind body, overshoots [extra angle] before settling, [material-specific]
中: [角色动作]，[服装部位] [角度] [方向] 摆动，比身体滞后 [N帧]，过甩 [额外角度] 再回落，[材质特征]
```

#### 完整示例

| 场景 | 提示词 |
|---|---|
| 武士穿宽松和服冲刺停下 | EN: Samurai sprints then halts, kimono sleeve billows 60° backward from headwind, lags 3 frames behind arm, overshoots 20° forward at stop, silk fabric ripples softly 中: 武士冲刺停下，和服袖管因顶风后摆 60°，比手臂滞后 3 帧，停下时过甩 20°，丝绸轻微涟漪 |
| 法师穿长袍施法转身 | EN: Mage rotates to face enemy, robe hem trails 25° behind her 3 frames after torso turns, cascading fabric waves settle slowly 中: 法师转向敌人，长袍下摆在躯干转向 3 帧后还拖在身后 25°，层层布料慢慢落回 |
| 日常穿 Oversized 卫衣走路 | EN: Teen walks casually, oversized hoodie hem sways 15° left-right with each step, cuffs slide down wrists as arms swing forward 中: 少年悠闲走路，Oversized 卫衣下摆随步伐左右摆 15°，袖管摆臂时滑下手腕 |

---

### 场景配置表：什么时候紧身，什么时候宽松

| 场景类型 | 推荐配置 | 理由 | 反例（为什么错） |
|---|---|---|---|
| **战斗/对决** | 紧身 | 减少布料飘动干扰动作识别，238 动作戏矩阵要求服装不挡动作线 | 穿长裙打斗：裙摆晃，看不清腿法 |
| **竞技/追逐** | 紧身 | 高速动作下宽松衣会乱飘，观众分不清是布料还是主角在动 | 穿长袍赛车：长袍被风吹成帆 |
| **机甲/高科技** | 紧身 | 暗示科技感，贴体 = 人体的延伸 | 穿宽松斗篷开机甲：风格违和 |
| **日常/校园** | 半贴身→宽松 | 增加画面层次，走路时有微动，406 场景生机 | 穿紧身衣上学：像制服/战衣 |
| **仪式/婚礼/演出** | 宽松 | 需要飘逸感+氛围感，布料微动占画面 30% | 紧身婚纱：没有裙摆飘动 |
| **古风/仙侠** | 宽松（广袖/长袍/披风） | 传统服饰特征，225 线条方向塑体积——飘动线条增加动势 | 穿紧身古风：不像古装 |
| **冬季/寒冷** | 半贴身（厚毛衣） | 太厚太宽松会笨重，半贴身保留微动 | 穿薄纱在雪地里：违和 |
| **秘密行动/潜行** | 紧身 + 全黑 | 暗示隐匿，宽松衣会反光/晃眼暴露位置 | 穿白色宽松衣潜行：目标明显 |

### AI 视频常见穿帮 & 修复

| 错误 | 出现频率 | 修复方案 |
|---|---|---|
| 紧身衣加飘动 | ★★★★☆ 极常见 | 在提示词里显式写 "no loose fabric / form-fitting / shows body contours through fabric" |
| 宽松衣像紧身衣 | ★★★☆☆ | 显式写摆动角度 + 滞后帧数 + "loose/oversized/billowy" |
| 皮革衣飘得像丝绸 | ★★★☆☆ | 写 "leather stiff, barely moves, minimal flutter even in wind" |
| 链甲像金属片飘 | ★★☆☆☆ | 写 "chainmail clinks, metal rings shift with body, no cloth-like flowing" |

## 备注

- 紧身 vs 宽松的判断边界（间隙 5cm）来自时尚工业常规（Pattern Making 标准），动画师内部共识
- 战斗场景推荐紧身与 238 动作戏视角×服装矩阵联动——紧身衣 + 低角度仰视 = 压迫感，宽松衣 + 侧面 = 飘逸感
- 431 将深入讨论**特殊结构**（裙摆/披风/燕尾），这些都是宽松衣的子类，但其动态公式与普通宽松衣不同
- 所有提示词中 "no loose fabric" / "form-fitting" 是**否定指令**——AI 模型对否定词的敏感度高于肯定词
