---
title: 动作拉扯：跑步/挥刀/摔倒/转身的衣料惯性与滞后动画
category: 作画与光影
tags: [布料物理, 动作拉扯, 惯性, 帧延迟, 提示词, AI视频, WAN3]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 跑步衣摆后甩、挥刀袖管随臂、摔倒先绷后坠、转身衣角滞后 2-3 帧——4 类常见动作的布料惯性公式与提示词
related: [406, 074, 238, 427, 428, 430, 431]
---

# 动作拉扯：跑步/挥刀/摔倒/转身的衣料惯性

## 核心要点

- 动作拉扯 = 角色**直接施加给布料的力**（奔跑拉扯、挥臂甩动）+ **相对风的叠加**（428）——两者同时作用，不可分割（确定性：公认）
- 跑步衣摆后摆角度 ≈ 跑步速度 × 空气阻力系数：慢跑 30°、冲刺 45-60°；停下时衣摆会**过度前甩**（overshoot）再回弹（确定性：经验）
- 挥刀/挥拳时**袖管/袖口是独立微动体**，比手臂慢 2-3 帧（@24fps）= 3-4 帧（@30fps）到达最大摆幅，然后继续摆 3-5 帧才停下（确定性：公认）
- 摔倒的布料两阶段：**先紧绷**（身体突然加速下坠，布料被拉长贴体）→ **再坠荡**（布料在空中自由下落摆动，滞后身体 0.2 秒）（确定性：经验）
- 转身/急停时**衣角滞后 2-3 帧**（@24fps，轻薄材质）= 3-4 帧（@30fps），厚重材质 4-5 帧（@24fps）= 5-6 帧（@30fps）；AI 视频里不写"lag"几乎一定会出现"身体停了衣角还在飞"的穿帮（确定性：经验）
- 所有拉扯动画遵循迪士尼 12 原则中的 **Follow-Through & Overlapping Action**——没有一停全停的布料（确定性：公认）

## 详细内容

### 1. 跑步：衣摆后甩 + 裤腿/袖口同步拉扯

#### 核心公式

```
衣摆后摆角度 ≈ 跑步速度(m/s) × 空气阻力系数(0.08) × 100
```

| 跑步状态 | 速度 m/s | 相对风 | 衣摆后摆角 | 袖口摆角 | 裤腿摆角 |
|---|---|---|---|---|---|
| 慢走 | 1.0 | 微风 | 10° | 15°（随臂） | 5° |
| 快走 | 2.0 | 轻风 | 20° | 25° | 10° |
| 慢跑 | 3.0 | 微风 | 30° | 35° | 15° |
| 跑步 | 5.0 | 清风 | 45° | 50° | 25° |
| 冲刺 | 7.0 | 劲风 | 60°+ 抽打腿部 | 65°+ 绕臂 | 35°+ 抽打 |
| 停下瞬间 | 0 | 突然消失 | 先 **过度前甩 15-20°**（惯性）→ 再回弹回垂落 | 同上 | 同上 |

#### 停下瞬间的 Overshoot 关键帧

**@24fps 基准（30fps 按 ×1.25 换算）**：

1. **帧 N**（身体开始减速）：衣摆还在 45° 后摆
2. **帧 N+1 ~ N+3**（身体完全停下）：衣摆因惯性**继续向前甩到 15° 前摆**（overshoot）
3. **帧 N+4 ~ N+7**：衣摆回弹到垂直 ±5°，小幅振荡
4. **帧 N+8**：完全垂落静止

**@30fps 换算**：
1. 帧 N：同上
2. 帧 N+1 ~ N+4：overshoot
3. 帧 N+5 ~ N+9：回弹振荡
4. 帧 N+10：完全静止

#### AI 提示词

```
EN: Character sprinting fast, coat hem billows 60 degrees backward from headwind, sleeves snap with each arm swing, the fabric overshoots forward when she skids to a stop then settles
中: 角色高速冲刺，外套下摆因顶风后摆 60°，袖管随每次摆臂甩出，她紧急停下时衣摆过度前甩再落回
EN: Slow jogging, loose shirt hem sways 20 degrees back and forth in sync with leg movement, slight overshoot at each footfall
中: 慢跑中，宽松T恤下摆随步伐前后摆动 20°，每步落地时轻微过度
```

