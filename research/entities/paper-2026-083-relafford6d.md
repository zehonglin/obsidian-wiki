---
title: "RelAfford6D: Relational 6D Affordance Graphs for Constraint-Driven Robotic Manipulation"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, manipulation, spatial-reasoning]
sources: [raw/papers/2026-083-RelAfford6D-relational-affordance.md]
arxiv: "2606.27036"
date: 2026-06-25
related_topic: T008, T011
confidence: high
---

# RelAfford6D 论文

**作者**：Guodong Zhang et al.
**日期**：2026-06-25 | arXiv: 2606.27036
**研究方向**：`T008` + `T011`

## 核心一句话

> 基于关系 6D 可供性图（Relational 6D Affordance Graph）的训练无关框架，从自由格式指令推断语义拓扑 → SE(3) 位姿估计 → 运动学约束满足 → 闭环重规划。

## 关键创新

1. **训练无关（Training-free）**——利用预训练视觉基础模型，无需额外训练
2. **关系 6D 可供性图**——从自由格式指令推断主要交互部件及其物理锚点的语义拓扑
3. **运动学约束满足**——将下游执行建模为运动学约束问题，旋转/滑动关节轨迹在物理流形上
4. **闭环重规划**——动态环境中对抗干扰的鲁棒跟踪

## 实验结果

- 仿真和真实环境均验证
- 零样本成功率和跨类别泛化优于数据驱动基线
- 对铰接物体（articulated objects）操作效果突出

## 价值定位

RelAfford6D 将空间感知与可供性推理结合，提供训练无关的即插即用方案。被 [[paper-2026-042-affordvla]]（AffordVLA）引用为可供性方向的重要对比工作。与 [[concept-t008-3d-vla]] 的方向一致——3D 空间感知融入 VLA 增强空间理解能力。

## 局限性

- 依赖预训练视觉基础模型质量
- 铰接物体以外的一般化操作场景有待验证
- 训练无关特性虽灵活，但可能不如端到端方法在特定任务上优化

## 关键引用 / 相关页

- [[concept-t008-3d-vla]]
- [[concept-t011-manipulation]]
- [[paper-2026-042-affordvla]] — 同为可供性方向
