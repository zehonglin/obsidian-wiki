---
title: "T008 选题：3D 视觉增强 VLA 模型"
created: 2026-07-11
updated: 2026-07-11
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [vla, spatial-reasoning, manipulation, mllm]
sources: [raw/topics/topics.json]
related_papers: [paper-2026-001, paper-2025-002, paper-2026-013, paper-2026-018, paper-2026-019]
confidence: high
novelty: 高
feasibility: 高
---

# T008 选题：3D 视觉增强 VLA 模型

## 一句话定位

> 把 3D 空间理解能力注入 Vision-Language-Action 模型，让机器人在 3D 操作任务上鲁棒。

## 为什么这个方向重要

VLA 模型（如 GR00T、π₀）底层 MLLM 主要在 2D 数据训练，**空间智能不足**——遇到 3D 操作、视角变化、几何敏感任务容易翻车。

## 三条已收敛的技术路线（基于 5 篇首批 ingest）

### 路线 A：**改造中间表示**（特征融合）
代表：[[paper-2026-001-3d-mix]]
- 把 3D 几何特征注入 VLA 的中间层
- 即插即用，**不改原模型**
- 适合快速验证不同 VLA 架构

### 路线 B：**改造输入**（视图变换）
代表：[[paper-2025-002-og-vla]]
- 把 RGBD 渲染成视角不变的 canonical 视图
- 改变输入空间，让 VLA 看到一致的图
- 代价：丢透视深度信息

### 路线 C：**引入世界模型**（想象力）
代表：[[paper-2026-013-world2vlm]] + [[paper-2026-018-starry]] + [[paper-2026-019-rise]]
- 用世界模型给 VLA 提供"想象"的 3D 未来
- 子路线 C1：蒸馏到 VLM（World2VLM）
- 子路线 C2：联合扩散时空+动作（STARRY）
- 子路线 C3：组合世界模型 + 想象空间训练（RISE）

## 评测基准全景

| 基准 | 类型 | 代表使用 |
|---|---|---|
| **SIMPLER** | OOD 仿真 | 3D-Mix |
| **LIBERO** | 桌面操作 | 3D-Mix |
| **Arnold** | 未见环境 | OG-VLA |
| **Colosseum** | 视觉干扰 | OG-VLA |
| **RoboTwin 2.0** | 双手操作 | STARRY |
| **真实世界 3 任务** | 动态/接触密集 | RISE |

## 待老板裁决的差异化方向（来自 3D-Mix 论文）

1. **实时 3D 感知**（绕开 VGGT 离线重建）
2. **更精细的 3D-语言跨模态对齐**
3. **更泛化的场景验证**（不只是桌面）
4. **点云/深度图等替代 3D 表征**

## 相关 wiki 页

- 5 个 paper 实体页（见 related_papers）
- [[concept-world-model-for-robotics]]（跨选题概念，待建）
- [[concept-vla-model]]（VLA 总述，待建）
