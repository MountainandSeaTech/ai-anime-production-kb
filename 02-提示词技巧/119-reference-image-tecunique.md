---
title: 参考图与垫图技法（图生视频/角色锁定/构图锁）
category: 提示词技巧
tags: [提示词, 参考图, 垫图, 图生视频, ControlNet, IP-Adapter, WAN3]
source: 网络学习
created: 2026-10-13
updated: 2026-10-13
summary: 参考图是控制AI最硬的手段；sref/cref/ControlNet/IP-Adapter/LoRA 分工
related: [087, 088, 113, 114, 120]
---

# 参考图与垫图技法

## 核心要点
- 提示词是"说"——参考图是"指"，指比说准十倍
- 五大参考图手段：**sref 风格 / cref 角色 / ControlNet 结构 / IP-Adapter 风格化 / LoRA 训练**
- 分工：sref/cref 是 MJ 专利；ControlNet/IP-Adapter 是 SD 系；LoRA 是训练
- 动漫短剧一致性的核心=图生视频链路（MJ出帧→视频AI动起来）

## 五大手段分工

```
--sref (MJ)        锁风格：色/质/光/构图氛围
--cref (MJ)        锁角色：脸/发/衣
ControlNet (SD)   锁结构：姿势/构图/边缘/深度
IP-Adapter (SD)    风格化参考：类似 sref 但更灵活
LoRA (SD)          训练定制：角色/画风（最稳但需训练）
```

## MJ 参考图（见 113 详解）
```
--sref [url] --sw 200      风格参考
--cref [url] --cw 100       角色参考
```
- 参考图优先用 MJ 自出图
- 角色 60%+ 占画面、正面、光线干净

## SD 系 ControlNet 详解

### 主流 ControlNet 类型
```
OpenPose            姿势锁（骨骼关键点）
Depth               深度图（远近层次）
Canny               边缘检测（精确轮廓）
Lineart             线稿
SoftEdge            软边缘
Normal              法线贴图（3D 表面）
Scribble            涂鸦
Tile                分块重构（放大用）
```

### 选用决策
```
锁姿势/动作     → OpenPose
锁构图/远近     → Depth
锁精确轮廓       → Canny / Lineart
锁 3D 表面       → Normal
```

### ControlNet vs IP-Adapter
- **ControlNet**：锁**结构**（姿势/构图）——"摆这个 pose"
- **IP-Adapter**：锁**风格/脸**（注入特征向量）——"用这张脸"
- 二者可同时用=姿势+风格+脸全锁

## IP-Adapter 进阶
```
IP-Adapter FaceID    脸部 ID 注入
InstantID            身份锁定（人脸专用）
PuLID                脸部 ID（FLUX 系）
Reference-only       仅参考（不训练）
```
- IP-Adapter 是 SD 系最接近 MJ --cref 的等效物

## LoRA 训练（最强一致性）
- 训练角色 LoRA：100-500 张该角色图
- 训练画风 LoRA：30-100 张目标画风图
- 调用：`(lora_name:0.7)` 权重 0.6-0.8 推荐
- 训练耗时但一致性最高

## 图生视频链路（动漫短剧核心）

### 标准链路
```
1. MJ 出角色定妆图（cref 池）
2. MJ 出场景关键帧（sref 锁风格 + cref 锁角色）
3. 关键帧喂 Gen3/Kling/即梦 图生视频
4. 拼接剪辑（见 090）
```

### 链路要点
- **顺序不能反**：先动后调=崩；先图后动=稳
- **关键帧要干净**：崩坏帧喂视频AI=崩坏放大
- **同 sref + 同 cref 全片复用**=统一
- **多 seed 抽张力最强帧**再喂视频AI

## 角色锁定验证闭环
```
生成 → 2. 对比 DNA（脸/发线/饰物/服装色） →
3. 若 ≥2 锚点漂移 → 提高参考权重并重附同参考 →
4. 同 seed/session 重投 →
5. 3 次仍漂移 → 加 OpenPose 或换 cref 图
```
- DNA 锚点：脸型 + 发色 + 标志饰物 + 服装主色
- 4 锚点对得上=角色锁成功

## 参考图选择原则
1. **MJ 自出图优先**——训练分布对齐
2. **角色占画面 60%+**
3. **正面/45度侧**——别用大侧面
4. **光线干净单一**——别逆光剪影做 cref
5. **背景简洁**——别污染识别
6. **同分辨率同风格**——多参考图要风格统一

## 常见坑
- **用网图做 cref**：识别差→变脸
- **ControlNet 权重太高**：>1.5→画面僵硬像贴图
- **IP-Adapter + ControlNet 冲突**：同时强权重→互打架
- **图生视频大改提示词**：视频AI按图生成——提示词改太多=图与词矛盾→崩
- **同角色不同场景换 cref**：每场景换参考=角色变——一角色一张 cref 全片用

## 进阶
- **角色定妆集**：每角色出 5-8 张定妆图做 cref 池
- **场景定妆集**：每场景出 1 张构图定妆图做 ControlNet 构图锁
- **多 ControlNet 叠加**：OpenPose + Depth=姿势+构图双锁
- **风格图库**：按情绪分类的风格图池（冷峻/温暖/水墨/赛博）

## 备注
- 提示词是说，参考图是指——指比说准
- MJ 用 sref/cref，SD 用 ControlNet/IP-Adapter
- 图生视频是动漫短剧一致性的核心链路
- 关联：087 MJ分镜、088 角色一致性、113 风格锁定、120 避坑调试

## WAN3.0 校准（2026-10-20）
WAN3 10 图+5 视频+5 音频=20 件多模态参考上限
