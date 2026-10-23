---
title: 头发物理——挂在头上的"第二披风"动力学
category: 作画与光影
tags: [头发, 布料物理, follow-through, 风动态, 发型, 动画原理]
source: 网络学习 + 动画原理
created: 2026-10-20
updated: 2026-10-20
summary: 头发 = 挂在头上的独立微动体——长发软滞后、短发硬快摆、扎辫有独立摆动相位；转头滞后、奔跑后甩、长发飘肩过脸
related: [406, 074, 225, 238, 442, 443, 445]
---

# 头发物理——挂在头上的"第二披风"动力学

## 核心要点

- 头发与布料同属"挂在身上的独立微动体"——AI 视频中最容易被忽略的动态信号之一（公认）
- 三种发型的风动态：**长发软滞后（滞后 1.5-2 帧）、短发硬快摆（滞后 0.5 帧）、扎辫独立摆动**（公认）
- 转头时头发**滞后甩出反向再回摆**——与裙摆转身原理相同（重叠动作原理）
- 奔跑时长发几乎完全向后甩成流线形，风阻主导而非身体带动（公认）
- 头发与衣服交互：长发会飘到肩上、被风吹到脸上、跑步时发尾可能扫过背（经验）
- 头发层次=动态层次：顶层被风先吹起、中层跟随、底层最后响应（公认）

## 详细内容

### 发型 × 动态参数表

| 发型 | 英文术语 | 风阻面积 | 滞后帧数 | 动态特征 | 提示词关键词 |
|---|---|---|---|---|---|
| 超短发（寸头） | buzz cut | 极小 | 0 帧 | 几乎无动态，只随头动 | `very short hair, no independent motion` |
| 短发（耳下） | short bob | 小 | 0.5 帧 | 硬挺摆动，摆幅小 | `short bob with slight lag swing, 0.5 frame delay` |
| 中长发（肩） | shoulder-length | 中 | 1 帧 | 波浪摆动，层次清晰 | `shoulder-length hair waving in S-curves, 1 frame lag` |
| 长发（腰/臀） | long hair | 大 | 1.5-2 帧 | 软流体，大幅后甩 | `long hair flowing dramatically behind, 2 frame lag` |
| 双马尾 | twin tails | 中（分两股） | 1 帧（每股独立） | 两个独立钟摆 | `twin tails swinging independently like pendulums` |
| 马尾辫（高） | high ponytail | 小-中 | 1 帧 | 大幅前后甩 | `high ponytail bouncing forward-backward` |
| 马尾辫（低） | low ponytail | 中 | 1.5 帧 | 左右摆+上下飘 | `low ponytail swaying side-to-side and floating` |
| 麻花辫 | braid | 小（编织紧实） | 1 帧 | 硬角摆动，发梢微颤 | `braid swinging with sharp angles, tip trembling` |
| 散卷长发 | curly long | 大（每缕独立） | 2-3 帧（每缕不同） | 非常不规则 | `curly hair with each strand responding independently to wind` |
| 齐耳碎发 | layered short | 中 | 0.5-1 帧 | 各层分别飘 | `layered short hair with each layer lifting separately` |

### 三种核心运动下的头发动态

| 运动 | 头发主方向 | 滞后 | 关键信号 | 提示词 |
|---|---|---|---|---|
| 转头（快速） | 反向甩出（惯性）→ 被拉回 | 1.5-2 帧 | 角色警觉/突然反应 | `hair lagging 2 frames behind head turn, whipping opposite direction before snapping back` |
| 奔跑 | 向后完全展开 | 1.5 帧 | 速度感、空气动力学 | `long hair stretched horizontally behind by running speed, wind resistance dominant` |
| 跳跃 | 先因失重下垂 → 再被风拉起 | 1 帧 | 跳跃瞬间失重感 | `hair dropping downward on jump (weightless), then caught by wind mid-air` |
| 静止有风 | 风向决定（长发飘起） | 2 帧 | 环境有风（呼应 406 场景生机） | `long hair drifting in ambient wind, layered response - top lifts first, bottom follows` |

