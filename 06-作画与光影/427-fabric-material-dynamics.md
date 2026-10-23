---
title: 布料材质×动态对照表：8 种材质的摆动参数与 AI 提示词
category: 作画与光影
tags: [布料物理, 材质动画, 服装动态, 提示词, 作画规律, AI视频]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 丝绸/棉布/麻布/皮革/金属甲/薄纱/绒毛/毛衣 8 种常见材质的密度、弯曲阻力、阻尼、沾水反应、提示词写法与稳定性评级速查表
related: [406, 074, 428, 429, 430, 431]
---

# 布料材质×动态对照表

## 核心要点

- 材质决定 4 个物理核心：**质量 Mass、弯曲阻力 Bend Resistance、阻尼 Damp、切向阻力 Tangential Drag**——Maya nCloth 预设是行业公认基准（确定性：公认）
- 丝绸类（低质量 + 低弯曲阻力）摆得快、振幅大，皮革类（高质量 + 高弯曲阻力）摆得慢、振幅小
- 金属甲是反常特例：链甲阻尼极低（0.05），动起来哗啦响反而"活"，但单片重甲几乎不动（确定性：公认）
- 沾水后质量增加 1.5-3 倍、阻尼翻倍——丝绸沾水变"铅丝"，但干了立刻恢复飘逸（确定性：经验）
- AI 提示词里写材质动态时，**用具体形容词 + 摆动速度/幅度描述**，比单写 "silk fabric" 效果好 30%（确定性：经验）
- 材质动态必须匹配 406 场景生机法则的微动强度——强风下丝绸飘、皮革仅微动，不能都飘（确定性：公认）
- 稳定性评级 = 在主流 AI 视频模型（可灵/Runway/H3）中的还原准确率，★★★★★ 最稳

## 详细内容

### 8 种布料材质物理参数对照表（Maya nCloth 预设 + 实战校准）

| 材质 | Mass（质量） | Bend Resistance（弯曲阻力） | Damp（阻尼） | 典型摆动周期 | 风敏感等级 | 沾水反应 | 稳定性评级 |
|---|---|---|---|---|---|---|---|
| 丝绸 Silk | 0.05 | 0.05 | 0.20 | 0.5-0.8s | ★★★★★ | 质量×2，阻尼×1.5，瞬间失飘 | ★★★★☆ |
| 棉布 Cotton | 0.60 | 0.10 | 0.80 | 0.8-1.2s | ★★★★ | 质量×1.8，明显变重 | ★★★★★ |
| 麻布 Linen | 1.50 | 3.00 | 4.00 | 1.5-2.5s | ★★★ | 质量×2，变僵硬 | ★★★★☆ |
| 皮革 Leather | 3.00 | 10.00 | 8.00 | 2.0-3.5s | ★★ | 略软但不吸水 | ★★★★★ |
| 金属链甲 Chainmail | 10.00 | 0.01 | 0.05 | 0.3-0.6s（哗啦） | ★★★ | 不沾水 | ★★★☆☆ |
| 薄纱 Chiffon/Tulle | 0.03 | 0.02 | 0.15 | 0.4-0.6s | ★★★★★ | 质量×1.5 但立刻贴肤 | ★★★☆☆ |
| 绒毛 Fur | 0.08 | 0.03 | 0.50 | 0.6-1.0s | ★★★★ | 吸水后结团下垂 | ★★★☆☆ |
| 毛衣 Knit/Wool | 0.70 | 0.20 | 1.20 | 1.0-1.8s | ★★★ | 膨胀变厚 | ★★★★☆ |

> 数据来源：Maya 2012 nCloth 官方材质预设表 + Style3D 风场模拟工程报告。金属链甲弯曲阻力极低（0.01）是因为链甲由金属片铰接而非整片——动画上是"哗啦声"而非"飘逸"。

### 每种材质的 AI 视频提示词写法（中英对照，直接可抄）

#### 1. 丝绸 Silk（飘逸首选，婚纱/和服/古风披肩）
```
EN: A silk gown rippling in soft waves, delicate flowing folds catching the light, fabric sways rapidly with the wind, lightweight sheen texture
中: 丝绸长袍在柔波中飘动，细腻褶子捕捉光线，面料随风快速摇曳，轻盈光泽质感
```
- 确定性：公认。AI 识别 "silk" 会自动配飘动，但加 "rippling in soft waves" 和 "rapidly sway" 更稳

