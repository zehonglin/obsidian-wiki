---
title: "MoE-RL：故障容忍的腿足机器人混合专家强化学习"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, navigation, reinforcement-learning, architecture]
sources: [raw/papers/2026-073-moe-rl-fault-tolerant.md]
arxiv: "2606.25965"
date: 2026-06-24
related_topic: T013
confidence: medium
---

# MoE-RL Fault-Tolerant Legged Locomotion 论文

**作者**：Giulio Turrisi, Ozan Pali, Luca Oneto, Claudio Semini（IIT 意大利）
**日期**：2026-06-24 | arXiv: 2606.25965
**研究方向**：`T013`（Navigation / Locomotion），交叉 `T012`（RL）、`T009`（安全/鲁棒性）

## 核心一句话

> 显式利用故障信息的 **Mixture-of-Experts（MoE）架构**，让不同专家网络学习不同执行器故障条件下的补偿策略，实现腿足机器人在复杂地形上的故障容忍运动。

## 关键创新

1. **故障感知模块化控制**——故障检测器动态路由到合适的专家子网络，而非单一策略覆盖所有故障模式
2. **MoE + RL 端到端训练**——专家间自动分工，无需手动指定故障-专家映射
3. **行星探索场景驱动**——面向远程环境下执行器故障不可修复的实际需求

## 实验结果

- 多种执行器故障（关节卡死、力矩衰减等）× 复杂地形上验证
- 相比单一策略：MoE 架构在故障条件下维持更稳定的运动性能
- 展示专家网络间的有效分工

## 价值定位

为 [[concept-t013-navigation]] 提供了 **locomotion 鲁棒性** 的模块化思路。MoE 故障路由与 T009 安全研究中的运行时验证（[[paper-2026-046-pre-vla]]）形成互补：一个事前检测、一个事后补偿。

## 局限性

- ⚠️ 故障类型需预定义，开放集故障检测能力有限
- ⚠️ MoE 路由在边缘故障情况下可能不稳定
- ⚠️ 仅验证足式运动，未扩展到轮式或飞行平台

## 相关 wiki 页

- [[concept-t013-navigation]] — 本文所属选题总览
- [[concept-t012-rl-training]] — RL 训练方法交叉
- [[paper-2026-088-ppo-eal]] — 安全约束 RL 控制（T009×T012）
- [[paper-2026-046-pre-vla]] — 运行时验证（事前安全 vs 事后补偿）
