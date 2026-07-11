---
title: "STARRY: 时空动作中心的机器人操作世界模型"
created: 2026-07-11
updated: 2026-07-11
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, spatial-reasoning, vision-language]
sources: [raw/papers/2026-018-STARRY.md]
arxiv: "2604.26848v2"
date: 2026-04-29
related_topic: T008
confidence: high
---

# STARRY 论文

**作者**：Yuxuan Tian et al.
**日期**：2026-04-29（v2: 2026-05-01）| arXiv: 2604.26848v2
**研究方向**：`T008`（3D+VLA）

## 核心一句话

> 用统一扩散过程**联合去噪未来时空潜变量和动作**，把 3D 几何信息（GASAM）注入 VLA 注意力，桥接 2D 视觉 token 和 3D 度量控制。

## 三大组件

1. **世界模型增强的动作生成策略**——统一扩散时空+动作
2. **GASAM（Geometry-Aware Selective Attention Modulation）**——把深度/末端位姿几何信息转 token 权重
3. **以动作为中心的时空世界建模**

## 实验结果

| 基准 | 成功率 |
|---|---|
| RoboTwin 2.0 Clean | 93.82% |
| RoboTwin 2.0 Randomized | 93.30% |
| 真实世界（对比 π₀.₅）| **42.5% → 70.8%**（+28.3） |

50 个双手操作任务平均。

## 局限性

- ⚠️ 扩散过程计算开销大
- ⚠️ 依赖深度估计精度
- ⚠️ 仅在双手操作验证

## 与 T008 其它论文关系

- vs [[paper-2026-001-3d-mix]]：**都是 3D 注入 VLA**，但 STARRY 用 GASAM 改注意力权重，3D-Mix 用门控融合改中间特征
- vs [[paper-2026-019-rise]]：**都引入世界模型**，但 STARRY 用扩散联合训练，RISE 用组合式世界模型 + 想象空间策略更新

## 关键引用

- π₀.₅（Physical Intelligence）
- RoboTwin 2.0 benchmark
- Diffusion policy
