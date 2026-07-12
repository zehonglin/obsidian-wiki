---
title: "FORCE：VLA 强化学习微调的值校准热身 + 自蒸馏"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, training, reinforcement-learning]
sources: [raw/papers/2026-072-force-vla-rl-finetuning.md]
arxiv: "2606.26006"
date: 2026-06-24
related_topics: [T010, T012]
authors: "Shuyi Zhang, Yunfan Lou, Hongyang Cheng, Yichen Guo, Chuyao Fu, Yaoxu Lyu, Xiaojie Zhang, Haoran Li, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang"
source_db: "arXiv"
confidence: high
---

# FORCE 论文

**作者**：Shuyi Zhang 等（Shanghang Zhang 组）  
**日期**：2026-06-24 | arXiv: 2606.26006  
**关联选题**：`T010`（数据效率）、`T012`（RL Training）

## 核心一句话

> 提出三阶段 RL 微调框架（Value-Calibrated Warm-Up → Online Training → Self-Distillation），解决 VLA 从模仿学习到 RL 的**灾难性初始遗忘**问题，成功率绝对提升 **79%**，训练加速 **32.5%**。

## 关键创新

1. **Value-Calibrated Warm-Up** — 利用 on-policy rollout 缓解 Q 函数的分布偏移，避免 RL 初期的性能崩塌
2. **Q 函数过滤策略** — 校准后的 Q 函数同时筛选策略自身动作提案和专家数据，仅高价值动作进入训练
3. **Self-Distillation 稳定化** — 自蒸馏进一步稳定 RL 后期的策略抖动

## 实验结果

| 指标 | 数值 |
|---|---|
| 成功率绝对提升 | **+79%** |
| vs 先前 RL 方法 | **+10%** |
| 训练加速 | **32.5%** |
| 评测范围 | 仿真 + 真实世界任务 |

关键：缓解了 VLA RL 微调中常见的成功率骤降问题，**无需人工干预**。

## 局限性

- ⚠️ 三阶段训练流程较复杂，超参敏感
- ⚠️ 仍依赖 on-policy rollout，计算开销大
- ⚠️ Value calibration 质量依赖初始 Q 函数训练

## 价值定位

FORCE 直击 VLA RL 微调的核心痛点——**灾难性遗忘**。Value-calibrated warm-up 是一个工程上可直接复用的技巧。与 Z-1 的 GRPO 采样效率优化形成互补：FORCE 稳定训练前期，Z-1 提升采样效率。

## 相关页

- [[concept-t012-rl-training]]
- [[paper-2026-097-z1]] — Z-1 的 GRPO 与 FORCE 的三阶段框架是 VLA RL 后训练的两条路线
- [[paper-2026-067-dvla-rl]] — dVLA-RL 解决离散 VLA 的 RL 目标问题，FORCE 解决连续 VLA 的训练稳定性
- [[paper-2026-020-world-env]] — World-Env 用世界模型降低 RL 环境成本，FORCE 降低 RL 训练不稳定性
- [[paper-2026-053-bora]] — BORA 的残差适配思路与 FORCE 的 Q 函数过滤互补
- [[concept-t010-data-efficiency]]
