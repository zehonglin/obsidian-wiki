---
title: "CWI：人形机器人全身模仿学习——解耦行走与操作的复合框架"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, navigation, manipulation, imitation-learning]
sources: [raw/papers/2026-090-cwi-humanoid-locomanipulation.md]
arxiv: "2606.27663"
date: 2026-06-26
related_topic: T013
confidence: medium
---

# CWI 论文

**作者**：Wenqi Ge 等
**日期**：2026-06-26 | arXiv: 2606.27663
**研究方向**：`T013`（Navigation / Locomotion），交叉 `T011`（操作）

## 核心一句话

> 解耦策略——上身操作用 MoCap 模仿、下身行走用命令条件控制 + 双判别器 AMP——在 LimX Oli 全尺寸人形上实现稳定的 loco-manipulation 协调。

## 关键创新

1. **复合全身模仿（Composite Whole-Body Imitation）**——上身/下身解耦：上身 MoCap 数据 + 下身 AMP 命令条件控制
2. **Multi-critic 架构**——分离行走、操作、动作风格三个目标的判别器，减少梯度冲突
3. **Teacher-student 蒸馏**——部署时仅需双手位姿和速度/高度命令，无需全身体态捕捉设备

## 实验结果

- LimX Oli 全尺寸人形机器人部署
- 竞争性的 loco-manipulation 性能（行走 + 操作同时进行）
- 无需全身体态捕捉即可遥操作

## 价值定位

CWI 的解耦思路为 [[concept-t013-navigation]] 中「导航 + 操作共存」场景提供了实用方案。与 VLK（[[paper-2026-093-vlk]]）的合成数据路线不同，CWI 走的是架构解耦路线。

## 局限性

- ⚠️ 解耦策略可能限制上下身协同的复杂动作（如需要腰腹发力的任务）
- ⚠️ 下身完全依赖 AMP 学习，数据片段质量影响行走风格
- ⚠️ 仅单平台验证（LimX Oli）

## 相关 wiki 页

- [[concept-t013-navigation]] — 本文所属选题总览
- [[paper-2026-093-vlk]] — 对比：VLK 用 3DGS 合成数据解决类似问题
- [[paper-2026-095-human-as-humanoid]] — 对比：Human-as-Humanoid 用人类视频做数据源
- [[paper-2026-038-dexora]] — 双臂操作（T011），可与 CWI 的上身操作互补