> 确定性：公认（运动物理 + 迪士尼动画标准案例）。停下时的 overshoot 是 12 原则中 Follow-Through 的教科书案例。

---

### 2. 挥刀/挥拳/挥臂：袖管独立微动体

#### 核心模型

挥臂动作中布料分 3 层（自由度递减）：
1. **肩线**：几乎不滞后（和身体同步）
2. **上臂袖管**：滞后 1 帧，摆幅中等
3. **袖口**：滞后 **2-3 帧**，摆幅最大，到达最大摆幅后还会继续摆 3-5 帧

#### 挥剑 3 阶段布料表现

| 挥剑阶段 | 时间 | 手臂角度 | 袖口摆角 | 关键动画 |
|---|---|---|---|---|
| 蓄力（后摆） | 0-200ms | -30° → -90° | 滞后 2 帧（@24fps）= 3 帧（@30fps）到 -60° | 袖口还在原位，手臂已经后摆 |
| 挥击（前劈） | 200-400ms | -90° → +120° | 滞后 3 帧（@24fps）= 4 帧（@30fps）到 +90° → +135°（overshoot） | 袖口甩过手臂位置 |
| 收势 | 400-600ms | +120° → 0° | 滞后 2 帧（@24fps）= 3 帧（@30fps）回到 45° → 小幅振荡 → 停下 | 袖口还在甩，剑已归鞘 |

#### AI 提示词

```
EN: Swordsman swings blade overhead, his robe lags 2 frames behind arm motion, sleeve overshoots the arm angle by 15 degrees before snapping back, fabric flutters for 5 frames after the strike lands
中: 剑士当头挥剑，他的袍子比手臂动作滞后 2 帧，袖口摆角超过手臂 15° 再弹回，击中后布料还飘 5 帧
EN: Martial artist punches forward with 2 frames of sleeve lag, fist stops but cuff continues forward briefly
中: 武师出拳，袖口滞后 2 帧，拳头停了袖口还前探一小段
```

> 确定性：公认。来源：RebusFarm Follow-Through 指南、《Frozen》Elsa 披风参考。游戏动画袖口滞后通常为 1-2 帧（更干净），电影动画 2-3 帧（更自然）。

---

### 3. 摔倒：先绷后坠两阶段

#### 物理本质

身体从静止→突然加速下坠（重力），布料因惯性**保持原位**→被身体"扯紧"→贴体。然后布料也开始下落，但空气阻力让它比身体慢**0.1-0.2 秒**到达地面，着地后还会弹一下。

#### 摔倒 4 阶段布料关键帧

| 阶段 | 身体状态 | 布料状态 | 帧数 @30fps |
|---|---|---|---|
| **① 突然下坠** | 身体加速向下 | 布料保持原位→被拉成紧绷直线，完全贴体 | 1-3 帧 |
| **② 自由下落** | 身体继续加速 | 布料开始下落，但比身体慢 0.1-0.2 秒，在身后"拖尾" | 4-10 帧 |
| **③ 触地** | 身体砸在地上，停止 | 布料还在空中→过度向下甩触地→弹一下 | 11-13 帧 |
| **④ 坠荡停止** | 静止躺在地上 | 布料摊开在地面，还有 1-2 次小幅振荡 | 14-20 帧 |

#### AI 提示词

```
EN: Character trips and falls forward, shirt stretches tight against torso at the sudden downward motion, then fabric billows behind her as she tumbles, coat hem lands 0.2 seconds after her body and bounces once
中: 角色绊倒向前摔，T恤在突然下坠时被拉紧贴身，然后翻滚中布料在身后飘，外套下摆比身体晚 0.2 秒触地还弹一下
EN: Hero crashes through a window, his cape stretches flat against him mid-fall, then flutters wildly before he lands hard
中: 英雄撞破窗户坠落，披风贴紧身体，落地前疯狂飘动
```

> 确定性：经验。行业普遍共识是"先绷后坠"，但精确帧数以布料材质为变量。427 的材质参数表可查。

---

