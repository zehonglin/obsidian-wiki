---
title: "OG-VLA: 正交视图生成的 3D-aware 视觉-语言-动作模型"
created: 2026-07-11
updated: 2026-07-11
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, spatial-reasoning, vision-language]
sources: [raw/papers/2025-002-OG-VLA.md]
arxiv: "2506.01196"
year: 2025
related_topic: T008
confidence: high
---

# OG-VLA 论文

**作者**：et al.
**年份**：2025 | arXiv: 2506.01196
**研究方向**：`T008`（3D+VLA）

## 核心一句话

> 用**正交投影**把 RGBD 渲染成 canonical 视角图，再用扩散模型生成编码末端执行器位姿的图像，实现**视角不变的 3D-aware 动作输出**。

## 三步管线

```
RGBD → 反投影为点云 → 渲染正交视图（消除视角依赖）
                    ↓
视觉 backbone + LLM + 图像扩散
                    ↓
扩散生成图像编码末端的下一位置和姿态
```

## 实验结果

| 基准 | 提升 |
|---|---|
| Arnold / Colosseum（未见环境）| **+40% 相对提升** |
| 真实世界 3-5 demo 适配 | 成功 |
| 已见环境 | 保持鲁棒 |

## 局限性

- ⚠️ **正交投影丢透视深度信息**——关键 trade-off
- ⚠️ 需 RGBD 传感器（深度依赖）
- ⚠️ 图像生成式动作表示信息密度可能不足

## 与 T008 同方向论文对比

vs [[paper-2026-001-3d-mix]]：

| 维度 | OG-VLA | 3D-Mix |
|---|---|---|
| **3D 来源** | RGBD 点云（在线） | VGGT 多视角重建（离线）|
| **注入方式** | 生成视图（改变输入） | 门控融合（保留原输入）|
| **架构侵入性** | 中（需预渲染管线）| 低（即插即用）|
| **视角鲁棒性** | ⭐⭐⭐（设计核心）| ⭐⭐（OOD 提升 +7%）|

→ 两条互补路线：OG-VLA 改造输入，3D-Mix 改造中间表示。
