---
title: "ESI-Bench：具身空间智能评测基准（感知-动作闭环）"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [benchmark, evaluation, spatial-reasoning, vla]
sources: [raw/papers/2026-039-ESI-Bench-embodied-spatial-intelligence.md]
arxiv: "2605.18746"
date: 2026-05
related_topic: T008
confidence: high
---

# ESI-Bench 论文

**作者**：Yining Hong, Jiageng Liu, Han Yin, Manling Li, Leonidas Guibas, Li Fei-Fei, Jiajun Wu, Yejin Choi
**日期**：2026-05-18 | arXiv: 2605.18746
**研究方向**：`T008`（3D+VLA 评测）

## 核心一句话

> 将空间智能的观察者重新定义为行动者，构建感知-动作闭环的主动空间智能评测基准（10 类任务 + 29 子类），揭示多数失败源于"动作盲"而非感知弱。

## 关键创新

1. **主动空间智能基准**——基于 OmniGibson 构建，智能体需自主决定感知、移动、操作的时机和序列，而非被动接收 oracle 观测
2. **Spelke 核心知识系统**——任务设计基于发展心理学的核心知识（物体持续性、空间导航、重力直觉等），系统化覆盖空间智能维度
3. **多维度评估框架**——主动 vs 被动、随机多视角、3D grounding 效果三个维度交叉评估

## 实验结果（关键发现）

| 发现 | 含义 |
|---|---|
| 主动探索 >> 被动方法 | 动作选择直接影响观测质量 |
| 随机多视角引入噪声 | 不是视角越多越好，需要选择性感知 |
| 多数失败源于"动作盲" | 糟糕动作 → 糟糕观测 → 级联错误 |
| 不完美的 3D 表示比 2D 更有害 | 低质量 3D 信息不如不用 |
| 元认知差距 | 模型过早高置信度承诺 |

## 价值定位

ESI-Bench 是 T008 选题的**核心评测基础设施**——它不仅测试 3D 感知能力，更揭示了一个深刻洞察：**空间智能的瓶颈不在感知，而在动作选择**。这直接质疑了 T008 多数工作（如 [[paper-2026-001-3d-mix]]、[[paper-2026-002-gst-vla]]）"改进感知就能改进操作"的隐含假设。

## 局限性

- ⚠️ 仅在 OmniGibson 仿真环境中评估，未涉及真实机器人
- ⚠️ 任务类型覆盖空间智能子集，不涉及灵巧操作
- ⚠️ 评测的模型范围未详

## 关键引用 / 相关页

- [[concept-t008-3d-vla]]
- [[paper-2026-001-3d-mix]] — 其 SIMPLER 评测需配合 ESI-Bench 的主动视角
- [[paper-2026-030-multiview-vla]] — 多视角选择策略可被 ESI-Bench 评估
- [[paper-2026-022-wam-survey]] — WAM 综述，评测维度全景
