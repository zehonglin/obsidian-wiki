---
title: "Evo-Depth：轻量级隐式深度增强 VLA（仅 0.9B 参数）"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, spatial-reasoning, inference, manipulation]
sources: [raw/papers/2026-034-Evo-Depth-lightweight-depth-VLA.md]
arxiv: "2605.14950"
date: 2026-05
related_topic: T008
confidence: high
---

# Evo-Depth 论文

**作者**：Tao Lin, Yuxin Du, Jiting Liu, Nuobei Zhu et al.
**日期**：2026-05-14 | arXiv: 2605.14950
**研究方向**：`T008`（3D+VLA）

## 核心一句话

> 仅 0.9B 参数，通过隐式深度编码（无需额外传感器）从多视角 RGB 提取深度特征，以最小模型/最低显存/最高推理频率实现 3D 增强 VLA。

## 关键创新

1. **Implicit Depth Encoding Module**——从多视角 RGB 图像直接提取紧凑深度特征，无需深度传感器或大型几何基础模型
2. **Spatial Enhancement Module**——通过深度感知调制将深度特征融入视觉语言表示
3. **Progressive Alignment Training**——渐进式对齐训练策略，分阶段对齐深度增强表示与下游动作学习
4. **极致轻量**——仅 0.9B 参数，最低 GPU 显存占用，最高推理频率

## 实验结果

| 维度 | 表现 |
|---|---|
| 4 个仿真基准 | 优越性能 |
| 真实世界实验 | 最高平均成功率 |
| 模型尺寸 | 最小（0.9B） |
| GPU 显存 | 最低 |
| 推理频率 | 最高 |

相比使用显式 3D 输入（点云/深度图）的方法更高效。

## 价值定位

Evo-Depth 直接解决 T008 核心研究空白——**如何高效地将 3D 信息注入 VLA**。其隐式深度估计方案无需额外传感器，代表了"端到端深度估计 + VLA"的技术路线，与 [[paper-2026-002-gst-vla]] 的显式深度图输入形成对比。

## 局限性

- ⚠️ 隐式深度估计的精度受限于 RGB 输入质量
- ⚠️ 多视角输入要求可能限制单目场景应用
- ⚠️ 与显式 3D 方法的精度上限对比不够充分

## 关键引用 / 相关页

- [[concept-t008-3d-vla]]
- [[paper-2026-002-gst-vla]] — 显式深度 token vs 隐式深度编码
- [[paper-2026-001-3d-mix]] — VGGT 重建 vs 隐式估计
- [[paper-2026-055-stereopolicy-3d-vla]] — 立体视觉深度感知对比
