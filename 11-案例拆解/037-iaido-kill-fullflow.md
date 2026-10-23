---
title: 居合斩杀全流程拆解
category: 案例拆解
tags: [张力, 居合, 全流程, 拆解, 综合案例, WAN3]
source: 拆解
created: 2026-10-13
updated: 2026-10-13
summary: 居合斩杀是张力工艺集大成者，从待机到收刀全流程串联前29条技法
related: [011, 014, 025, 026, 030, 032, 034]
---

# 居合斩杀全流程拆解

## 核心要点
- 居合斩杀是动漫短剧**张力工艺的集大成者**——一条戏串联前 29 条技法
- 骨架：待机（025）→前摇（026）→停顿（029）→爆发峰值→收刀定格
- 全程以静态张力（012）为主，爆发仅 0.3s，比例 6:1:3（014）
- 本条是"毕业案例"，把零散技法缝成完整流程

## 全流程镜表（参考时长 6s）

| 镜号 | 时码 | 时长 | 镜头 | 景别角度 | 角色 | 动作 | 音频 |
|---|---|---|---|---|---|---|---|
| 001 | 0-1.5s | 1.5s | static | 近景平视 | 主角 | 居合站姿（025） | 低频drone渐强（034） |
| 002 | 1.5-2s | 0.5s | slow push in | 大特写平视 | 手 | 手搭刀柄（026） | 节奏加密 |
| 003 | 2-2.4s | 0.4s | static | 大特写 | 手 | 指节发白（030） | 渐强到顶 |
| 004 | 2.4-2.7s | 0.3s | static | 大特写 | 眼 | 瞳孔收缩+屏息（024） | 全静默（033） |
| 005 | 2.7-3s | 0.3s | static | 特写升格2x | 主角 | 出刀瞬间（021） | 重拍+刀声炸响（034） |
| 006 | 3-3.3s | 0.3s | static | 特写 | 敌人 | 中刀 | 中刀声 |
| 007 | 3.3-4.5s | 1.2s | slow pull back | 全景平视 | 主角 | 收刀背身定格（029） | 太鼓余响渐弱 |

## 张力曲线映射（014）
```
Build-up（0-2.7s，4镜）：待机→手搭→指节白→屏息，蓄势 4.5/6=75%（略超6:1:3，可调）
Peak（2.7-3.3s，2镜）：出刀+中刀，0.6s，最短
Release（3.3-4.5s，1镜）：收刀定格拉远，1.2s
```

## 三轴检查（013）
- 时间轴：蓄势 2.7s→爆发 0.3s，延迟释放到位
- 空间轴：近景对峙→大特写手/眼（注意力压缩）→全景拉远（释放）
- 心理轴：观众知主角会赢+角色知代价=揪心

## 静动结构（012）
- 全段 5/7 镜是 static 固定机位，仅 002/007 缓推/缓拉
- 爆发镜（005）也是 static+主体动=固定机位爆发力最强（018）
- 静→静峰→动→静，四段式

## 关键技法串联
- 025 待机姿势：001 居合站姿
- 026 动作前摇：002-004 手搭→指白→屏息四段递进
- 030 手部细节：003 指节发白
- 024 微表情：004 瞳孔收缩+屏息
- 029 停顿：007 收刀定格余韵
- 021 升格：005 出刀 2x 慢镜
- 018 镜头运动：仅缓推/缓拉，峰不动
- 032 硬切：004→005 静默到爆的硬切
- 033 静默：004 全静默 0.3s 接爆点
- 034 BGM：低频渐强→静默→重拍+刀声
- 036 闪（可选）：005 出刀可叠闪白 0.1s 增爆

## AI 生成提示词（按镜）
- 001：`iaido stance, side-on, hand near sword hilt, blade sheathed, low center of gravity, tense, static shot, medium close-up`
- 002：`extreme close-up of hand slowly moving to sword hilt, slow push in, shallow depth of field`
- 003：`macro close-up of white knuckles gripping hilt, intense grip, static`
- 004：`extreme close-up of eyes, pupils contracting, breath held, intense stare, static`
- 005：`2x slow motion, sword draw slash mid-action, extreme close-up, energy burst, static camera`
- 006：`close-up of enemy struck, impact, motion line, static`
- 007：`full body, sheathing sword, back turned, slow pull back, wide shot, still final pose`

## 可复用结论
- 居合戏的镜头几乎全 static+大特写=AI 最稳的打戏拍法
- 蓄势靠手/眼双锚点特写交替（030+024），不靠大动作
- 爆发仅 0.3s+升格+固定机位=爆发力顶配
- 音频三段（渐强→静默→重拍+刀声）是居合标配
- 全段 6s 是居合戏黄金时长，可压缩到 4s（减蓄势）或拉到 8s（加对峙前摇）

## 备注
- 本条是 30 条张力课的毕业案例，串联前 29 条
- 居合是动漫短剧最高频高张力场景，掌握它=掌握静态张力体系
- 实操：按镜表逐条生成 AI clip，剪辑按镜拼接，音频后期叠加
- 时长可调但比例守恒：蓄势最长，峰值最短，释放留韵

## WAN3.0 校准（2026-10-20）

- WAN3 30秒原生可直接生成完整段落，无需多段拼接；原参考时长可作为 WAN3 段落内子结构时长使用。
