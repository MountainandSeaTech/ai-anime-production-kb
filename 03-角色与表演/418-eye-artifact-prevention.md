---
title: AI 视频眼部崩坏防治——成因·负面提示词·图生视频参数
category: 角色与表演
tags: [眼部崩坏, 负面提示词, 图生视频, 稳定性, 斗鸡眼, 瞳孔漂移]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 眼部崩坏五大型（斗鸡眼/双眼不同步/瞳孔漂移/眨眼卡半开/高光乱闪）的成因诊断、负面提示词写法与"运动越小越稳"的图生视频参数策略
related: [163, 165, 133, 417, 419, 420, 421]
---

# AI 视频眼部崩坏防治

## 核心要点
- **先诊断首崩帧，再改参数**（公认）：逐帧拖时间轴，找到"第一次崩"的时间点——之后的所有变形都可能是它的后果。改一个变量重测，别随机抽卡
- **崩坏主因是运动负载**（公认）：头部大角度转动（尤其转头再转回）、相机运动+快速动作+灯光变化叠加、单条提示多事件——模型对脸的 3D 理解跟不上就会"重发明"五官
- **运动幅度越小越稳是铁律**（公认）：眼特写镜头一次只动一个变量——1 次眨眼或 1 次视线转移，不要都要
- **负面提示词要短、具体、可见**（公认）：3-6 条名词短语（如 "asymmetrical eyes"），不写 "don't make it weird" 这类抽象命令；先修正面提示词再加负面
- **特写片段控制在 4-6 秒**（经验）：10 秒以上生成常出现后段"融化"（melting），表情漂移回中性刻板脸——在漂移前剪断比重生成便宜
- 关联：163 总纲翻车表、417 稳定性评级、419 景别阈值

## 详细内容

### 一、五大眼部崩坏对照表
| 崩坏型 | 视觉症状 | 主要成因 | 首选对策 |
|---|---|---|---|
| 斗鸡眼/斜视 (cross-eyed) | 双眼视线不汇聚、各看各的 | 双人特写视线指令冲突；无明确注视目标 | 写画内具体目标（"eyes fixed on the mug"），双人戏单侧描述+133 方位词 |
| 双眼不同步 (asymmetrical eyes) | 一眼大一眼小、眨眼不同时 | 源图脸部遮挡/侧脸极限角度；解剖结构不稳 | 换 3/4 或正面源图；负面词加 "asymmetrical eyes" |
| 瞳孔漂移 (wandering pupils) | 瞳孔无目的游走、身份漂移 | 一条提示里塞多次眼动指令；"eyes dart everywhere" 类高危词 | 5-6 秒片段只放 1 次视线变化；降低 motion 强度词 |
| 眨眼卡半开 (half-blink freeze) | 眼睑停在半闭、抖动 | 眨眼时长写太长；时长超 6 秒后模型调度失控 | 写 "a single slow blink" 单次事件；缩短片段；运动幅度调低 |
| 高光乱闪 (catchlight flicker) | 眼中光点跳动、位置乱变 | 光源描述缺失或变化；灯光闪烁 | 正面提示锁定 "soft key light from frame left, consistent lighting"；负面加 "lighting flicker" |

### 二、负面提示词写法（通用规范）
- **格式**：名词短语、可见缺陷、一次 3-6 条，按实际观察到的失败增补（公认）
  ```
  眼部特写推荐负面词组：
  asymmetrical eyes, wandering pupils, cross-eyed, half-closed eyes, eye flicker, lighting flicker
  ```
- **不要写**：抽象命令（"please keep realistic"）、与正面对冲突的词（正写浅景深就别负写 "blur"）（公认）
- **注意**：部分接口会把 "no blur" 里的 blur 当概念引入——逐条测试（经验/争议）
- 先修正面：负面提示词修不好超载的镜头设计——一镜只许一个主体、一个动作、一个运镜

### 三、图生视频（I2V）参数建议：运动越小越稳
| 参数 | 建议值 | 依据 |
|---|---|---|
| 运动幅度/动态强度 | 从最低档起测（subtle→medium→bold 三级阶梯，选第一个稳定的） | Quest Studio "稳定阶梯"工作流（经验，多模型通用） |
| 片段时长 | 眼特写 4-6 秒，上限 8 秒 | 10 秒+后段融化高发（经验） |
| 运镜 | 锁定镜头或缓慢推近（slow push-in）；禁 orbit/快速环绕 | 环绕迫使模型重建脸部 3D（公认） |
| 相机明确静止 | 必须明写 "the camera is entirely motionless"——不写≠静止，先验会自动加漂移 | Versely 实测（经验） |
| 源图要求 | 正面或 3/4 脸、双眼清晰无遮挡、光照均匀、中性表情起步 | 源图缺陷会被视频放大（Runway 官方指南，公认） |
| 事件密度 | 1 条片段 = 1 次眼动 + 0-1 次眨眼 | 多事件=瞳孔漂移主因（经验） |

### 四、可复制的防崩模板
```
模板A·最安全眼特写（图生视频）：
Close-up of [角色固定描述], eyes [颜色/形状锁定]. Action: one slow blink, gaze holds steady. Camera: entirely motionless, focus locked on eyes. Lighting: soft key light from frame left, consistent. Preserve: exact eye shape, eye spacing, iris color throughout the shot.

模板B·视线转移版：
Close-up of [角色]. Action: eyes lower to the letter in her hands for one beat, then return to the lens. One blink only. Camera: slow push-in, shallow depth of field. No head turn. No morphing.
负面：asymmetrical eyes, wandering pupils, eye flicker, morphing face, lighting flicker
```

### 五、修复决策（省额度）
```
崩几帧+靠近剪辑点 → 直接剪掉/B-roll 盖住（最便宜）
源图与镜头设计没问题+失败随机 → 固定全部输入重生成一次
整段都崩/需求本身高危（大转头+特写+说话+运镜） → 重设计镜头
拿到一帧稳定好图 → 导出当锚点，参考链（reference-chain）接下一次生成
```

## 备注
- 来源：Quest Studio《How to Fix AI Video Face Warping & Drift (7 Steps)》（首崩帧诊断、稳定阶梯、参考链）、HyperFrames《Negative Prompts for AI Video》（负面词规范）、Hailuo AI 知识页（Eye-Dart 问题=运动强度过高；10 秒+融化）、Kling 官博（"camera zooms in on the woman's eyes" 给模型明确目标）
- 确定性：运动负载与崩坏的因果关系、负面词写法规范=多源公认；具体秒数阈值（4-6 秒）=经验值，随模型版本浮动
- 争议：Kling 系社区有"动态权重调控+运动敏感度耦合"等进阶玩法（php.cn），属平台特定技巧，普适性待验
- 关联：163 翻车对照表（上游症状清单）、417 ★☆☆ 高危提示词的救火流程、419 景别选择（景别越大眼部容错越高）、254 动物待机微动（同样的低幅度哲学）
