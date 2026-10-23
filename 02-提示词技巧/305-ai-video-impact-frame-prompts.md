---
title: AI视频冲击帧提示词法——能与不能
category: 提示词技巧
tags: [冲击帧, AI视频, 提示词, Wan, H3, 生成边界]
source: 网络学习
created: 2026-10-16
updated: 2026-10-16
summary: 当前AI视频模型生成冲击帧的能力边界——提示词可诱导的类型、不可控的帧级精度、以及"生成端诱导+后期端保底"的双轨策略
related: [292, 305, 306, 141]
---

# AI视频冲击帧提示词法——能与不能

## 核心要点

- **帧级精度不可得**：当前视频模型无法保证"恰好1-2帧、恰好卡在接触点"——冲击帧的命根子AI给不了
- **可诱导的是"倾向"**：提示词能提高模型自发产生类冲击帧画面的概率，但位置/帧数/形态都不可控
- 结论：**生成端诱导＋后期端保底**双轨——能诱导出来的算赚到，决定性的冲击帧必须后期插入

## 详细内容

### 可诱导的提示词（提高自发概率）
```
正向：
- 命中瞬间画面闪烁：a brief white flash at the moment of impact
- 高对比爆闪：sudden high-contrast flash, screen burst of white light
- 反色倾向：colors invert for a split second on impact
- 漫画式拟声爆点：comic-style impact burst, radial speed lines explosion
```

### 诱导的局限（三不可控）
1. **帧位不可控**：闪光可能出现在挥拳中段而非接触帧
2. **帧数不可控**：可能连闪半秒（变成"频闪故障"而非冲击帧）
3. **形态不可控**：反色可能变成全局变亮/变暗，失去负片的锐利感

### 负向防护（防止模型乱闪）
```
负向：random flickering, strobe lights, screen glitch, frame tearing,
excessive flashing, unstable exposure, brightness pulsing
```
——不要冲击帧的镜头必须压死一切自发闪烁倾向，把"闪"的控制权全部留给后期

### 双轨工作流
| 轨道 | 做法 | 负责部分 |
|---|---|---|
| 生成端 | 提示词诱导+底片保持干净 | 意外之喜、氛围性微闪 |
| 后期端 | 单独生成/制作冲击帧静图，剪辑插入（306） | 所有决定性冲击帧 |

## 关键参数 / 模板 / 清单

**决策树**：这处冲击影响打击感成立吗→是：后期插入｜否，有更好：生成端诱导试试｜都不要：负向压死flickering

## 备注

- 与141-150（H3/Wan提示词体系）联用：本条是"特效帧"子类专项
- Wan 3.0的30s长镜头里模型自发闪烁概率更高——长镜头反而要更狠地压负向