### 头发层次响应（分层风阻）

头发不是整体一块——分层响应是让头发看起来"真"的关键：

| 层次 | 风阻优先级 | 滞后 | 效果 |
|---|---|---|---|
| 顶层（刘海/头顶发） | 最先被风吹动 | 0.5 帧 | 刘海先飘起来 |
| 中层（脸颊/耳侧） | 第二波 | 1 帧 | 脸颊发跟着飘 |
| 底层（发尾/后脑勺） | 最后响应 | 1.5-2 帧 | 发尾最后被甩起 |

```
# 分层头发动态提示词
hair responding in 3 layers: top layer (bangs/forehead) lifts first 
(0.5 frame lag), middle layer (cheek/ear) follows (1 frame lag), 
bottom layer (tips/nape) lags 1.5-2 frames
```

### 头发与衣服的交互场景

| 场景 | 交互效果 | 提示词 |
|---|---|---|
| 长发+肩膀 | 长发飘到肩上，形成 S 曲线搭肩 | `long hair draping over shoulder in natural S-curve` |
| 被风吹+脸部 | 发梢被风吹到脸上/眼睛前 | `strand of hair blown across face by wind` |
| 奔跑+背带 | 发尾扫过背包/披风 | `long hair tip brushing against backpack with each stride` |
| 低头+长发 | 长发从肩上垂到胸前，有重力感 | `long hair falling forward over chest when head bows` |
| 甩头+长发 | 长发甩起成弧形，有惯性回弹 | `long hair swinging in wide arc after head flick` |

### AI 视频提示词中英对照

```
# 正常走路 + 马尾辫 + 有风
high ponytail bouncing 1 frame behind head movement, 
strands separating slightly in ambient wind, tip trembling

# 快速转头 + 长发 + 奔跑前的警觉
long hair lagging 2 frames behind head snap turn, 
whipping 180° in opposite direction before being pulled back, 
strands catching individual wind gusts

# 奔跑 + 长发 + 披风联动
long hair stretched horizontally behind (2 frame lag), 
cape at 30° angle behind (1.5 frame lag), 
both synchronized to running rhythm

# 静止 + 齐耳碎发 + 微风
layered bob with 3-layer wind response: top bangs lift first, 
middle cheek strands follow, bottom nape hair lifts last, 
1.5 frame total lag
```

### 头发物理的"空气力学参数"

| 风速 | 英文 | 长发表现 | 提示词 |
|---|---|---|---|
| 0-0.5 m/s（微风） | gentle breeze | 微微飘起，发梢晃动 | `hair gently tousled by soft breeze, tips swaying` |
| 1-2 m/s（轻风） | light wind | 明显飘向风向 | `long hair drifting toward wind direction, flowing` |
| 3-5 m/s（强风） | strong wind | 完全被风吹平 | `hair blown completely flat by strong wind, no independent strands` |
| > 10 m/s（狂风） | gale | 被吹得紧贴头面、部分打结感 | `hair flattened against head and face by gale-force wind` |

## 备注

- 头发与裙摆（442）、披风（443）、配饰（445）同属"挂在身上的独立微动体"家族，遵循 follow-through 和 overlapping action 两大动画原理（公认）
- 头发分层响应 = 空气力学 × 层次结构，与披风波浪层次同原理（443）
- 马尾辫在奔跑时的"前后甩"而非"左右摆"是马尾辫独有的特征——这是离心力与空气阻力共同作用的结果（公认）
- 齐耳碎发（layered hair）的每层独立响应在 AI 视频中较难稳定生成，可额外强调 `each layer responds separately`
- 本条目是头发在"正常重力环境"下的物理；水下/太空/失重的头发物理不在此覆盖
- 确定性：分层风阻和滞后帧数属业界公认动画经验；具体数值来自实战测试（经验）
