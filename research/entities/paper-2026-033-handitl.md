---
title: "HandITL: 人类在环修正提升灵巧 VLA 操作"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, imitation-learning]
sources: [raw/papers/2026-033-HandITL-dexterous-VLA.md]
arxiv: "2605.15157"
date: 2026-05-14
related_topic: T011
confidence: high
---

# HandITL 论文

**作者**：Zhuohang Li et al.
**日期**：2026-05-14 | arXiv: 2605.15157
**研究方向**：`T011`（Manipulation / Dexterous）

## 核心一句话

> 将人类修正意图与自主策略**无缝融合**，解决双臂灵巧操作中的"手势跳跃"问题，接管抖动减少 **99.8%**。

## 关键创新

1. **无缝干预融合**——解决人机交接时的 gesture jump（手势跳变），使人类修正与策略执行连贯过渡
2. **干预数据→策略微调闭环**——收集人类干预数据用于策略改进，形成正循环
3. **双臂灵巧操作专属设计**——针对高 DoF 双手场景的累积误差问题

## 实验结果

| 指标 | 改善 |
|---|---|
| 接管抖动 | 减少 **99.8%** |
| 抓取失败率 | 降低 **87.5%** |
| 平均完成时间 | 减少 **19.1%** |
| 微调后任务提升 | **+19%** 平均（3 个长期灵巧任务） |

验证任务：双臂协调、工具使用、精细长视野操作。

## 局限性

- ⚠️ 仅针对双臂灵巧操作场景，未验证其他形态
- ⚠️ 依赖人类实时干预，数据收集成本高
- ⚠️ 与 [[concept-t009-safety-robustness]] 的运行时验证思路有重叠但未对比

## 价值定位

HandITL 是灵巧操作 VLA 中**人机协同范式**的代表工作，将交互式模仿学习从低 DoF 扩展到高 DoF 双臂场景，解决了关键的 gesture jump 技术瓶颈。

## 相关页

- [[concept-t011-manipulation]]
- [[paper-2026-038-dexora]] — 同为双臂灵巧 VLA，关注数据规模与质量
- [[paper-2026-053-bora]] — 灵巧 VLA 的 RL 后训练，互补路线
- [[paper-2026-046-pre-vla]] — 运行时验证思路，与干预修正可对比
