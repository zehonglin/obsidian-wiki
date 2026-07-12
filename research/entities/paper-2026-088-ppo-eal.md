---
title: "PPO-EAL：精确增广拉格朗日 PPO 实现安全机器人控制"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [training, reinforcement-learning, navigation]
sources: [raw/papers/2026-088-ppo-eal-safe-rl.md]
arxiv: "2606.27861"
date: 2026-06-26
related_topics: [T009, T012]
authors: "Jiatao Ding et al."
source_db: "arXiv"
confidence: high
---

# PPO-EAL 论文

**作者**：Jiatao Ding 等  
**日期**：2026-06-26 | arXiv: 2606.27861  
**关联选题**：`T009`（安全鲁棒性）、`T012`（RL Training）

## 核心一句话

> 将**精确增广拉格朗日优化**集成到 PPO 中，理论保证安全约束执行，零样本 sim-to-real 部署于齿轮装配任务，降低峰值接触力。

## 关键创新

1. **精确二次惩罚项** — 替代传统大惩罚因子方法，理论保证约束满足且无需不切实际的极大惩罚
2. **动量调节乘子更新** — 提升对偶变量稳定性，减少训练中的约束振荡和不安全行为
3. **一阶可扩展** — 虽然是"精确"方法，但保持一阶计算复杂度，可扩展到高维机器人

## 实验结果

| 指标 | 结果 |
|---|---|
| 评测任务 | cart-pole、双摆、7-DoF Franka 到达、四足行走 |
| 安全精度 | 优于 SOTA 一阶安全 RL |
| 任务奖励 | 与不安全 RL 基线相当 |
| Sim-to-real | 齿轮装配零样本迁移成功 |
| 关键指标 | 提高任务成功率，**降低峰值接触力** |

## 局限性

- ⚠️ 一阶方法在高度非线性约束上可能效果受限
- ⚠️ Sim-to-real gap 仍然存在
- ⚠️ 未在 VLA 架构上直接验证

## 价值定位

PPO-EAL 提供了**安全 RL 的通用框架**，可直接应用于 VLA 策略训练中的安全约束。对 T009（VLA 安全）有方法论价值：在训练阶段而非推理阶段保证安全，与 [[paper-2026-046-pre-vla]] 的推理时验证形成互补。

## 相关页

- [[concept-t012-rl-training]]
- [[paper-2026-046-pre-vla]] — Pre-VLA 在推理时做安全验证，PPO-EAL 在训练时做安全约束
- [[paper-2026-073-moe-rl-fault-tolerant]] — MoE-RL 做故障容忍，PPO-EAL 做安全约束，不同安全维度
- [[concept-t009-safety-robustness]]
- [[concept-t010-data-efficiency]]