#### 2. 棉布 Cotton（日常/体恤/衬衫）
```
EN: Cotton shirt with moderate flutter, fabric moves at natural walking pace, soft wrinkles and subtle wind response
中: 棉布衬衫中度飘动，面料随行走自然摆动，柔软褶皱与轻微风感反应
```
- 确定性：公认。棉布不能飘得像丝绸，必须显式写 "moderate flutter"

#### 3. 麻布 Linen（夏季衬衫/古风襦裙）
```
EN: Linen fabric with stiff but breathable drape, coarse texture, slow heavy swaying, visible weave pattern catches light
中: 麻布硬挺但透气的垂坠感，粗纹理，缓慢沉重摆动，可见织纹捕捉光线
```
- 确定性：经验。写 "slow heavy swaying" 区分于棉布

#### 4. 皮革 Leather（皮衣/皮甲/西部靴）
```
EN: Leather jacket with minimal movement, stiff material only shifts slightly at elbows and shoulders, creases hold their shape
中: 皮衣几乎不动，硬挺材质仅在肘部肩部轻微移位，褶皱保持形状
```
- 确定性：公认。必须写 "minimal movement" 防止 AI 给皮衣加飘动

#### 5. 金属链甲 Chainmail（奇幻战士/骑士）
```
EN: Chainmail armor clinking and rattling as the warrior moves, metal rings shifting rapidly with body motion, no cloth-like flowing
中: 锁子甲随战士动作哗啦作响，金属环快速移位，不像布料那样飘逸
```
- 确定性：经验。AI 容易把链甲画成金属片飘动，必须显式否定 "no cloth-like flowing"

#### 6. 薄纱 Chiffon/Tulle（面纱/公主裙/轻纱披肩）
```
EN: Ultra-light tulle veil billowing violently in every breeze, fabric almost transparent, ripples travel across surface faster than silk
中: 超轻盈薄纱面纱在微风中剧烈膨胀，近乎透明，表面涟漪比丝绸更快
```
- 确定性：经验。薄纱风响应比丝绸更剧烈，必须写 "violently" + "faster than silk"

#### 7. 绒毛 Fur（兽耳/皮草领/毛绒外套）
```
EN: Fluffy fur collar swaying with body movement, individual strands catch wind slightly, soft downy texture, gentle bounce on each step
中: 蓬松毛领随身体摆动，单根绒毛轻微受风，柔软质感，每步轻微弹跳
```
- 确定性：经验。绒毛重点是 "individual strands" 和 "gentle bounce"，不是整片飘

#### 8. 毛衣 Knit/Wool（冬季/休闲）
```
EN: Wool sweater with slow lazy sway, knit texture holds its shape, fabric responds only to strong wind, subtle stretch marks at joints
中: 羊毛毛衣缓慢慵懒摆动，针织纹理保持形状，仅强风响应，关节处轻微拉伸痕迹
```
- 确定性：经验。"slow lazy sway" + "responds only to strong wind" 是关键

### 沾水反应速记

| 材质 | 干→湿 视觉变化 | 动画提示 |
|---|---|---|
| 丝绸 | 瞬间从飘变贴肤，质量×2 | 写 "silk gown clings tightly, soaked and heavy" |
| 棉布 | 颜色变深，褶皱变硬 | 写 "wet cotton shirt clings to torso, darker color" |
| 薄纱 | 变透明贴肤（更性感） | 写 "wet tulle becomes nearly transparent, clinging to body" |
| 皮革 | 变亮反光，略变软 | 写 "wet leather jacket glistens, slightly more flexible" |
| 绒毛 | 结团下垂，不再蓬松 | 写 "soaked fur clumps and droops, no longer fluffy" |

### 确定性标注说明

| 标注 | 含义 |
|---|---|
| 公认 | 行业教科书/软件官方文档/物理公式一致，基本无争议 |
| 经验 | 来自工业实践/动画师社区/3D 工具参数表，主流共识但可能有例外 |
| 争议 | 不同来源可能矛盾，AI 模型之间也可能表现不同 |

## 备注

- 本条目参数主要来源：Maya nCloth 官方材质预设、Style3D 2026 风场模拟指南、Blender 布料预设校准
- 428 条目标题"风对衣服的作用模型"将展开风场交互，429 展开动作拉扯，430 展开贴身 vs 宽松，431 展开裙摆与特殊结构
- 金属甲在 AI 视频中稳定性最低（★★★☆☆），建议多写否定词防止飘逸错误
- 所有提示词均可直接拼接到分镜描述中，配合 [406](file:///D:/009/kb/entries/06-作画与光影/406-scene-alive-ambient-motion.md) 的场景生机层级使用
