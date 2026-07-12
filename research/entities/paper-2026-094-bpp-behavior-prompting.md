---
title: "BPP: Behavior Prompting Policy — Demonstrations as Prompts for Manipulation"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, manipulation, imitation-learning]
sources: [raw/papers/2026-094-BPP-behavior-prompting.md]
arxiv: "2606.30457"
date: 2026-06-29
related_topic: T010
confidence: high
---

# BPP: Behavior Prompting Policy 论文

**作者**：Austin Patel, Ben Pekarek, Joel Enrique Castro Hernandez, et al.
**日期**：2026-06-29 | arXiv: 2606.30457
**研究方向**：`T010`（少样本适配）

## 核心一句话

> 将 LLM 的 in-context learning 范式迁移到机器人操作：单次人类演示作为「行为提示」，推理时即时执行新任务，无需 fine-tuning。

## 关键创新

1. **Behavior Prompting 范式**——单次人类演示作为 prompt，推理时即时执行新任务
2. **BPP 架构**——in-context visuomotor 网络，将行为提示和当前观测转化为机器人动作
3. **iPhUMI 数据接口**——手持操作接口，用于收集多样化训练数据
4. **任务多样性 > 数据量**——发现任务多样性（而非数据量）是 prompting 能力的核心驱动因素

## 实验结果

- 评估基准：DrawAnything 和 LIBERO-Gen
- 通过单次演示即可命令机器人完成已知任务或定义新能力
- 任务多样性驱动 prompting 能力的关键 insight 对数据采集策略有指导意义

## 价值定位

BPP 将 in-context learning 从 LLM 自然延伸到机器人领域，概念优雅。被 [[paper-2026-100-sarl]]（SARL）引用为行为提示方向的对比工作——BPP 用演示做 prompt，SARL 用 RL 优化语言 prompt。

## 局限性

- 单次演示的信息量有限，复杂任务可能不足
- iPhUMI 手持接口虽然低成本，但数据质量依赖操作者
- 评估基准（DrawAnything / LIBERO-Gen）相对新颖，社区认可度有待观察

## 关键引用 / 相关页

- [[concept-t010-data-efficiency]]
- [[paper-2026-100-sarl]] — RL vs prompting 对比
- [[paper-2026-079-abc-scalable-behavior-cloning]] — 数据基础设施互补
