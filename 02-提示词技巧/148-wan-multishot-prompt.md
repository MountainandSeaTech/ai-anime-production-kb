---
title: Wan3.0多镜头分镜提示词（Shot格式深入）
category: 提示词技巧
tags: [Wan, 分镜式, Shot, 多镜头, 提示词, WAN3]
source: 网络学习
created: 2026-10-13
updated: 2026-10-20
summary: Wan3.0的Shot [时间码]格式=一条提示词生成整场戏；但每Shot仍要守单镜纪律
scope: WAN3.0 单段内多镜头分镜式提示词（Shot [时间码] 写法）
validated_on: WAN3.0（2026-10-15）
related: [143, 138, 135, 146, 150]
---

# Wan3.0多镜头分镜提示词

## 核心要点
- Wan 3.0 支持在一条提示词内写多个Shot：**`Shot N [起始-结束s]: 描述 + Camera + Audio`**
- 单提示词生成整场戏=分镜验证/短剧原型的最快路径
- Wan 3.0 **单次生成最长 30s**（30s 是上限，不是建议值——见下"时长取舍"）
- 多Shot≠随意——**每Shot仍守单镜纪律**（单一动作/状态延续/轴线一致）
- 关联 143 Wan公式、138 多镜头连续、135 因果链

## Shot格式详解

### 标准结构
```
Shot 1 [0-2s]: [景别] of [主体+外观], [动作], [场景+光线].
  Camera: [运镜]. Audio: [声音].
Shot 2 [2-4s]: …
```

### 时间码规则
```
递增且连续：0-2 / 2-4 / 4-7 ✓
重叠：0-2 / 1-3 ✗
跳号：0-2 / 5-8 ✗
总时长 ≤ 模型单次生成上限（Wan 3.0 单次最长 30s）
```

### 时长取舍：30s 怎么用（2026-10 更正）
```
上限 30s ≠ 建议值 30s。两股力要平衡：
  拉长（用满上限）→ 接缝少、连续性好、模型内建承诺强，但要吃后段漂移
  收紧（多分段）  → 漂移可控、可单独重抽、单段翻车代价小，但接缝多

三条实操：
① 接缝尽量压在"动作切/硬切"上，别压在交手动势中段（分段处=穿模高发区）
② 镜数需实测（本条未验证）：镜越密后段越易糊——若后段出现换人/变形，
   把该段一拆二，宁多一段缝也别让模型硬撑
③ 长段必须补首尾帧锚：5-10s 靠氛围词就够，20-30s 要逐 Shot 重写锚词＋
   明确起止姿态，否则中段人物/武器先漂（144）
```

### Shot时长分配
```
建压Shot：给长（2-3秒）
爆点Shot：给短（1-1.5秒）
释放Shot：给长（2-3秒）
= 镜头时长的呼吸（关联023切频）
```

## 多Shot连续性保障

### 1. 角色锚词每Shot复写
```
Shot 1: "silver-haired swordsman in torn blue coat…"
Shot 2: "the silver-haired swordsman (same torn blue coat)…"
```
- 偷懒写"he"=AI可能换人——每Shot给完整锚点

### 2. 空间方位词延续
```
Shot 1: "…on the left of frame, facing right"
Shot 2: "reverse angle, he remains frame-left, facing right"
```
- 关联 131 轴线

### 3. 动作相位衔接
```
Shot 1结尾动作=Shot 2开头动作：
Shot 1: "…she raises her hand toward the door"
Shot 2: "her hand pushes the door open, …"
```
- 关联 132 动作匹配

### 4. 光线词全局一致
```
每个Shot重复光线锚：
"cold blue moonlight" → Shot 2: "same cold blue moonlight"
```

## 分镜式 vs 分次生成

| 维度 | Shot格式一次生成 | 逐镜生成 |
|---|---|---|
| 速度 | 快（一次出全场） | 慢 |
| 连续性 | 模型内建（较好） | 靠锚点接力 |
| 单镜控制 | 弱（不能单独重抽某镜） | 强（每镜独立调） |
| 适用 | 原型验证/简单场景 | 成片/复杂镜头 |
- **推荐流程：Shot格式做原型→确认节奏→逐镜精生成**

## 模板示例

### 例1：三镜短场景（发现）
```
Shot 1 [0-3s]: Wide shot, a wanderer in a tattered cloak
  enters the misty forest path, morning fog.
  Camera: slow push in. Audio: wind, distant crow.
Shot 2 [3-5s]: Close-up of the wanderer's face, eyes narrowing,
  noticing something off-screen right. Same morning fog light.
  Camera: static. Audio: wind dies down, silence.
Shot 3 [5-7s]: POV shot — a ruined shrine emerges from the mist
  on frame right. Camera: slow tilt up revealing the broken torii.
  Audio: a single deep bell toll.
```
- 3镜=看→反应→所见（133视线匹配结构）
- 每Shot：方位+光线锚+运镜+音频齐全

