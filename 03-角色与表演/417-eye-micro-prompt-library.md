---
title: AI 提示词眼部微动写法库——30+ 条情绪分组速查
category: 角色与表演
tags: [眼神, 提示词, 眼部微动, AI视频, 稳定性, 中英对照]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 眼部微动提示词按情绪分组的中英对照速查库：每条标注适用场景与 AI 生成稳定性评级，写物理动作不写情绪词
related: [163, 162, 165, 133, 027, 418, 419, 420, 421]
---

# AI 提示词眼部微动写法库

## 核心要点
- **写物理事件，不写情绪词**（公认）："sad" 返回训练集里所有悲伤脸的平均值（刻板脸）；写 "eyes lowered to the mug, one slow blink" 是可执行的几何指令。情绪词最多在句首放一个当上下文，之后全部写物理
- **命名画内目标优于命名方向**（公认/经验）："eyes fixed on the mug in her hands" 比 "looking down" 稳定——模型能解析物体，只能猜"下"是哪里
- **一条 5-6 秒片段只放 1 次视线变化**（经验）：多次眼动指令会导致瞳孔漂移 (wandering pupils) 与身份漂移
- **幅度控制词是稳定器**（公认）：slightly / barely / subtle / faint / a few degrees——不写控制词，模型默认拉满
- **稳定性评级**：★★★ 基本不崩 / ★★☆ 偶发崩坏 / ★☆☆ 高危（需抽卡）
- 关联：163 总纲、418 崩坏防治、420 情绪配方、421 对话节奏

## 详细内容

### A 组：平静·专注（基线态，全部 ★★★）
| 提示词 | 中文释义 | 适用场景 | 稳定性 |
|---|---|---|---|
| natural blinking | 自然眨眼（3-4秒一次） | 一切常态镜头打底 | ★★★ |
| slow blink every 5 seconds | 每5秒一次慢眨 | 沉静、疗愈氛围 | ★★★ |
| gaze fixed on [object] | 视线锁定某物 | 专注工作、凝视道具 | ★★★ |
| eyes following the [moving object] | 眼睛跟随运动物 | 看球、看雨、看飘雪 | ★★★ |
| steady gaze into the camera | 稳定直视镜头 | 独白、采访感 | ★★★ |
| looking just past the camera, screen left | 视线越过镜头略偏左 | 访谈、旁白陈述 | ★★★ |
| soft catchlight in eyes | 眼中有柔和高光点 | "活着"的视觉底线 | ★★★ |

### B 组：思考·回忆（★★★ 为主）
| 提示词 | 中文释义 | 适用场景 | 稳定性 |
|---|---|---|---|
| gaze drifts upward slowly | 视线缓慢上移 | 回忆、组织语言 | ★★★ |
| eyes unfocus slightly | 眼神微微失焦 | 走神、陷入思绪 | ★★★ |
| eyes lower for a beat, then return | 视线下垂一拍再回来 | 斟酌措辞、迟疑 | ★★★ |
| a single slow blink as she finishes the sentence | 说完一句时慢眨一次 | 台词节拍、冷幽默句号 | ★★★ |
| gaze shifts from the cup to the window | 视线从杯子移向窗 | 物到物的平滑转移 | ★★☆ |

### C 组：喜悦·温柔（★★★/★★☆）
| 提示词 | 中文释义 | 适用场景 | 稳定性 |
|---|---|---|---|
| softening around the eyes | 眼周放松柔和 | 欣慰、被打动 | ★★★ |
| eyes crinkle slightly at the corners | 眼角微微皱起 | 真笑（杜兴微笑标志） | ★★★ |
| glimmer in eyes | 眼中闪起微光 | 惊喜初现、心动 | ★★☆ |
| eyes brighten slightly | 眼睛微亮 | 听到好消息 | ★★☆ |
| pupils dilate slightly | 瞳孔轻微放大 | 渴望、看到在意的人 | ★★☆（仅特写有效） |
| eyes slightly wet, not crying | 眼眶微湿未哭 | 感动克制版 | ★★☆ |

