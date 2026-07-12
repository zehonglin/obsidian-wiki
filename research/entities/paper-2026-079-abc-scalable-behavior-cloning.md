---
title: "ABC: Scalable Behavior Cloning with Open Data, Training, and Evaluation"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, dataset, manipulation, imitation-learning]
sources: [raw/papers/2026-079-abc-scalable-behavior-cloning.md]
arxiv: "2606.27375"
date: 2026-06-25
related_topic: T010
confidence: high
---

# ABC: Scalable Behavior Cloning

**作者**：Arthur Allshire, Himanshu Gaurav Singh, Ritvik Singh, Adam Rashid, Hongsuk Choi, et al.
**日期**：2026-06-25 | arXiv: 2606.27375
**研究方向**：`T010`（数据效率）

## 核心一句话

> 全开源行为克隆工具栈：ABC-130K 数据集（3500 小时 / 130K+ 片段 / 195 种任务）+ 硬件设计 + 训练基础设施 + 仿真评估管道，为社区提供可复现的 BC 研究基础。

## 关键创新

1. **ABC-130K**——迄今最大开源遥操作数据集，3500 小时、130K+ 片段、195 种任务
2. **全链路开源**——硬件设置、训练基础设施、仿真管道、评估方案全公开
3. **仿真-真实协同**——400 小时仿真遥操作数据 + 协同训练方案
4. **架构对比基准**——系统对比 DiT 和 VLA 模型的常见架构选择

## 实验结果

- 成功执行折纸、从钱包取信用卡等灵巧任务
- 项目页: https://abc.bot
- 提供可复现的完整工具链

## 价值定位

ABC 是 VLA 数据效率研究的重要基础设施。被 [[paper-2026-126-vla-review-realworld]]（VLA 部署综述）引用为数据采集标准化范例；被 [[paper-2026-127-vla-survey-manipulation]]（VLA 操作综述）引用为大规模数据集代表；被 [[paper-2026-128-embodied-ai-sae]]（Embodied AI 白皮书）引用为开源工具链标杆。

## 局限性

- 硬件设置仍需一定成本
- 数据采集依赖遥操作质量
- VLA 模型对比可能不涵盖最新方法

## 关键引用 / 相关页

- [[concept-t010-data-efficiency]]
- [[paper-2026-104-qwen-robotmanip-alignment]] — 同为大规模数据驱动方向
- [[paper-2026-094-bpp-behavior-prompting]] — 任务多样性 vs 数据量对比