### 例2：战斗4镜（压缩节奏）
```
Shot 1 [0-1.5s]: Two swordsmen charge at each other across frame.
  Camera: lateral tracking. Audio: rapid footsteps on stone.
Shot 2 [1.5-2s]: Extreme close-up, blades clash mid-frame, sparks.
  Camera: static, slight shake. Audio: metal clash.
Shot 3 [2-3s]: One fighter staggers back, frame left, off-balance.
  Camera: handheld follow. Audio: heavy breathing.
Shot 4 [3-5s]: Wide shot, the victor stands still, rain resumes.
  Camera: slow pull out. Audio: rain, fading breath.
```
- 爆点Shot给0.5秒=切割最快
- 收尾Shot 2秒+拉远=释放（关联121三幕式）

### 例3：25s 完整戏剧节拍（三幕短喜剧原型）
```
Shot 1 [0-4s]: 幕起——清晨街角咖啡店，店主擦玻璃。
  Camera: static wide, warm morning light。Audio: 门铃脆响，远处车流。
Shot 2 [4-8s]: 冲突触发——外卖员冲进门，气喘吁吁找地址。
  Camera: slow push in to medium。Audio: 急促脚步声，背包拉链声。
Shot 3 [8-12s]: 误会加深——店主递外卖，外卖员说"这不是我的"，两人对视。
  Camera: two-shot static, slight tilt。Audio: 冰箱嗡鸣渐停，尴尬沉默。
Shot 4 [12-16s]: 翻转——第三个人走进来，原来外卖是给他的，大家笑。
  Camera: orbit slightly around group。Audio: 笑声，轻松 BGM 起。
Shot 5 [16-20s]: 收束——三人举杯碰咖啡，阳光更亮。
  Camera: slow pull back, lens flare。Audio: 杯盖轻碰声，BGM 延续。
Shot 6 [20-25s]: 尾声——咖啡店招牌特写，阳光正好。
  Camera: static close-up, soft focus。Audio: 风铃声，BGM 渐停。
```
- 6 镜 × 4.2s 平均 = 25s，在 30s 原生上限内
- 戏剧三幕：建立→冲突→翻转→收束（完整闭环）
- 每 Shot 角色/场景锚词逐镜复写+多模态参考辅助=长段不易漂

## 多模态参考辅助长段连续性（WAN3.0 专属）

20-30s 长段最大敌人是**后段漂移**（人物变脸/场景串味/道具消失）。WAN3 的 20 件多模态参考是目前最有效的抗漂手段。

### 抗漂参考堆叠法
```
必放：
  3-5 张角色设定图（同一角色不同姿态）——锁脸
  2-3 张场景参考图（同一场景不同光线）——锁环境
  2-3 张风格参考图（统一色调/颗粒/画风）——锁美术

可选但推荐：
  1-2 个动作参考视频（同类型动作）——锁节奏
  1-2 个音频参考（同风格 BGM）——锁氛围

参考排序：角色图 > 场景图 > 风格图 > 视频 > 音频
  （模型按输入顺序加权，重要的放前面）
```

### 长段连续性自检
```
生成 30s 段后回放检查：
□ Shot 1 vs Shot 7：角色脸/服装是否一致？
□ Shot 2 vs Shot 6：场景光线/时间是否连贯？
□ 中段（Shot 3-5）：是否有隐形漂移（不显眼但细看不对）？
□ 音频描述：每 Shot 是否都有声音锚？
```

## 长段漂移的后期兜底
```
如果 30s 段不可避免后段漂移：
① WAN3 本地编辑：选中漂移段→改锚词→局部替换（优先试）
② 分段重生成：把 30s 拆成 15s+15s，各自用首尾帧接力
③ 逐镜精做：放弃 Shot 格式，每镜独立生成+锚点接力（最稳但最慢）
```

## 常见坑
- **Shot当分镜表用**：单段塞 20+ Shot＝信息过载，后段易糊；30s 上限下建议单段 8-12 镜（快剪战斗可到 15-18，需实测）
- **锚词省略**：Shot2起用代词=角色换人
- **时间码超标**：时间码总和超单次上限（Wan 3.0 = 30s）=尾部 Shot 被截
- **每Shot塞多动作**：违反146单动作铁律
- **音频行丢三落四**：只写Shot1音频=后面Shot静音断裂感

## 进阶
- **Shot格式做预演**：先用Shot格式低成本验证整场戏节奏，再决定哪些镜头值得逐镜精做
- **嵌套提示词**：复杂单Shot可先在Shot格式里定调，再单独拿出来用143完整公式扩写
- **音频叙事线**：音频行按137设计J/L-cut逻辑（Shot N+1的声音在Shot N末尾提及）
- **Shot改写循环**：某个Shot不满意=把该Shot拆成独立提示词精调，再剪回去

## 备注
- Shot [时间码]格式=一条提示词一场戏
- 每Shot四件套：画面+Camera+Audio+锚词复写
- 原型用Shot格式，成片逐镜精做
- 单次上限：Wan 3.0 = 30s；接缝压在"切"上，别压在交手中段
- 关联：143 Wan公式、146 铁律、138 连续性、137 声音桥
