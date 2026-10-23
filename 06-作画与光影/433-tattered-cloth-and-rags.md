---
title: 破损与破布条动态
category: 作画与光影
tags: [布料物理, 破损动画, 流苏, 破边, 战损表现, 提示词]
source: 网络学习
created: 2026-10-20
updated: 2026-10-20
summary: 破边、撕裂、流苏、补丁的风动态规律，破布条摆动频率与风速长度的关系，战斗中布条脱落的帧级描写。
related: [432, 434, 435, 436, 406, 074, 238, 225]
---

# 破损与破布条动态

## 核心要点

1. **破边频率公式（公认）**：破布条摆动频率 f ≈ St × U / L，其中 St（Strouhal 数）≈ 0.2-0.3（柔性布条典型值），U 为风速（m/s），L 为布条自由长度（m）。即频率与风速成正比、与长度成反比。
2. **流苏/须条近似单摆（公认）**：流苏可近似为下端集中质量的单摆，周期 T = 2π√(L/g)，L 为流苏长度，g=9.8。短流苏（10cm）周期约 0.6s → 摆得快；长流苏（50cm）周期约 1.4s → 摆得慢且稳。
3. **破边多层动态（经验）**：撕裂边缘的纤维须（1-5cm 长）受风影响极敏感（高频抖动，8-15Hz），主撕裂口边缘（10-30cm）以 1-4Hz 摆动，大块悬垂破布（>50cm）以 0.3-1Hz 缓慢摆动。三层节奏叠加产生丰富感。
4. **补丁的刚性差（经验）**：补丁（尤其是皮革/金属补丁）比周围布料更硬、更重，摆动幅度小，周期长，补丁边缘与布料连接处有应力褶皱。
5. **风阻力增加（公认）**：破损布料的粗糙边缘使空气阻力系数 C_d 增加 20-50%，相同风速下整体摆幅略大于完好布料（因阻力大，风更容易"抓住"布料）。
6. **战斗中脱落（经验）**：布条脱落分为预撕裂（纤维已松、摆动中有细微分离）→ 临界撕裂（纤维被拉到最大张力、某一瞬间断裂）→ 自由落体（脱落瞬间具有身体运动的动量，做抛物线运动）三个阶段。
7. **陈旧破损与新鲜撕裂（经验）**：旧伤边缘纤维已被风反复拉直，呈毛躁但"驯服"的状态（边缘纤维方向一致，随风轻轻摆）；新伤纤维收缩蜷曲，呈炸裂感（边缘纤维方向紊乱、有向外张力）。

## 详细内容

### 破布条频率计算表

假设 St ≈ 0.25（柔性布条典型值），f ≈ 0.25 × U / L

| 风速 U | 布条长度 L | 摆动频率 f | 视觉效果 | 确定性 |
|--------|-----------|-----------|---------|--------|
| 微风 2 m/s | 0.5m | 1.0 Hz | 每秒摆一次，缓慢优雅 | 公认 |
| 微风 2 m/s | 0.2m | 2.5 Hz | 每秒 2.5 次，轻快 | 公认 |
| 强风 10 m/s | 1.0m | 2.5 Hz | 大风中长布剧烈摆 | 公认 |
| 强风 10 m/s | 0.1m | 25 Hz | 短纤维须高频抖动（肉眼感知为颤振） | 公认 |
| 飓风 30 m/s | 0.5m | 15 Hz | 破边疯狂抽打 | 公认 |

**Strouhal 数说明**：St 无量纲，不同文献取值略有差异（0.2-0.35），动画中统一取 0.25 即可。风洞实验（Virot et al., JFS 2013）确认 St 对柔性旗帜约 0.15-0.3，薄布条接近 0.25。

### 流苏周期计算表（单摆近似）

T = 2π√(L/g)，g = 9.8 m/s²

| 流苏长度 L | 周期 T | 频率 f | 视觉效果 |
|-----------|--------|--------|---------|
| 5cm（短穗） | 0.45s | 2.2 Hz | 快速小幅度摆动 |
| 15cm（中穗） | 0.78s | 1.3 Hz | 中等速度 |
| 30cm（长穗） | 1.1s | 0.9 Hz | 缓慢大弧度摆 |
| 50cm（超长穗） | 1.4s | 0.7 Hz | 厚重感强 |

