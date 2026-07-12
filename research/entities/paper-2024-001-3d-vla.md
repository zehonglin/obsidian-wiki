---
title: "3D-VLA：3D 视觉-语言-动作生成式世界模型"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, spatial-reasoning]
sources: [raw/papers/2024-001-3D-VLA.md]
arxiv: "2403.09631"
date: 2024-03
related_topics: [T008, T014]
authors: "Haoyu Zhen, Aoran Wang, Tan Song, Jia Zheng, Liang-Jian Deng, Wenhao Huang, Xiaoxiao Luo, Xiaojuan Qi, Qianru Sun, Hanwang Zhang, Zhi-Gang Liu, Jiaqi Wang, Zi Huang"
source_db: "arXiv"
confidence: high
---

# 3D-VLA 论文

**作者**：Haoyu Zhen 等  
**日期**：2024-03 | arXiv: 2403.09631  
**关联选题**：`T008`（3D 视觉）/ `T014`（世界模型）

## 一句话

> **开创性工作**：首次将 3D 感知、推理、动作和生成式世界模型统一在单一 3D-LLM 框架中，通过交互 token 操作 3D 环境。

## 核心方法

### 1. 基于 3D-LLM 的统一架构
- 以三维 LLM 为骨干，通过**交互 token**（interaction tokens）操作 3D 环境
- 统一 3D 感知 → 推理 → 动作生成的 pipeline

### 2. 生成式世界模型
- 内嵌**扩散模型**预测目标图像和点云
- 不仅执行动作，还能"想象"动作后的环境变化

### 3. 大规模 3D 具身指令数据集
- 从现有机器人数据集提取 3D 信息
- 构建大规模 3D embodied instruction 数据

## 实验结果

- held-in 数据集验证
- 显著提升推理、多模态生成和规划能力
- （早期工作，实验规模有限）

## 价值定位

- **VLA + 世界模型 + 3D 的开创性融合**：后续 OG-VLA、3D-Mix、GaussianDream 均可视为其延伸
- 提出了 3D-VLA 的基本框架：感知 → 世界模型 → 动作
- 为 [[paper-2026-108-rynnworld-4d]]（4D 世界模型）和 [[paper-2026-056-gaussiandream-3d-vla]]（3D 高斯世界模型）奠定概念基础

## 局限性

- 2024 年早期工作，实验规模有限
- 仅在 held-in 数据测试，泛化性未充分验证
- 系统复杂度高，推理效率未讨论

## 引用页

- [[concept-t008-3d-vla]] — 3D 视觉增强 VLA 选题
- [[concept-t014-wm]] — 世界模型选题总览
- [[paper-2025-002-og-vla]] — 后续 3D-aware VLA 工作
