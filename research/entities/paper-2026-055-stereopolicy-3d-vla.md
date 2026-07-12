---
title: "StereoPolicy：立体视觉驱动的 3D 机器人操作策略"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, spatial-reasoning, manipulation, architecture]
sources: [raw/papers/2026-055-stereopolicy-3d-vla.md]
arxiv: "2605.09989"
date: 2026-05
related_topic: T008
confidence: high
---

# StereoPolicy 论文

**作者**：Evans Han et al.
**日期**：2026-05-11 | arXiv: 2605.09989
**研究方向**：`T008`（3D+VLA）

## 核心一句话

> 直接利用同步立体图像对进行视动策略学习，通过 Stereo Transformer 隐式捕获视差和深度线索，无需显式 3D 重建或相机标定。

## 关键创新

1. **Stereo Transformer 融合**——使用预训练 2D 视觉编码器分别处理左右图像，通过 Stereo Transformer 融合表征，隐式捕获空间对应和视差线索
2. **即插即用集成**——可与 diffusion-based 和 VLA 策略无缝集成
3. **无需显式 3D 重建或相机标定**——绕过点云重建和传感器标定的工程开销，利用 2D 预训练模型的优势

## 实验结果

| 基准 | 表现 |
|---|---|
| RoboMimic | 超越 RGB, RGB-D, 点云, 多视角基线 |
| RoboCasa | 超越所有基线 |
| OmniGibson | 超越所有基线 |
| 真实世界（桌面 + 双臂移动） | 验证鲁棒性 |

证明立体视觉是连接 2D 预训练表征与 3D 几何理解的可扩展鲁棒模态。

## 价值定位

StereoPolicy 代表 T008 的**立体视觉路线**——介于纯 2D 方法和显式 3D 方法之间的"甜点"。相比 [[paper-2026-001-3d-mix]] 的 VGGT 重建（重量级）和 [[paper-2026-034-evo-depth]] 的隐式估计（轻量但间接），立体视觉提供了一种天然的深度来源，且可复用海量 2D 预训练模型。

## 局限性

- ⚠️ 需要双目相机硬件配置，限制了部署灵活性
- ⚠️ 立体匹配的计算开销（虽然比点云重建轻量）
- ⚠️ 未在极端遮挡或弱纹理场景验证

## 关键引用 / 相关页

- [[concept-t008-3d-vla]]
- [[paper-2026-001-3d-mix]] — VGGT 重建 vs 立体融合
- [[paper-2026-034-evo-depth]] — 隐式深度 vs 双目立体
- [[paper-2026-030-multiview-vla]] — 多视角合成 vs 立体视觉
