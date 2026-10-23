---
title: 披风/斗篷专篇——长度·姿态·镜头引导三重视角
category: 作画与光影
tags: [披风, 斗篷, 布料物理, 风动态, 镜头引导, 转场技巧]
source: 网络学习 + 动画原理
created: 2026-10-20
updated: 2026-10-20
summary: 披风/斗篷是角色的"第二动作系统"——短披肩硬挺角、中披风波浪 S、长大披风流体拖曳；还能引导视线、作为转场
related: [406, 074, 238, 225, 442, 444, 445]
---

# 披风/斗篷专篇——长度·姿态·镜头引导三重视角

## 核心要点

- 披风 = 角色的**动作放大器**：长度决定动态类型（公认）、姿态决定气势信号（经验）
- 长度三档：短披肩（< 肘）= 硬挺角 / 中披风（肘-膝）= 波浪 S 曲线 / 长大披风（> 膝）= 流体拖曳（公认）
- 静止时披风仍要有风的微动——没有就是挂在墙上的布（呼应 406 场景生机法则）
- 披风作为**镜头引导**：飘动方向强制观众视线跟随角色移动方向（公认）
- 披风**掀落/飞起**可做转场：披风完全展开遮画面 → 下一镜披风在新场景收回（动画业界惯用）
- 骑马/飞行时披风的风阻模式完全不同于步行（经验）

## 详细内容

### 披风长度 × 动态类型对照表

| 类型 | 英文术语 | 长度 | 风动态 | 角色静止时 | AI 提示词 |
|---|---|---|---|---|---|
| 短披肩 | short capelet | 肩到肘 | 硬挺三角摆动，几乎不弯 | 贴肩微颤，边缘略飘 | `short capelet stiffly flapping with sharp angles` |
| 中披风 | standard cape | 肘到膝 | 明显 S 波浪，中段拐点 | 波浪起伏，底边有节奏地扫 | `medium cape flowing in graceful S-curves` |
| 长大披风 | long cloak | 膝以下/拖地 | 流体式拖曳，多层波纹 | 大面积起伏，底边有涡旋 | `long cloak billowing in fluid waves, trailing on ground` |
| 连帽斗篷 | hooded cloak | 变化大 | 风穿过兜帽形成额外抖动 | 兜帽耳侧晃动 | `hooded cloak with hood flapping slightly` |
| 披风＋披帛 | cape + sash | 双层 | 外层硬挺＋内层柔软飘带 | 内层先动、外层后动 | `outer cape rigid, inner silk sash drifting freely` |

### 不同姿态下的披风表现

| 姿态 | 披风动态 | 核心信号 | 提示词 |
|---|---|---|---|
| 站着不动 | 风驱动的小幅度波浪（必须有！） | 环境有风、角色沉稳 | `cape gently billowing in ambient wind, subtle S-wave` |
| 走路 | 缓慢后摆，底边周期扫地面 | 角色匀速移动 | `cape trailing behind in smooth arcs with each step` |
| 奔跑 | 大幅后甩成翼状，前沿被风鼓起 | 速度感加强 | `cape flapping horizontally behind like wings, wind catching front edge` |
| 骑马 | 披风底部被气流向上掀起（因马速快） | 高速移动感 | `cape whipped upward and backward by gallop airflow` |
| 飞行/滑翔 | 披风像降落伞般完全展开 | 角色掌控空间 | `cape fully spread like a wingsuit, fabric taut with air resistance` |
| 转身 | 披风滞后 2-3 帧甩出反向 | 角色改变方向有动量 | `cape lagging 2 frames behind turn, whipping outward then snapping back` |
| 跃起 | 披风先下垂（离地失重）再被风拉起 | 跳跃瞬间 | `cape dropping first on jump, then caught by wind mid-air` |
| 战斗姿势（拔刀前） | 披风被肌肉绷紧拉向肩背 | 即将动武的张力 | `cape pulled taut across shoulders by tense posture` |

### 披风作为镜头引导（视线控制）

披风的飘动方向是**最强的视线引导线**：
- 披风向左飘 → 观众视线被拉向左 → 自然跟随角色向左移动的方向
- 披风掀起遮画面 → 下一镜在新环境收回披风 → **无缝转场**（《进击的巨人》MAPPA 版常用）
- 披风扫过前景 → 遮蔽→揭示 的景深错觉

```
# 披风镜头引导提示词
pan cape flowing leftward forcing viewer eye to follow character
cape edge entering frame from right, sweeps across → reveals new scene

# 披风转场提示词
long cloak flapping into frame until fabric fully covers screen → cloak 
pulls back to reveal character standing in completely different location
```

### 披风掀落/披风飞扬转场套路

| 转场类型 | 描述 | 经典用例 | 确定性 |
|---|---|---|---|
| 披风遮画面 | 披风飞大盖住整帧 → 下一镜披风收回在新场景 | 《鬼灭之刃》无限列车篇 炼狱炎柱登场 | 公认 |
| 披风甩出 | 角色转身时披风大幅甩出 → 切到披风扫过的新场景 | 《进击的巨人》MAPPA 最终季 | 经验 |
| 披风滑落 | 披风从肩上滑落 → 地面披风为前景 → 切到角色新身份/新地点 | 《死神》队长袍解体 | 经验 |

### 材质对披风动态的修正

| 材质 | 英文 | 动态差异 |
|---|---|---|
| 厚重毛呢/麂皮 | wool, suede | 波浪宽、滞后感强、飘动慢 |
| 丝绸/缎面 | silk, satin | 波浪密、反光、飘动灵活 |
| 皮革/仿皮革 | leather | 几乎无波浪、只有硬角摆动 |
| 薄纱/蕾丝 | organza, lace | 完全流体、透光、被风整体掀起 |

```
# 鬼灭风披风（厚棉+内衬）
thick cotton demon slayer cape, stiff edges with slight billow, 
wave amplitude 30°, lag 1.5 frames, inner red lining visible when flapping

# 进巨风斗篷（厚重帆布）
heavy canvas survey corps cloak, rigid flap pattern, 
stiff trailing, slow wave motion with 2-frame lag

# 死神队长袍（混合）
bleach captain haori, outer solid, inner lined, 
layered wave motion with 2 distinct frequencies
```

## 备注

- 披风与裙摆（442）、头发（444）、配饰（445）同属"挂在身上的独立微动体"物理家族，共享 follow-through 滞后原理（公认）
- 披风作为镜头引导的功能呼应 225（线条方向塑体积）——披风线条 = 最强方向性线条
- 披风风阻的物理模拟可参考 446（布料物理实片拆解方法论）的拆解流程
- 《大剑》《咒术回战》《银魂》也是披风/斗篷动态的优质拆解对象
- 与 074（服装张力信号）联动：战斗姿势时披风被绷紧 = 张力信号；奔跑时披风松 = 速度信号
- 确定性：长度-动态对应关系为业界公认；镜头引导和转场技巧为动画导演经验总结
