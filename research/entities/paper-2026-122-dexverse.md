---
title: "DexVerse: 多任务多本体灵巧操作模块化基准"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [benchmark, manipulation, dataset, evaluation]
sources: [raw/papers/2026-122-dexverse-benchmark.md]
arxiv: "2607.08751"
date: 2026-07-09
related_topic: T011
confidence: high
---

# DexVerse 论文

**作者**：Yunchao Yao, Zhuxiu Xu, Tianqi Zhang, Zixian Liu, Sikai Li, et al.（15 authors）
**日期**：2026-07-09 | arXiv: 2607.08751v1
**研究方向**：`T011`（Manipulation / Dexterous Benchmark），交叉 `T010`（数据效率）

## 核心一句话

> 大规模模块化灵巧操作基准：**100 个任务 + 3 臂 6 手 + 可配置视觉变化**，揭示 OpenVLA / π₀.₅ 等模型在跨任务泛化上的显著不足。

## 关键创新

1. **100 个任务 8 大类**——抓取重置、铰接物体交互、工具使用、双臂协调、非抓取控制、接触丰富行为、多目标执行、长时程多阶段
2. **多本体支持**——3 个机械臂 + 6 个灵巧手，可扩展新本体
3. **可配置视觉变化**——纹理、背景、光照、相机视角四维度可控
4. **VR 遥操作数据**——3,180 条多模态示范（本体感知 + RGB + 深度 + 点云 + 状态）

## 实验结果

| 模型 | 发现 |
|---|---|
| Diffusion Policy / DP3 | 基线表现 |
| OpenVLA | 跨任务泛化困难 |
| π₀.₅ | 同样存在显著泛化挑战 |

结论：**任务泛化和视觉运动鲁棒性仍是重大挑战**，确立 DexVerse 作为通用灵巧操作测试平台的价值。

## 局限性

- ⚠️ 主要面向仿真环境，sim-to-real gap 未完全覆盖
- ⚠️ 3 臂 6 手虽多，但真实机器人形态更多样
- ⚠️ 任务虽丰富，但可能无法完全反映真实世界的复杂物理交互

## 价值定位

DexVerse 是灵巧操作领域**最全面的模块化基准之一**（2026-07 最新），其多本体设计直接服务于跨机器人适配研究。对评估 [[paper-2026-038-dexora]] 等灵巧 VLA 模型具有直接价值。

## 相关页

- [[concept-t011-manipulation]]
- [[paper-2026-038-dexora]] — 可直接在 DexVerse 上评测
- [[paper-2026-063-libero-safety]] — LIBERO 系列基准对比（安全 vs 灵巧）
- [[concept-t010-data-efficiency]] — 多本体设计支撑少样本跨机器人适配研究
