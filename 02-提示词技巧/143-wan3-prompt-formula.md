---
title: Wan3.0提示词公式（官方结构与分镜写法）
category: 提示词技巧
tags: [Wan, 万兴, 提示词公式, 文生视频, 阿里, WAN3]
source: 网络学习
created: 2026-10-13
updated: 2026-10-20
summary: Wan系公式=主体+场景+运动；进阶版加镜头/光影/氛围；3.0支持分镜式Shot写法
scope: WAN3.0 文生视频/图生视频提示词写法（主体+运动+场景+镜头/光影/氛围）
validated_on: WAN3.0（阿里云百炼 2026-10-15）
related: [111, 142, 144, 146, 148]
---

# Wan3.0提示词公式

## 核心要点
- Wan（阿里万相）官方公式：**主体（主体描述）+ 场景（场景描述）+ 运动**
- 进阶公式：**+ 镜头语言 + 光影 + 氛围**
- Wan 3.0特性：支持**分镜式多Shot写法**和**音频描述**
- Wan 3.0 **单次生成最长 30s**（分镜式多 Shot 的时间码总和也在 30s 内）
- 与H3差异：Wan用自然语言写运镜，H3用[指令]——两套语法别混
- 关联 111 公式化结构、142 H3结构对比

## 公式详解

### 基础公式
```
提示词 = 主体(主体描述) + 运动 + 场景(场景描述)
```
- 主体：人/动物/物体+外貌细节（发型/服饰/姿态，多短句列举）
- 运动：主体运动+非主体运动（静态/小幅度/大幅度写清楚）
- 场景：背景+前景，写实或幻想空间

### 进阶公式
```
提示词 = 主体 + 运动 + 场景 + (镜头语言 + 光影 + 氛围)
```
- 镜头语言：景别+视角+运镜（自然语言："镜头缓缓左移"）
- 光影：光源/光质/时间
- 氛围：情绪词+风格词

### Wan 3.0 完整公式（官方推荐）
```
[Shot Type] of [Subject + Appearance], [Action], [Setting + Lighting].
Camera [Movement]. [Audio description]. [Style note].
```
- 5行结构：镜头/动作/运镜/音频/风格各占一行
- 音频描述独立成行=3.0原生支持音画同构

## 分镜式写法（Wan 3.0杀手锏）

### Shot格式
```
Shot 1 [0-2s]: 画面描述。Camera: 运镜。
Shot 2 [2-4s]: 画面描述。Camera: 运镜。
Shot 3 [4-7s]: 画面描述。Camera: 运镜。
```

### 官方示例风格
```
Shot 1 [0-2s]: A panoramic view of a hanging garden in a futuristic city,
  with floating plants swaying in the breeze.
Shot 2 [2-4s]: A robot gardener meticulously prunes the plants.
Shot 3 [4-7s]: Sunlight breaks through clouds, illuminating the garden.
```
- 每个Shot带**时间码**=镜头节奏显式控制
- 单提示词生成多镜头=短剧雏形一次成型

### 分镜写法要点
```
1. 时间码递增且连续（0-2/2-4/4-7）
2. 每Shot一个核心动作（关联146单一动作）
3. 运镜用自然语言（"camera moves left"）不用方括号
4. Shot间状态延续词复用（同一角色描述每Shot重写）
```

## 运镜的自然语言写法（Wan系）

### 官方认可写法
```
"The camera moves left, slowly panning across…"
"camera gradually rises from eye level to top-down view"
"camera dollies backward and tilts up to reveal…"
```
- 复合运镜可以写：dolly + tilt组合=官方示例常见
- 写**运镜的目的**（to reveal…）比只写动作响应好

### 与H3指令对照表
| Wan自然语言 | H3指令 |
|---|---|
| camera pushes in | [Push in] |
| camera pulls back | [Pull out] |
| camera moves left | [Truck left] |
| camera tilts up | [Tilt up] |
| camera orbits | [Orbit left/right] |
| static shot | [Static] |

## 首尾帧写法（Wan特色）

### 首尾帧差异大时必须写过渡
```
官方建议：首尾帧主体/场景差异大时，描述过渡过程：
"A small black cat looks up at the sky curiously.
 The camera gradually rises from eye level and finally
 captures its curious gaze from a top-down view."
```
- 写清**怎么从首帧到尾帧**=过渡由你导演，不由AI乱猜
- 关联 144 首尾帧详解

## 模板示例

### 基础版（单镜）
```
"红衣女子在沙漠中奔跑，长发与裙摆向后飞扬。
 场景：黄昏沙漠，远处孤山。
 镜头从侧面跟拍，camera tracks alongside。
 金色逆光，沙尘在光中闪烁。史诗孤独氛围。"
```

### 分镜版（3镜短场景）
```
Shot 1 [0-2s]: 红衣女子站在沙丘顶，远眺。
  Camera: static wide shot。风声。
Shot 2 [2-4s]: 她转身向镜头跑来，裙摆飞扬。
  Camera: tracking shot following her。脚步踩沙声。
Shot 3 [4-6s]: 她冲过镜头，裙摆扫过画面。
  Camera: low angle, she passes over camera。风声渐强。
```

