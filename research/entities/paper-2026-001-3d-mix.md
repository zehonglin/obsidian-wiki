---
title: "3D-Mix: VGGT 3D 信息注入 VLA 的即插即用模块"
created: 2026-07-11
updated: 2026-07-11
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, spatial-reasoning, mllm]
sources: [raw/papers/2026-001-3D-Mix.md]
arxiv: "2603.24393"
date: 2026-03-25
related_topic: T008
confidence: high
---

# 3D-Mix 论文

**作者**：Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Haishan Liu, Changti Wu, Hang Yuan, Bailing Wang, Cong Huang, Kai Chen
**日期**：2026-03-25 | arXiv: 2603.24393
**研究方向**：`T008`（3D+VLA）

## 核心一句话

> 把 VGGT 输出的 3D 高斯几何特征，用**语义条件门控**方式注入 VLA 的 MLLM，增强 3D 感知能力，**不修改原模型任何参数**。

## 关键创新

1. **系统比较 9 种 VGGT-VLA 融合方案**——首次给出实证基准
2. **语义条件门控融合**——根据任务上下文自适应平衡 2D/3D 特征权重
3. **即插即用**——同时兼容 GR00T-style 和 π₀-style VLA 架构

## 实验结果

| 基准 | 提升 |
|---|---|
| OOD SIMPLER（9 个 GR00T-style 变体）| **+7.0% 平均** |
| LIBERO | 一致提升 |

跨 6 个 MLLM 系列、9 个模型变体（2B-8B）验证。

## 局限性（与本研究方向 T008 的差异化机会）

- ⚠️ 依赖 VGGT 离线重建，**实时性存疑**
- ⚠️ 仅桌面操作任务验证，未涉及灵巧操作/导航
- ⚠️ 未探索点云直接输入方案

## 关键引用 / 相关页

- [[concept-t008-3d-vla]]
- VGGT
- [[paper-2026-018-starry]] — 同一研究方向，提出 GASAM 注意力机制
- [[paper-2025-002-og-vla]] — 同一方向，用正交投影解决视角问题

## 相关 wiki 页

- 3D-Mix（entity 简称别名页）
