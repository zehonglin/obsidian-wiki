---
title: "WARP-RM：自监督时间扭曲进度奖励模型"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, training, reinforcement-learning, dataset, imitation-learning]
sources: [raw/papers/2026-087-warp-rm-progress-reward.md]
arxiv: "2606.28320"
date: 2026-06-26
related_topics: [T010, T012]
authors: "Justin Yu, Ken Goldberg et al. (UC Berkeley)"
source_db: "arXiv"
confidence: high
---

# WARP-RM 论文

**作者**：Justin Yu, Ken Goldberg 等（UC Berkeley）  
**日期**：2026-06-26 | arXiv: 2606.28320  
**关联选题**：`T010`（数据效率）、`T012`（RL Training）

## 核心一句话

> 全**自监督**算法通过时间扭曲增强（变速播放 + 倒放）生成逐帧进度奖励信号，无需人工标注；在数据质量下降时维持 **19/20** 成功率（vanilla BC 仅 2/20），吞吐量提升最高 **18×**。

## 关键创新

1. **时间扭曲增强（Warp Augmentation）** — 通过变速播放和倒放生成逐帧进度目标，完全自监督，无需人工标注
2. **密集帧级进度信号** — 聚合重叠窗口预测产生连续的进度奖励，替代稀疏的二值任务奖励
3. **WARP-BC** — 利用标量奖励估计在行为克隆中加权高优势动作块，自动过滤低质量演示帧

## 实验结果

| 指标 | 数值 |
|---|---|
| 数据质量下降时成功率 | **19/20**（vs BC 2/20） |
| 吞吐量提升 | 最高 **18×** |
| 任务 | 物理双臂 T 恤折叠（从随机揉皱开始） |

## 局限性

- ⚠️ 仅在单一长时序任务（T 恤折叠）上验证
- ⚠️ 时间扭曲增强策略可能不适用于所有操作类型（如需要精确力控的任务）
- ⚠️ 奖励信号的泛化性有待更多任务验证

## 价值定位

WARP-RM 解决了 RL/IL 中的**奖励标注瓶颈**。完全自监督的进度评估对降低 VLA RL 训练的数据标注成本有直接价值。"数据质量下降时仍维持高性能"这一特性对实际部署场景（混合质量演示）尤为重要。

## 相关页

- [[concept-t012-rl-training]]
- [[paper-2026-097-z1]] — Z-1 的 completion-aware 奖励校准与 WARP-RM 的进度奖励互补
- [[paper-2026-020-world-env]] — World-Env 用 VLM 反思器做奖励，WARP-RM 用自监督时间扭曲做奖励
- [[paper-2026-053-bora]] — BORA 的 HiL 数据可与 WARP-RM 的质量加权结合
- [[concept-t010-data-efficiency]]
