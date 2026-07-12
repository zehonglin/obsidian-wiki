---
title: "RynnWorld-4D：4D 具身世界模型（RGB+深度+光流联合生成）"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, architecture, spatial-reasoning]
sources: [raw/papers/2026-108-rynnworld-4d.md]
arxiv: "2607.06559"
date: 2026-07-07
related_topics: [T008, T014]
authors: "Haoyu Zhao, Xingyue Zhao, Siteng Huang, Xin Li, Deli Zhao, Zhongyu Li"
source_db: "arXiv"
confidence: medium
---

# RynnWorld-4D 论文

**作者**：Haoyu Zhao, ... Zhongyu Li  
**日期**：2026-07-07 | arXiv: 2607.06559  
**关联选题**：`T008`（3D 视觉）/ `T014`（世界模型）

## 一句话

> 从单张 RGB-D 图像**联合生成未来 RGB 帧 + 深度图 + 光流**的 4D 世界模型——比 2D 像素视频更接近机器人末端执行器动作的物理基础。

## 核心方法

### 1. RGB-DF 4D 世界模型
- 在**统一扩散过程**中同时生成 RGB、深度、光流
- 确保外观、几何和运动三者一致

### 2. 三分支架构
- 跨模态注意力（cross-modal attention）
- 帧级 3D RoPE（旋转位置编码）

### 3. Rynn4DDataset 1.0
- 超过 **2.544 亿帧**自中心人类和机器人操作视频
- 含深度和光流伪标签

### 4. RynnWorld-4D-Policy
- 逆动力学头**单次前向传播**输出动作
- 绕过多步去噪，推理高效

## 实验结果

- 灵巧双手操作任务达到 SOTA
- 在需要**空间精度和时间协调**的任务上表现尤为出色

## 价值定位

- **世界模型从 2D→4D 的跨越**：深度 + 光流提供几何和运动信息，超越纯 RGB 视频预测
- 与 [[paper-2026-057-rynnvla002-unified-vla-wm]]（同团队 RynnVLA-002）形成系列：先统一 VLA+WM，再升级到 4D
- 与 [[paper-2026-056-gaussiandream-3d-vla]]（3D 高斯世界模型）互补：GaussianDream 用高斯表示，RynnWorld-4D 用 RGB-DF

## 局限性

- 需要 RGB-D 输入（深度传感器依赖）
- 2.544 亿帧数据集的构建成本高
- 尚未充分验证 sim-to-real 迁移

## 引用页

- [[paper-2026-057-rynnvla002-unified-vla-wm]] — 同团队 VLA+WM 统一
- [[paper-2026-056-gaussiandream-3d-vla]] — 3D 高斯世界模型
- [[paper-2024-001-3d-vla]] — 3D-VLA 开创性工作
- [[concept-t008-3d-vla]] — 3D 视觉增强 VLA 选题
- [[concept-t014-wm]] — 世界模型选题