注意：流苏下端有重量时周期会略有偏差，但单摆近似对动画足够。

### 战斗布条脱落——帧级描写（以 24fps 动画为例）

| 帧 | 阶段 | 画面描述 | 确定性 |
|----|------|---------|--------|
| N-8 ~ N-3 | 预撕裂 | 布条纤维被拉扯，出现细小裂纹；正常摆动中夹杂细微纤维分离 | 经验 |
| N-2 ~ N | 临界点 | 纤维张力拉满，某根纤维先断；断裂产生冲击波使附近纤维瞬间全断（时间 < 1 帧） | 经验 |
| N+1 | 刚脱落 | 布条仍保持被拉扯的瞬间形状，惯性使其延续原运动方向 | 公认 |
| N+2 ~ N+5 | 自由抛物线 | 布条受初始速度 + 重力 + 风作用，做抛物线飘出；此时布条恢复柔性、开始随风摆动 | 公认 |
| N+6 ~ N+24 | 飘落 | 摆动幅度随空气阻尼衰减，落到地面或被风卷走 | 公认 |

### AI 视频提示词（中英对照）

#### 场景：风中破袍（三层动态）

```
[中文提示词]
破旧红色僧袍在强风中飘扬。袍缘破损撕裂成三层：最外层是5厘米长的白色纤维须，高频快速抖动如蝴蝶翅膀；中间层是20厘米长的撕裂缝口，以中等节奏摆动；内层是1米长的垂挂破布条，缓慢沉重地左右横扫。补丁是深色皮革，比布料硬，摆幅小但周期长。背景是荒漠，天空昏暗有沙尘。电影画面，动态捕捉级布料。

[English Prompt]
Tattered red monk robe billowing in strong wind. Hem torn into three layers: outermost 5cm white fiber tassels flutter at high frequency like butterfly wings; middle layer 20cm tear gaps swing at medium rhythm; innermost 1m long hanging rags sweep slowly and heavily left and right. Dark leather patches stiffer than fabric, smaller swing amplitude but longer period. Desert background, dim dusty sky. Cinematic footage, motion-capture level cloth dynamics.
```

#### 场景：战斗中布条脱落

```
[中文提示词]
剑客与敌人激战中，左肩外袍被剑气划过。慢镜头展示：先看到纤维被拉得根根分明，瞬间全部断裂；脱落的布料碎片带着挥剑的惯性向右飞出，同时开始在空中随风轻摆，像一只被惊起的小鸟。背景是飞溅的剑光和落叶。动态捕捉级布料撕裂效果，电影慢镜头（120fps→24fps）。

[English Prompt]
Swordsman in battle, left shoulder robe torn by sword slash. Slow motion: fibers stretch visibly then snap all at once; torn cloth fragment flies right with sword-swing inertia, begins fluttering in air like a startled bird. Background of sword sparkles and falling leaves. Motion-capture level cloth tearing, cinematic slow motion (120fps to 24fps).
```

#### 提示词稳定性技巧

| 技巧 | 说明 | 确定性 |
|------|------|--------|
| 指定层数 | 明确写 `three-layer tear: 5cm fibers / 20cm gaps / 1m rags` 给 AI 清晰层次 | 经验 |
| 给频率参照 | `flutters like butterfly wings`（高频参照）比单纯写 `flutters fast` 稳定 | 经验 |
| 避开矛盾 | 破损严重的衣服不要同时写 `sleek elegant movement`（破损使运动更混乱） | 公认 |
| 补丁材质对比 | `leather patch stiffer than surrounding cotton` 明确材质差 | 经验 |

## 备注

- 关联 [432-沾水与潮湿]：湿布破损时纤维粘连，撕裂不如干布"炸"，脱落也更沉重。
- 关联 [238-动作戏视角×服装矩阵]：战斗中布条脱落的视觉节奏与镜头运动速度互补——慢镜头中布条自然摆动填补张力。
- 物理来源：Strouhal 数用于布料的文献（Dynamics of flags over wide ranges of mass and bending stiffness, arXiv 2106.14988；Fluttering flags, Virot et al., JFS 2013）。
- 争议点：St 的精确取值不同实验差异较大（0.15-0.4），动画创作取 0.25 为通用值。