### 4. 转身/急停：衣角滞后 2-3 帧

#### 物理本质

身体有重心（骨盆/躯干中心），布料自由端（衣角/裙角/披风末端）**没有重心**——当身体突然转向时，自由端因惯性保持原方向，所以出现"身体转了衣角还没转"的错位帧。

#### 转身 3 阶段

```
【@24fps 基准，30fps 按 ×1.25 换算】
帧 N    ：身体开始右转，衣角还指向左（滞后状态）
帧 N+2  ：身体已完成右转 180°，衣角还指向左后方（最大滞后）
帧 N+3  ：衣角终于跟上，过甩 15-20° 再回到正常位置
帧 N+6  ：完全同步

【@30fps 换算】
帧 N    ：同上
帧 N+3  ：最大滞后
帧 N+4  ：过甩到位
帧 N+8  ：完全同步
```

#### 材质与滞后帧数关系

| 材质 | 转身滞后（@24fps） | **转身滞后（@30fps·主表）** | 急停滞后（@24fps） | **急停滞后（@30fps·主表）** |
|---|---|---|---|---|
| 丝绸/薄纱 | 2-3 | **3-4** | 1-2 | **1-2** |
| 棉布/毛衣 | 3-4 | **4-5** | 2-3 | **3-4** |
| 麻布 | 4-5 | **5-6** | 3-4 | **4-5** |
| 披风/斗篷 | 4-6 | **5-8** | 3-5 | **4-6** |
| 皮革 | 5-7 | **6-9** | 4-6 | **5-8** |

> 换算规则：30fps = 24fps × 1.25，四舍五入取整。

#### AI 提示词

```
EN: Character spins 180 degrees in a hurry, her hair and scarf lag 2 frames behind the head turn, scarf overshoots 20 degrees after the spin completes
中: 角色匆忙转 180°，头发和围巾比头的动作滞后 2 帧，转完后围巾过甩 20°
EN: Hero skids to a halt while cape still carries momentum forward, cape swings forward 25 degrees past the hero's torso before snapping back
中: 英雄紧急停下，披风还带着惯性向前摆，超过躯干 25° 再弹回
```

> 确定性：公认。来源：CLIP STUDIO 动画教程、Animation Mentor 在线课程（"hair and clothes sway one tempo behind body"）

### 动作拉扯优先级（AI 视频提示词顺序）

当多个拉扯同时作用时，按以下优先级写（影响从大到小）：

1. **动作本身**（跑步/挥剑/转身）——告诉 AI "主体在做什么"
2. **拉扯效果**（coat hem billows 45° backward / sleeve lags 2 frames）
3. **相对风**（headwind from running adds extra force）
4. **材质特征**（silk vs leather 不同摆动）——427 查表

#### 完整示例

```
EN: Samurai sprints at full speed then skids to a stop, robe sash billows 60 degrees backward from headwind, sleeve lags 2 frames behind each arm swing, the entire robe overshoots 20 degrees forward at the sudden stop before settling, wind from the sprint adds extra flutter to loose sleeves
中: 武士全速冲刺后紧急停下，腰带上因顶风后摆 60°，袖管每次摆臂滞后 2 帧，突然停下时整件袍子过甩 20° 再回落，冲刺的风给宽松袖管额外推力
```

## 备注

- 本条目核心物理来源：Disney 12 Principles（Follow-Through & Overlapping）、RebusFarm 指南、Animation Mentor 标准案例
- 数据准确性：滞后帧数（2-3 帧）和摆角是公认范围，overshoot 角度因材质有 ±5° 误差，属"经验级"
- 争议点：摔倒时衣服到底"绷多长时间"不同动画工作室有不同处理（1-3 帧都是合理范围），但"先绷后坠"模式无争议
- 与 428 的风场延迟可叠加——户外跑步的衣角延迟 = 动作延迟（2帧@24fps）+ 风场延迟（额外1帧）= 共 3 帧（@24fps）= 4 帧（@30fps）
- WAN3.0 校准（2026-10-20）：所有帧级参数补 30fps 换算（×1.25），材质滞后表新增 30fps 主表列；摔倒阶段已标注 @30fps 无需重复改
