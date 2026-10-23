---
title: 情绪七态眼神配方——眨眼×眼跳×瞳孔×眼睑四通道对照
category: 角色与表演
tags: [情绪, 眼神, 四通道, 配方表, 提示词, FACS]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 喜/怒/哀/惧/惊/厌/蔑七种情绪在眨眼频率、眼跳方向、瞳孔、眼睑高度四个通道上的配方对照表，每态配一条可直接复制的整段提示词
related: [163, 162, 161, 165, 164, 417, 418, 419, 421]
---

# 情绪七态眼神配方

## 核心要点
- **四通道配方法**（经验整合）：任何情绪的眼神都可拆成 ①眨眼频率 ②眼跳方向 ③瞳孔 ④眼睑高度——四通道同向叠加=标准情绪，矛盾对位=复杂情绪（164）
- **瞳孔只随唤醒度走，不分正负**（公认）：恐惧/愤怒/兴奋/爱慕都放大（交感神经），平静与低唤醒才缩小——瞳孔放大≠喜欢，只="上头"
- **眼睑高度是最稳的情绪轴**（经验）：上眼睑抬高=惧/惊，压低=哀/蔑/疲，收紧=怒——AI 模型对 lid 指令响应比 pupil 指令稳定得多
- **眼跳方向给叙事**（163）：下=哀/愧，上=回忆/翻白眼，锁死=怒/专注，扫描=惧/焦虑
- 写提示词时四通道最多写 2-3 条，写满=超载崩坏（417/418）
- 关联：161 AU 系统、162 微表情、417 词库、419 景别带宽

## 详细内容

### 一、七态四通道对照表
| 情绪 | ①眨眼频率 | ②眼跳方向 | ③瞳孔 | ④眼睑高度 | 关键辅证 |
|---|---|---|---|---|---|
| 喜 | 正常或柔和双眨（真笑想到幸福事会眨眼） | 柔和、愿意停在对方脸上 | 轻微放大、眼亮 | 下眼睑上提、眼角皱（杜兴标志） | 假笑眼角无皱纹（公认） |
| 怒 | 眨眼受抑、瞪视不眨 | 锁死目标不动 | 中度放大（神经学）* | 上眼睑收紧、眉下压聚拢 | 鼻翼扩张、下颌紧 |
| 哀 | 慢眨增多 | 下移或失焦 | 中性或轻放大、黯淡 | 上眼睑下垂遮瞳，内眉上挑 | 泪膜增厚、眶微红 |
| 惧 | 冻结不眨→应激后连眨 | 大幅扫描或僵住（scanning or frozen） | 强放大（可达45%） | 上眼睑抬到最高、露上眼白 | 眉抬且聚拢、面白 |
| 惊 | 瞬间定格→一次快眨 | 瞬间锁定刺激源 | 0.3秒内快速放大 | 上眼睑快速抬高、眉全抬 | 真惊讶持续<1秒（PMC 公认），拖长=假 |
| 厌 | 正常或一次慢眨 | 从目标滑开或下瞟 | 轻微收缩 | 下眼睑上抬挤压、眉轻压 | 鼻梁皱、上唇提（AU9/10） |
| 蔑 | 一次刻意的慢眨（招牌） | 居高临下斜瞟→滑开 | 中性偏小 | 眼睑半垂（half-lidded） | 单侧嘴角、下巴微抬 |

\* 怒的瞳孔存在争议：神经学测量为中度放大（高唤醒），中文科普多写"收缩聚焦"——写提示词建议避开怒+瞳孔的组合，用眼睑收紧表达。

### 二、每态整段可复制提示词（CU 景别，5 秒模板）
```
喜：Close-up, camera motionless. Her eyes soften, lower eyelids lifting, faint crinkles at the outer corners, pupils bright with a soft glimmer. One gentle double-blink as the smile arrives. Warm key light from frame left, soft catchlight in eyes.

怒：Close-up, camera motionless. His brows press down and together, eyelids tightened, eyes locked on the other person without blinking. Jaw set. Hard light from frame right, high contrast. No head turn.

哀：Close-up, camera motionless. Her inner brows rise, upper eyelids droop covering part of the iris, gaze drifts downward and unfocuses. One slow blink, eyes slightly wet, not crying. Cool soft light.

惧：Close-up, camera motionless. Her eyes snap wide, upper eyelids fully raised showing the white above the iris, pupils dilate fast. Frozen, no blink for two seconds, then rapid blinking as she scans left. Cold light from below.

惊：Close-up, camera motionless. His brows shoot up, eyes widen in an instant, pupils expand. A beat of stillness, one quick blink, then the face relaxes back. Soft even light.

厌：Close-up, camera motionless. Her lower eyelids rise slightly, brows press down a touch, gaze slides off the object and away to frame right. One slow dismissive blink. Neutral light, shallow depth of field.

蔑：Close-up, camera motionless. Half-lidded eyes look down at him, chin slightly raised. One slow, deliberate blink, then her gaze slides away like he isn't worth holding. Mouth neutral.
```

### 三、配方使用规则
1. **挑 2-3 通道写，留白给模型**（417）：全写满=指令超载
2. **惊态计时最短**（公认）：真惊讶 0.2-1 秒，之后必然转入其他情绪——提示词里用 "a beat of stillness, then..." 写回落
3. **哀与蔑共用眼睑下垂**，靠眉毛区分：哀=内眉上挑，蔑=眉平或轻压
4. **惧与惊共用瞪眼**，靠眨眼区分：惧=持续冻结+扫描，惊=快速回落
5. 复杂情绪=两态配方对位（例：喜的眼睑+哀的视线=苦笑），见 164

## 备注
- 来源：NeuroLaunch 情绪眼型矩阵（悲/怒/惧/焦虑/羞耻的眉睑-瞳孔-视线三列数据）、温州七医《眼睛：心灵之窗中的情绪密码》（惧 45% 瞳孔、喜的下眼睑上提）、PMC 真/假惊讶时序研究（AU1+2+5，真惊讶短暂）、乔·纳瓦罗肢体语言科普（瞳孔不可控）
- 确定性：瞳孔=唤醒度、杜兴微笑眼角、惊讶<1秒=公认；七态的眨眼频率行=表演教学经验值（量化数据少）
- 争议：怒的瞳孔方向（放大 vs 收缩）两派都有来源，实操建议绕开
- 关联：163 三通道理论底座、161 AU 编号（AU1/2/4/5/9/10）、164 复杂表情、417 稳定性评级（本表 blink/gaze 词全部 ★★★，pupil 词 ★★☆ 限特写）、419 各景别能读哪几通道、421 对话戏中的情绪转换节拍