### D 组：悲伤·疲惫（★★★/★★☆）
| 提示词 | 中文释义 | 适用场景 | 稳定性 |
|---|---|---|---|
| gaze slowly lowers | 视线缓缓下移 | 认输、悲伤、回避 | ★★★ |
| eyelids droop slightly | 眼睑轻微下垂 | 疲惫、醉意、慵懒 | ★★★ |
| distant gaze | 眼神飘远 | 麻木、出神 | ★★★ |
| eyes close for a beat, then open toward the window | 闭眼一拍再向窗睁开 | 释然、整理情绪 | ★★☆ |
| a tear wells up but doesn't fall | 泪在眶中不落 | 隐忍哭戏 | ★☆☆（泪液是高危元素） |

### E 组：愤怒·压迫（★★☆ 居多，易崩）
| 提示词 | 中文释义 | 适用场景 | 稳定性 |
|---|---|---|---|
| eyes narrow slightly | 眼睛微眯 | 起疑、威胁前奏 | ★★★ |
| unblinking stare | 不眨眼的盯视 | 压迫、对峙（张力天花板） | ★★☆（超5秒易蜡像） |
| gaze holds, no blink | 盯住不眨 | 支配、盯人压制 | ★★☆ |
| eyes lock onto the other person | 双眼锁死对方 | 对峙、杀意 | ★★☆ |
| pupils constrict | 瞳孔收缩 | 聚焦怒火 | ★☆☆（仅大特写可读） |

### F 组：恐惧·惊讶·紧张（★★☆/★☆☆ 高危区）
| 提示词 | 中文释义 | 适用场景 | 稳定性 |
|---|---|---|---|
| eyes widen slightly | 眼睛微微睁大 | 轻度惊讶（推荐用 slight） | ★★☆ |
| eyes dart to the door | 眼睛猛地瞟向门口 | 警觉、做贼心虚 | ★★☆ |
| rapid blinking | 快速连眨 | 紧张、撒谎、信息过载 | ★★☆（易过头变癫痫感） |
| eyes dart around the room | 眼睛四下乱扫 | 恐慌——**慎用** | ★☆☆（瞳孔漂移高发） |
| eye trembling / pupils trembling slightly | 瞳孔地震微颤 | 动漫式震惊 | ★☆☆（真人模型几乎必崩） |

### G 组：轻蔑·疯批·死人脸（★★★ 反差最稳）
| 提示词 | 中文释义 | 适用场景 | 稳定性 |
|---|---|---|---|
| one slow, deliberate blink | 一次刻意慢眨 | "我在听一个笑话" | ★★★ |
| eyes stay on the lens, no blink through the line | 盯镜头整句不眨 | deadpan 冷面 | ★★☆ |
| gaze slides away slowly | 视线缓缓滑开 | 轻蔑、懒得理 | ★★★ |
| eyes glance down, then back up | 向下瞟一眼再回 | 打量、评估对方 | ★★★ |

### 五要素公式（组装任何眼部指令，公认）
```
[状态 instant/slow/sustained] + [部位 eyes/lids/pupils] + [幅度 slightly/18%] + [时长 0.35s/one beat] + [过渡 then return]
例：slow blink (slow) with eyelids (部位) dropping halfway (幅度) for one beat (时长), then eyes lift back to the lens (过渡)
```

### 组合范例（可直接抄）
```
冷静观察："eyes fixed on the chessboard, natural blinking, soft catchlight in eyes"
心动瞬间："glimmer in eyes, pupils dilate slightly, eyes soften, one slow blink"
压抑愤怒："eyes narrow slightly, unblinking stare, jaw tight, gaze locked on the other person"
心虚撒谎："rapid blinking, eyes dart to the left for a beat, then return near the camera"
冷面毒舌："one slow, deliberate blink, gaze slides away slowly, mouth stays neutral"
```

## 备注
- 核心来源：Versely《Directing gaze and micro-expression on a face》（写物理不写情绪、画内目标论）、Aivon Hashnode 微表情完全指南（五要素公式、六情绪模板）、Naviya 微表情提示词指南（gaze 风险清单、景别配对）
- 确定性分级：写物理动作/幅度控制词/单条眼动=多源公认；瞳孔级描述仅特写有效=经验共识；eye trembling 在真人模型必崩=经验（动漫模型可用）
- 争议：部分中文模型对中文提示词响应更弱（Aivon 认为英文更稳），实测因模型而异—— Seedance/Kling 中文可用但英文一致性更高
- 关联：163 眨眼/眼跳/瞳孔三重奏（本库是三通道的落地词典）、418 崩坏防治（★☆☆ 条目的救火手册）、420 七态配方（情绪维度重组本库）、421 对话戏节拍（眨眼/凝视的时序编排）
