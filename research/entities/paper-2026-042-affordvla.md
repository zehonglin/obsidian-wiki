---
title: "AffordVLA: 隐式可供性对齐增强 VLA 操作表征"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, spatial-reasoning]
sources: [raw/papers/2026-042-AffordVLA-affordance-feature-alignment.md]
arxiv: "2605.17517"
date: 2026-05-23
related_topic: T011
confidence: high
---

# AffordVLA 论文

**作者**：Weijie Kong, Zhian Su, Wei Yu, Huixu Dong（浙江大学 Grasp Lab）
**日期**：2026-05-23 | arXiv: 2605.17517
**研究方向**：`T011`（Manipulation / Grasping），交叉 `T008`（3D 视觉）

## 核心一句话

> 通过**隐式表征对齐**将可供性感知内化到 VLA 视觉表征中，推理零额外开销，RoboTwin Easy 超基线 **+20.5%**。

## 关键创新

1. **零样本可供性教师**——从 RGB 观察 + 语言指令提取任务条件的可供性视觉表征，无需额外可供性标注
2. **隐式表征对齐**——训练时将 VLA 中间视觉表征与教师可供性表征对齐，推理时移除教师模块
3. **推理零开销**——与基线 VLA 推理速度完全一致，不增加任何计算负担

## 实验结果

| 基准 | 提升 |
|---|---|
| RoboTwin Easy | **+20.5%** vs 最佳基线 |
| RoboTwin Hard | **+12.8%** vs 最佳基线 |
| 真实世界 | 非结构化场景验证通过 |

消融分析表明 AffordVLA 有效重塑 VLA 视觉表征，使其聚焦功能交互区域。

## 局限性

- ⚠️ 可供性教师的质量受限于教师模型能力上限
- ⚠️ 仅在 RoboTwin 和有限真实场景验证
- ⚠️ 隐式对齐可能损失部分全局语义表征能力

## 价值定位

AffordVLA 在操作任务中解决了 VLA 的**"看哪里"问题**——让模型聚焦任务相关功能区域。隐式对齐 + 零推理开销的设计极具工程价值，与 [[concept-t008-3d-vla]] 的 3D 空间感知互补。

## 相关页

- [[concept-t011-manipulation]]
- [[paper-2026-001-3d-mix]] — 3D-Mix 关注几何感知，AffordVLA 关注功能感知，互补
- *relafford6d*（待 ingest） — 同为可供性方向（如已录入）
- [[concept-t008-3d-vla]] — 可供性 + 3D 空间感知是自然组合
