---
title: Breaking-PowerMoves高阶篇——托马斯/大回环/头转/1990/2000
category: 动作与战斗
tags: [街舞, breaking, powermove, flare, airflare, headspin, 1990, 2000, halo, 托马斯, 大回环, 头转, 手转, 动作编排, AI视频]
source: 社区
created: 2026-10-16
updated: 2026-10-16
summary: Breaking空中系五大旋转大招形态辨识与力学要点、连招衔接顺序、仰角机位与AI分段生成策略
related: [313, 316, 317, 327, 330]
---

# Breaking-PowerMoves 高阶篇：Flare / Air Flare / Head Spin / 1990 / 2000

## 核心要点

- 五个高阶招分两族：**绕手摆腿族**（Flare 托马斯、Air Flare 大回环）——双手轮流撑地、腿画大圈；**直立旋转族**（Head Spin 头转、1990 单手转、2000 双手转）——倒立成线、垂直轴自转
- 辨识一句话：**Flare 身体朝上头朝天、腿低位扫圈；Air Flare 身体倾斜近倒立、胸交替翻向地面、整个人"飞"在高处转圈；头转用头、1990 用一只手、2000 用两只叠手**
- 高阶大招的视觉本质是"**离地高度**"：脚离地越彻底、支撑点越少越炸；机位必须用仰角或斜 3/4 角证明"人在空中"
- 连招（combo）黄金顺序：风车 → 托马斯 → 大回环 → 1990/2000 收（低→高、多支撑→少支撑），本身就是一条爬升能量曲线
- AI 生成：高阶动作必崩率高于基础招，策略为**拆成"起势-半圈-收 freeze"三段分别生成再剪**，不要让模型一次生成完整多圈

## 详细内容

### 一、Flare（托马斯全旋 / 托马斯）

- **来源**：体操托马斯全旋（Thomas Flair），被 breaking 吸收
- **形态**：双手在身前依次撑地，**双腿伸直大大打开、在低位连续画大圈摆越**；一条腿从身前扫过、另一条从身后带过，双手在腿经过时交替推离-撑回
- **身体朝向**：胸始终朝上或微侧，脸看前方/上方；身体与地面夹角约 30–60°
- **一圈关键拍**：
  1. 双手身前撑地，双腿大开，一腿前摆蓄力
  2. 前腿横扫过支撑手（对侧手短暂抬起让腿）
  3. 双腿在身后形成大分腿，重心换手
  4. 后腿再从另一侧扫回，回起始位，立刻接下一圈（不能停）
- **命门**：**腰胯要高、脚尖要绷、圈要圆**；腿掉高度、膝盖弯曲立刻变"坐地转圈"
- **变体**：Virgin（双腿并拢的 flare，更难）、Lotus flare（盘腿）、Elbow flare（肘撑）

### 二、Air Flare（大回环 / Airtrack）

- **形态**：breaking 最高标志招之一。身体近倒立倾斜，**双手交替短促撑地、双脚全程不落地**，整个人沿一个大圆弧在空中翻转行进；胸在一圈内交替朝地-朝天
- **与 Flare 核心区别**：
  - Flare：胸朝天、身体低、腿在低位扫
  - Air Flare：胸会翻向地面、身体高、像倾斜的倒立在"换手飞行"
- **一圈关键拍**：
  1. 从倒立/风车/halo 位起势，一腿用力向斜上方甩高画弧
  2. 单手撑地、身体翻向地面，腿的圆弧把身体带过支撑手
  3. **空中换手**（最难的一拍）：原手推离、另一手接住，后背朝向地面时完成交接
  4. 双腿继续画大圆带身，回到近倒立位，接下一圈或收成手转/freeze
- **动力**：圆摆腿（circular leg swing）是命门，手只负责"点"地，不是撑起
- **镜头**：斜 3/4 仰角跟圆弧横移，或正面微仰；连续 air flare 配慢速环绕机位可强化"飞行"错觉

### 三、Head Spin（头转）

- **形态**：头顶着地为唯一轴心，双手在头两侧，身体竖直倒立；双腿摆出稳定造型（并拢、分腿或抱胸团身）
- **启动**：从头立位双腿先向一侧甩摆获得扭转，随即双手**短促推地**把身体抬离地面，仅以头顶+帽子/头盔接触旋转
- **加速**：每一圈手再点推 1–2 次（taps），腿的开合也可调速（打开减速、收拢加速，角动量守恒）
- **视觉**：转速最快的招之一，常配"先慢速 1 圈展示造型→团身疾转多圈→展身急停"的编排
- **防护语义**：真人必须头盔/针织帽；AI 画面中帽子是造型特征不是可选项时保留

