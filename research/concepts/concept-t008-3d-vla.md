---
title: "T008 选题：3D 视觉增强 VLA 模型"
created: 2026-07-11
updated: 2026-07-12T18:00
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [vla, spatial-reasoning, manipulation, mllm]
sources: [raw/topics/topics.json]
related_papers: [paper-2026-001, paper-2025-002, paper-2026-013, paper-2026-018, paper-2026-019, paper-2025-001, paper-2026-002, paper-2026-017, paper-2026-030, paper-2026-034, paper-2026-039, paper-2026-055]
confidence: high
novelty: 高
feasibility: 高
---

# T008 选题：3D 视觉增强 VLA 模型

## 一句话定位

> 把 3D 空间理解能力注入 Vision-Language-Action 模型，让机器人在 3D 操作任务上鲁棒。

## 为什么这个方向重要

VLA 模型（如 GR00T、π₀）底层 MLLM 主要在 2D 数据训练，**空间智能不足**——遇到 3D 操作、视角变化、几何敏感任务容易翻车。

## 三条已收敛的技术路线（基于 5 篇首批 ingest）

### 路线 A：**改造中间表示**（特征融合）
代表：[[paper-2026-001-3d-mix]]
- 把 3D 几何特征注入 VLA 的中间层
- 即插即用，**不改原模型**
- 适合快速验证不同 VLA 架构

### 路线 B：**改造输入**（视图变换）
代表：[[paper-2025-002-og-vla]]
- 把 RGBD 渲染成视角不变的 canonical 视图
- 改变输入空间，让 VLA 看到一致的图
- 代价：丢透视深度信息

### 路线 C：**引入世界模型**（想象力）
代表：[[paper-2026-013-world2vlm]] + [[paper-2026-018-starry]] + [[paper-2026-019-rise]]
- 用世界模型给 VLA 提供"想象"的 3D 未来
- 子路线 C1：蒸馏到 VLM（World2VLM）
- 子路线 C2：联合扩散时空+动作（STARRY）
- 子路线 C3：组合世界模型 + 想象空间训练（RISE）

## 评测基准全景

| 基准 | 类型 | 代表使用 |
|---|---|---|
| **SIMPLER** | OOD 仿真 | 3D-Mix |
| **LIBERO** | 桌面操作 | 3D-Mix |
| **Arnold** | 未见环境 | OG-VLA |
| **Colosseum** | 视觉干扰 | OG-VLA |
| **RoboTwin 2.0** | 双手操作 | STARRY |
| **真实世界 3 任务** | 动态/接触密集 | RISE |

## 待老板裁决的差异化方向（来自 3D-Mix 论文）

1. **实时 3D 感知**（绕开 VGGT 离线重建）
2. **更精细的 3D-语言跨模态对齐**
3. **更泛化的场景验证**（不只是桌面）
4. **点云/深度图等替代 3D 表征**

## 相关综述

以下综述论文对 T008 选题有直接参考价值：

- [[paper-2026-125-vla-survey-embodied-ai]] — VLA 学术综述（三条研究路线分类法，T008 路线 A/B/C 对应组件级增强）
- [[paper-2026-126-vla-review-realworld]] — VLA 部署综述（架构演进+机器人平台视角）
- [[paper-2026-127-vla-survey-manipulation]] — VLA 操作综述（五维度框架中「模型架构」维度覆盖 T008）
- [[paper-2026-022-wam-survey]] — WAM 综述（路线 C 世界模型方向的顶层地图）

## 相关 wiki 页

- 12 个 paper 实体页（见 related_papers，含 Batch 10 新增 7 篇）
- [[concept-world-model-for-robotics]]
- [[concept-vla-model]]

---

## T008 论文技术路线分类（Batch 10 更新）

> Batch 10 补强后，T008 从 3 条路线扩展为 **8+ 条技术路线**，覆盖感知层→推理层→评测层。

| 技术路线 | 代表论文 | 核心思路 | 优势 | 局限 |
|---|---|---|---|---|
| **A. 特征融合** | [[paper-2026-001-3d-mix]] | VGGT 3D 高斯特征 → 门控注入 MLLM 中间层 | 即插即用，不改原模型 | 依赖离线重建，实时性存疑 |
| **B. 视图变换** | [[paper-2025-002-og-vla]] | RGBD → 正交 canonical 视图 | 视角不变，few-shot 强 | 丢透视深度信息 |
| **C. 世界模型想象** | [[paper-2026-013-world2vlm]], [[paper-2026-018-starry]], [[paper-2026-019-rise]] | 世界模型提供 3D 未来想象 | 生成式泛化，想象未见状态 | 世界模型本身训练成本高 |
| **D. 高斯 Token 化** | [[paper-2026-002-gst-vla]] | 深度图 → 128 个 3D 高斯基元 + DA-CoT 空间推理 | 显式几何编码 + 结构化推理 | 需预提供深度图 |
| **E. 图结构推理** | [[paper-2025-001-graphcot-vla]] | 3D Pose-Object 图 + 三层 CoT | 推理层增强，不改感知 | 依赖已知物体位姿 |
| **F. 检索增强** | [[paper-2026-017-rag-vlm-spatial]] | RAG 框架为 VLM 动态检索空间信息 | 不改架构，不增传感器 | 知识库构建成本，延迟 |
| **G. 多视角合成** | [[paper-2026-030-multiview-vla]] | 多视角扩散先验合成新视角 + 动作流形学习 | 从单目生成多视角，AML 高效 | 扩散模型质量上限 |
| **H. 隐式深度估计** | [[paper-2026-034-evo-depth]] | 从 RGB 隐式提取深度特征，0.9B 轻量参数 | 最轻量，无需额外传感器 | 隐式估计精度受限 |
| **I. 立体视觉** | [[paper-2026-055-stereopolicy-3d-vla]] | 双目 Stereo Transformer 融合，隐式视差 | 复用 2D 预训练，无需 3D 重建 | 需双目硬件 |
| **J. 主动评测** | [[paper-2026-039-esi-bench]] | 感知-动作闭环主动空间智能基准 | 揭示「动作盲」瓶颈 | 仅仿真环境 |

### 路线间关系图

```
感知层增强          推理层增强        评测
├─ A 特征融合        ├─ D DA-CoT      └─ J ESI-Bench
├─ B 视图变换        └─ E 图 CoT
├─ C 世界模型想象
├─ F 检索增强
├─ G 多视角合成
├─ H 隐式深度
└─ I 立体视觉
```

### Batch 10 关键洞察

1. **3D 信息注入方式已分化为 8+ 路线**——从显式重建（A）到隐式估计（H），从感知层（A/B/D/H/I）到推理层（E）到知识层（F）
2. **轻量化成为趋势**——Evo-Depth（0.9B）vs 3D-Mix（VGGT 离线重建）代表效率两端
3. **ESI-Bench 揭示根本性问题**——空间智能瓶颈可能在动作选择而非感知，质疑整个 T008 的隐含假设
4. **DA-CoT vs GraphCoT**——两条结构化空间推理路线（高斯 vs 图）值得对比研究
5. **立体视觉（I）可能是工程最优解**——平衡 2D 预训练复用与 3D 几何理解