### 完整 30s 戏剧节拍示例（WAN3.0 原生上限）
```
Shot 1 [0-5s]: 建压——雨夜竹林远景，剑客缓步入画，每步地面微震。
  Camera: slow dolly in from wide to medium。Audio: 雨声，竹叶沙沙。
Shot 2 [5-10s]: 推近——剑客停步，抬头望向对侧（Off-screen），眼神微变。
  Camera: push in to close-up。Audio: 雨声渐弱，风声突起。
Shot 3 [10-12s]: 爆点——一道黑影从侧方扑来，剑客拔刀半寸格挡。
  Camera: fast tilt up + shake。Audio: 金属出鞘+碰撞。
Shot 4 [12-18s]: 拉锯——两招快速过刃，各退三步，眼神锁定。
  Camera: orbit around both fighters。Audio: 急促脚步，刀光破空。
Shot 5 [18-22s]: 蓄势——双方面对面僵持，雨打在肩上，静默 4 秒。
  Camera: static two-shot, slow push。Audio: 只剩雨声，心跳声隐约。
Shot 6 [22-26s]: 决胜负——剑客拔刀斩落，对手侧闪，刀光过处雨水分两半。
  Camera: lateral tracking fast。Audio: 斩风声，闷响。
Shot 7 [26-30s]: 收束——对手单膝跪地，收刀入鞘，雨停，远处钟声。
  Camera: slow pull back to wide。Audio: 钟鸣，余雨滴水声。
```
- 7 镜 × 4.3s 平均 = 30s 刚好卡满原生上限
- 戏剧节拍：建压→推近→爆点→拉锯→蓄势→决胜负→收束（完整七拍）
- 每个 Shot 带音频描述=WAN3 原生音画一次出

## WAN3.0 多模态参考（2026-10-20 新增）

WAN3 支持 **10 图 + 5 视频 + 5 音频 = 20 件**参考素材同时输入，是一致性革命。

### 推荐参考组合
| 参考类型 | 数量 | 用途 | 示例 |
|---|---|---|---|
| 角色设定图 | 3-5 张 | 锁脸/锁服装/锁姿态 | 正面/侧面/背面三视图 + 情绪变体 |
| 场景参考图 | 2-3 张 | 锁环境风格/时间/光线 | 清晨/黄昏/夜景各一张 |
| 道具参考图 | 1-2 张 | 锁武器/配饰形态 | 刀身反光细节 + 刀柄缠绕 |
| 风格参考图 | 2-3 张 | 锁画风/色调/颗粒 | 目标作品截图/自制风格板 |
| 视频参考 | 1-2 个 | 锁动作节奏/运镜范式 | 同类型打戏片段/参考运镜 |
| 音频参考 | 1-2 个 | 锁氛围/节奏 | 目标 BGM 片段/环境音 |

### 多模态参考冲突解决
- 角色图 > 场景图 > 风格图：优先级递减
- 多张角色图必须**同一角色不同姿态**，不能混入其他角色
- 视频参考 ≤5s/个，长了模型只取前 3s 有效帧
- 音频参考建议用 BGM 片段，效果比纯音效好

## 本地编辑（WAN3.0 独有）

WAN3 支持选时间段→改提示词→局部替换，不需要整条重生。

### 操作流程
```
1. 生成 30s 完整段 → 回放定位出错段落（如 Shot 3 动作崩了）
2. 选中出错时间段（如 10-12s）
3. 只改该段的提示词（其他 Shot 不动）
4. 提交局部替换 → 保留其余部分，只重生选中段
```

### 适用场景
- 长段后段漂移（20-30s 段人物/场景变了）
- 单个 Shot 动作/运镜不满意
- 音画对不上（只改音频描述）

### 成本与时间
- 局部替换按选中时长计费，不浪费整条成本
- 重生速度比整条快 60-70%（只算选中段）

## 常见坑
- **H3语法混用**：Wan里写[Push in]=可能不识别——Wan用自然语言
- **分镜时间码重叠**：Shot1 0-3s，Shot2 2-5s=时间逻辑混乱
- **Shot间状态断裂**：Shot1红衣Shot2变白裙——每Shot重写角色锚
- **运镜无目的**："camera moves"不写到哪去=AI乱移
- **单Shot多动作**：一个Shot里"跑+跳+转身"=动作糊

## 进阶
- **提示词扩写**：短提示词（"小猫玩雪球"）可让系统自动扩成结构化长描述=先扩写再手动精修
- **公式喂给LLM**：把公式作为system message给qwen等模型=批量生成Wan格式提示词
- **音效行独立**：3.0把audio description单独成行=声音参与构图（关联151音画）
- **风格词尾部**：style note放最后=不干扰主体描述

## 备注
- Wan公式：主体+场景+运动（+镜头+光影+氛围）
- 3.0杀手锏：分镜式Shot [时间码]写法+音频行
- 运镜用自然语言+写明目的
- 关联：142 H3结构、144 首尾帧、148 多镜头分镜、146 通用原则