### 四、1990（单手转）与 2000（双手转）

| 项 | 1990 | 2000 |
|---|---|---|
| 支撑 | **单手掌**全掌接地、臂伸直 | **双手掌上下叠压**（十指可交叉）共成一个支点 |
| 身体 | 竖直倒立、双腿并拢绷直成线，非支撑手收贴背/胸或扶腕 | 同左，双臂合一承担 |
| 启动 | 常见从风车/flare 提身、或倒立位扭腰甩腿起转 | 倒立位小跳+甩肩起转 |
| 观感 | 更险、更"一根针上转" | 更稳、可转更多圈 |
| 圈数 | 高水平 5–10 圈 | 常更多 |

- 两者都要**肩完全顶开、身体一条垂直线、脚尖上领**；弯腰、塌肩立刻失衡
- 收招：旋转减速→另一手轻点地→落腿→接 freeze 或 footwork

### 五、Halo（头环）与其他衔接招

- **Halo**：以头顶为轴、双肩在地面交替滚动的"高位风车"，头在地面画小光环——风车到头转之间的桥
- **Turtle（乌龟）/ Turtle 转**：双肘顶腹、双手撑地身体水平悬空，靠手连续小幅移动原地旋转（float 系）
- **Air Walk（空中步）**：倒立位双手交替小幅跳起前移，像手在走路——炫耀控制力
- **Shoulder Spin**：单肩着地团身高速转，常夹在风车与定格之间

### 六、连招衔接表（Combo Ladder，按高度爬升）

```
Footwork(315)
  → Windmill(317)          [肩背支撑，最低]
  → Halo                   [头+肩]
  → Flare                  [双手点地，腿腾空]
  → Air Flare              [双手交替，整身腾空]
  → 1990 / 2000 / Head Spin [单点直立旋转，最高最险]
  → Air/Handstand Freeze(316) [钉在重拍收尾]
```

- 每升一级，支撑点减少、高度上升、转速或风险感上升——**分镜按此顺序给镜头规格升级**（景别收紧、慢动作时长增加、切点加密）
- 也可以反向"降级连招"制造意外：从 2000 突落 baby freeze，落差即炸点

## 关键参数 / 模板 / 清单

### 提示词模板（高阶大招）

```
b-boy performing continuous [flares / air flares / a head spin / a 1990],
flare: body facing up, legs in wide straddle sweeping large circles, hands alternating support
airflare: near-inverted body arcing through air, alternating hands, chest flipping groundward, feet never touch
headspin: vertical on crown of head, legs [together/in split], hands tapping to accelerate
1990: vertical one-hand handstand spin, body in one straight line, other hand on back
[1-2 rotations only], powerful circular momentum, [low 3/4 angle looking up], 
ground-level dust/shadow showing height, [场景]
exit: slow rotation then lock into air freeze on beat
负向：bent knees, sagging hips, feet dragging floor, feet touching ground on airflare, 
two hands shown during a 1990, curved spine, extra limbs, floating with no support, 
gymnastics vault horse, sequence teleportation
```

### AI 分段生成脚本（推荐 3×3 秒拼接）

| 段 | 内容 | 锚点 |
|---|---|---|
| A 起势 | footwork/风车末段→第一下甩腿进入 | 首帧喂起势参考图，末帧留"已离地" |
| B 旋转 | 半圈到一圈半的飞行/自转 | 固定机位、固定方向，1.5 圈内 |
| C 收招 | 减速→支撑→freeze hold 2 拍 | 末帧喂 freeze 参考图（316） |

### 验收清单

- [ ] Flare：胸朝上、腿大开直、圈为水平大圆，无坐胯屈膝
- [ ] Air Flare：有胸朝地的翻转帧、双脚全程无落地帧
- [ ] Head Spin：竖直成线、头顶为唯一接触、手只做点推
- [ ] 1990 全程只有一只手在地上（另一只手位置稳定）；2000 双手叠成一个支点
- [ ] 旋转方向、服装甩动方向、尘土方向三者一致
- [ ] 画面中看得见地面参照（影子/地胶纹理），证明高度与速度
- [ ] 收招 freeze 锁在重拍，镜头不与旋转同时乱晃（晕镜头）

## 备注

- 命名辨析：Air Flare＝大回环（大陆教学常称），港台称 Airtrack；日语圈称風車的延伸招时命名易混，英文提示词按本条目描述写可避免模型串招
- 真实高危：头转/大回环为高伤害风险动作，条目仅服务 AI 内容创作的动作描述与分镜
- Breaking 全套（314–318）至此完结；从下条起进入 Popping
