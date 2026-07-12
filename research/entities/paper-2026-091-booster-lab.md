---
title: "Booster Lab：以数据为中心的人形运动策略学习与部署流程"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, navigation, dataset, imitation-learning]
sources: [raw/papers/2026-091-booster-lab-data-centric.md]
arxiv: "2606.27813"
date: 2026-06-26
related_topic: T013
confidence: medium
---

# Booster Lab 论文

**作者**：Penghui Chen 等（Booster Robotics）
**日期**：2026-06-26 | arXiv: 2606.27813
**研究方向**：`T013`（Navigation / Locomotion），交叉 `T010`（数据效率）

## 核心一句话

> 一条完整的 **data-centric 训练-部署 pipeline**：运动数据筛选 → real-to-sim 适配 → AMP-based RL 训练 → sim-to-real 迁移，在 Booster T1/K1 上验证数据质量对人形运动策略的决定性影响。

## 关键创新

1. **数据导向质量过滤**——从混合质量数据源中自动筛选物理可行且自然的运动片段
2. **Real-to-sim 模型适配**——缩小仿真-现实差距的系统化流程
3. **端到端可复现 pipeline**——从原始人类运动数据到可部署策略的完整工业级流程

## 实验结果

- Booster T1 机器人主验证
- Booster K1 跨平台初步验证
- 数据筛选对策略质量有显著影响（定性 + 定量）

## 价值定位

Booster Lab 是 [[concept-t013-navigation]] 中 **sim-to-real locomotion** 的工业实践。其 data-centric 理念直接回应 T010「数据质量对适配效果的影响」研究空白（[[concept-t010-data-efficiency]]）。

## 局限性

- ⚠️ 主要聚焦行走/运动，上肢操作涉及较少
- ⚠️ 数据筛选标准依赖人工设计，缺乏自动化
- ⚠️ AMP 对抗训练对数据片段的多样性敏感

## 相关 wiki 页

- [[concept-t013-navigation]] — 本文所属选题总览
- [[concept-t010-data-efficiency]] — data-centric 方法论交叉
- [[paper-2026-095-human-as-humanoid]] — 对比：用人类视频替代遥操作数据采集
- [[paper-2026-073-moe-rl-fault-tolerant]] — 腿足 RL 控制的另一方向（故障容忍）
