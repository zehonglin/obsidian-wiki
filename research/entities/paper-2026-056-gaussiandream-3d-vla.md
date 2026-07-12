---
title: "GaussianDream：前馈式 3D 高斯世界模型插件"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, spatial-reasoning]
sources: [raw/papers/2026-056-gaussiandream-3d-vla.md]
arxiv: "2605.20752"
date: 2026-05-20
related_topics: [T008, T014]
authors: "Haibao Yu 等"
source_db: "arXiv"
confidence: high
---

# GaussianDream 论文

**作者**：Haibao Yu 等  
**日期**：2026-05-20 (v2) | arXiv: 2605.20752  
**关联选题**：`T008`（3D 视觉）/ `T014`（世界模型）

## 一句话

> **前馈式 3D 高斯世界模型插件**：训练时学习 3D 空间结构 + 未来演化的前缀查询，推理时丢弃所有辅助头——LIBERO **98.4% SOTA**，推理零额外开销。

## 核心方法

### 1. GaussianDream Queries
- 在编码器中引入**可学习前缀查询**
- 捕获当前帧 3D 空间结构 + 短期未来演化
- 推理时仅需前缀查询，**无需高斯重建或未来预测**

### 2. 双头训练
- **静态重建头**：当前 3D 高斯场景状态（RGB + 深度监督）
- **未来预测头**：未来高斯演化状态（未来 RGB + 深度 + 伪 3D 场景流监督）
- 推理时**全部丢弃**，仅保留学习到的前缀

### 3. 设计哲学
- 将 3D 高斯表示作为 VLA 的**内部中间表示**，而非外部输入模态
- 训练时学习空间感知，推理时"内化"为前缀查询

## 实验结果

| 基准 | 结果 |
|---|---|
| LIBERO | **98.4%**（SOTA） |
| RoboCasa Human-50 | 54.8% |
| 真实机器人 | 50.0% |

相比其他 3D 增强 VLA：精度强 + 推理效率高于视频世界模型方法。

## 价值定位

- **3D 世界模型的高效部署范式**：训练时学 3D，推理时零开销
- 与 [[paper-2026-108-rynnworld-4d]]（4D 世界模型）互补：GaussianDream 用高斯表示，RynnWorld-4D 用 RGB-DF
- 与 [[paper-2024-001-3d-vla]]（3D-VLA 开山工作）一脉相承：3D-VLA 用扩散模型生成点云，GaussianDream 用 3D 高斯
- LIBERO 98.4% SOTA 证明 3D 空间建模对操作的关键作用

## 局限性

- 训练时需要深度信息辅助监督
- 短期未来预测范围有限
- 3D 高斯表示在大规模场景的内存开销

## 引用页

- [[paper-2024-001-3d-vla]] — 3D-VLA 开创性工作
- [[paper-2026-108-rynnworld-4d]] — 4D 世界模型（互补）
- [[paper-2026-001-3d-mix]] — 3D-Mix（同属 T008 3D 增强）
- [[concept-t008-3d-vla]] — 3D 视觉增强 VLA 选题
- [[concept-t014-wm]] — 世界模型选题
