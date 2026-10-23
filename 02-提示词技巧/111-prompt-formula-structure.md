---
title: 提示词公式化结构（七段式）
category: 提示词技巧
tags: [提示词, 公式, 结构, 视频, 图像]
source: 网络学习
created: 2026-10-13
updated: 2026-10-13
summary: 把散装脑洞压成公式=可控出图；场景+主体+动作+镜头+光影+风格+参数七段式
related: [087, 112, 113, 114, 115, 116, 117, 118]
---

# 提示词公式化结构（七段式）

## 核心要点
- 提示词不是写散文——是**填公式**
- 公式化=可复用、可调参、可迭代
- 七段式骨架：`场景 + 主体 + 动作 + 镜头 + 光影 + 风格 + 参数`
- 顺序有讲究：先主体动作（视频AI听不懂长句，先抓主语动词）
- 缺哪段=哪段交给AI瞎猜=翻车

## 三种公式层级（按工具）
```
基础公式（新手探索）：Subject + Setting + Style
进阶公式（出片）：Entity + Scene + Motion + Aesthetic + Stylization
大师公式（张力片）：场景 + 主体 + 动作 + 镜头 + 光影 + 风格 + 参数
```
- 视频 AI（Gen3/Kling/即梦）推荐**进阶公式**——Motion 单独成段
- MJ 关键帧推荐**大师公式**——镜头光影分离更可控

## 七段式详解

### 1. 场景（Scene）
- where：环境/地点/氛围基底
- 词例：`vast empty corridor` / `ruined cathedral at dusk` / `neon-soaked alley`
- 写法：形容词+名词，给空间感而非地标名

### 2. 主体（Subject/Entity）
- who/what：人物/物件/生物外观
- 词例：`a lone swordsman in tattered black kimono` / `a celestial fairy in tattered magnificent robes`
- 写法：年龄+材质+服装+特征，形容词堆叠给细节

### 3. 动作（Motion/Action）
- 动词：**现在时单动词最稳**——视频AI多动词会糊
- 词例：`drawing katana` / `walking away` / `turning head`
- 视频 AI 一句一个动作，别塞两条

### 4. 镜头（Camera）
- 景别+运镜+角度+焦段（详见 115 镜头词汇库）
- 词例：`low angle tracking shot, 35mm, slow dolly in`
- 顺序：景别→运镜→角度→镜头

### 5. 光影（Lighting）
- 光源方向+质感+色温（详见 116 光影词汇库）
- 词例：`single overhead light, high contrast, cold blue tone`
- 张力核心——见 016 光影张力

### 6. 风格（Style）
- 视觉锚点：胶片/画风/媒介
- 词例：`cinematic film still, anamorphic` / `anime keyframe, cel shading` / `ink wash painting`

### 7. 参数（Parameters）
- 比例/风格强度/参考/排除（详见 114 参数调优）
- MJ：`--ar 16:9 --style raw --sref [url] --no text`
- SD：`(masterpiece:1.2), (negative:1.4)` 权重语法

## 模板示例

### 张力关键帧（MJ）
```
[wide shot, low angle] + [lone figure in black] + [standing still] +
[vast empty corridor] + [single overhead light, cold blue] +
[cinematic film still, 35mm, anamorphic] + [--ar 16:9 --style raw --sref url]
```

### 视频动作段（Gen3/Kling）
```
Entity: a young samurai in white haori
Scene: misty bamboo grove at dawn
Motion: slowly drawing katana (one verb)
Aesthetic: golden volumetric light through mist
Stylization: anime keyframe, cinematic, 35mm
```

## 6 层约束栈（电影级）
```
Camera Angle 15%      景别/视角/构图
Lens & Camera 20%     机身/焦段/光圈/传感器
Lighting Physics 25%  光源/方向/色温/阴影
Subject & Env 20%     主体/环境/材质/道具
Texture & Stock 10%   颗粒/调色/瑕疵
Mood & Narrative 10%  情绪/叙事
```
- 权重总和=100%，光影占比最大（25%）——张力命脉

## 常见坑
- **写整段散文**：AI 抓不到主语动词→四不像
- **七段全堆**：超过 60 词 MJ 会忽略后半部分→精简
- **动作多动词**："drawing and slashing and jumping"→视频糊
- **缺光影段**：均匀光=无对比=无张力（最常见翻车）
- **参数乱加**：`--chaos 100` 同时 `--stylize 1000`→不可控

## 进阶
- **变量化模板**：把七段存成模板，替换变量复用
- **风格词固化**：全片同一组风格词+同一 `--sref`=统一（见 113）
- **分层提示**：复杂场景分多张关键帧，别塞一张图
- **词序调换测试**：主体放首位=主体强；风格放首位=风格强

## 备注
- 公式是骨架，不是束缚——熟练后可破格
- 视频 AI 公式 < 图像 AI 公式（视频听不懂太复杂的镜头语言）
- 6 层约束栈适合追求电影感的关键帧
- 关联：087 MJ 分镜、114 参数、115-118 词汇库
