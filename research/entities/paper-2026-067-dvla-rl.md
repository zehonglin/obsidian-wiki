---
title: "dVLA-RL：离散扩散 VLA 的强化学习优化"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, training, reinforcement-learning, architecture]
sources: [raw/papers/2026-067-dVLA-RL-discrete-diffusion.md]
arxiv: "2606.23623"
date: 2026-06-22
related_topics: [T010, T012]
authors: "Yuhao Wu, Yitian Liu, Weijie Shen et al. (Yao Mu group)"
source_db: "arXiv"
confidence: high
---

# dVLA-RL 论文

**作者**：Yuhao Wu, Yitian Liu, Weijie Shen 等（慕宇课题组）  
**日期**：2026-06-22 | arXiv: 2606.23623  
**关联选题**：`T010`（数据效率）、`T012`（RL Training）

## 核心一句话

> 首次将 RL 应用于**离散扩散 VLA**，通过将去噪过程建模为 MDP 实现轨迹级优化，LIBERO 达 **99.7% 成功率**，RoboTwin 2.0 提升 **30.6%**。

## 关键创新

1. **轨迹级 RL 目标** — 将学习目标从边际动作概率转移到采样路径的联合概率，巧妙绕过 dVLA 中边际概率不可解的问题
2. **去噪 MDP 建模** — 将多步去噪过程建模为马尔可夫决策过程，路径概率 = step-wise transitions 的乘积
3. **自适应步调度** — 简单任务少步去噪、复杂任务多步去噪，平衡成功率和计算效率

## 实验结果

| 指标 | 数值 |
|---|---|
| LIBERO 成功率 | **99.7%**（SOTA） |
| RoboTwin 2.0 vs SFT | **+30.6%** |
| 架构类型 | 离散 Diffusion VLA |

## 局限性

- ⚠️ 离散 diffuser 架构的通用性 vs 连续 diffuser 的对比尚不充分
- ⚠️ RL 训练计算开销仍然显著
- ⚠️ RoboTwin 以外的 benchmark 验证不足

## 价值定位

dVLA-RL 是**离散扩散 VLA + RL 的首个工作**，理论上严格 formulate 了 dVLA 的 RL 训练目标。99.7% 的 LIBERO 成功率展示了 RL 优化的巨大潜力。自适应步调度对计算效率的提升也具工程价值。

## 相关页

- [[concept-t012-rl-training]]
- [[paper-2026-097-z1]] — Z-1 在连续 VLA 上做 GRPO，dVLA-RL 在离散 VLA 上做轨迹级 RL
- [[paper-2026-072-force]] — FORCE 关注训练稳定性，dVLA-RL 关注 RL 目标的数学可解性
- [[paper-2026-020-world-env]] — World-Env 用世界模型做 RL 环境，dVLA-RL 直接在仿真器中优化
- [[paper-2026-053-bora]] — BORA 在灵巧 VLA 上做离线-在线 RL，dVLA-RL 在操作 VLA 上做在线 RL
- [[concept-t010-data-efficiency]]
