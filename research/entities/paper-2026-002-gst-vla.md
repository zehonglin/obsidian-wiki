---
title: "GST-VLA：高斯空间 Token + 深度感知 Chain-of-Thought"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, spatial-reasoning, architecture, manipulation]
sources: [raw/papers/2026-002-GST-VLA.md]
arxiv: "2603.09079"
date: 2026-03
related_topic: T008
confidence: high
---

# GST-VLA 论文

**作者**：未详（arXiv 2603.09079）
**日期**：2026-03 | arXiv: 2603.09079
**研究方向**：`T008`（3D+VLA）

## 核心一句话

> 将深度图转化为 128 个各向异性 3D 高斯空间 Token，通过 DA-CoT（深度感知思维链）引导 VLA 进行显式空间推理，LIBERO 达 96.4%。

## 关键创新

1. **Gaussian Spatial Tokenizer (GST)**——冻结深度图 + 语义 patch → 128 个 3D 高斯基元（位置 μ∈R³、对数协方差 log σ∈R³、透明度 α），协方差编码表面朝向，透明度提供几何置信度
2. **空间注意力池化**——学习查询集中在几何显著区域，非均匀分布，有效压缩空间信息
3. **3D Depth-Aware CoT (DA-CoT)**——4 步结构化空间推理：3D 物体定位 → 抓取接触几何 → 成对度量距离 → 粗略 SE(3) 路点，每个 VLM transformer block 的 cross-attention 直接访问高斯基元
4. **300M flow-matching action expert + MoE FFN**——解码 7-DoF delta action chunks

## 实验结果

| 基准 | 成绩 | 提升 |
|---|---|---|
| LIBERO | 96.4% | +2.0% |
| SimplerEnv | 80.2% | +5.4% |

消融研究证实 GST 各组件、DA-CoT 各步骤、各训练阶段的独立和协同增益。

## 价值定位

GST-VLA 是 T008 主线的**直接竞品**——深度图→高斯 token 化的思路与 [[paper-2026-001-3d-mix]] 的 VGGT 特征注入形成两种截然不同的 3D 信息编码范式。DA-CoT 的显式空间推理步骤与 [[paper-2025-001-graphcot-vla]] 的图推理 CoT 可对比。

## 局限性

- ⚠️ 结果标注为 preliminary，实验仍在进行
- ⚠️ 仅桌面操作任务验证
- ⚠️ 深度图需预先提供（非端到端估计），与 [[paper-2026-034-evo-depth]] 的隐式深度估计形成对比

## 关键引用 / 相关页

- [[concept-t008-3d-vla]]
- [[paper-2026-001-3d-mix]] — VGGT 特征融合路线对比
- [[paper-2025-001-graphcot-vla]] — 图 CoT vs 高斯 CoT
- [[paper-2026-056-gaussiandream-3d-vla]] — 高斯世界模型，高斯表示另一应用
