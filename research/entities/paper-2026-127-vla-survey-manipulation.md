---
title: "VLA 操作综述：Survey of VLA Models for Embodied Manipulation"
created: 2026-07-12
updated: 2026-07-12
forward_ref_fixed: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [survey, vla, manipulation, training, dataset]
sources: [raw/papers/2026-127-VLA-Survey-Manipulation.md]
arxiv: "2508.15201"
date: 2025-08-21
related_topics: [T008, T010, T011, T012]
authors: "Haoran Li, Yu-Hui Chen, Wenbo Cui"
source_db: "arXiv (中文)"
confidence: high
---

# VLA 操作综述论文（Embodied Manipulation 五维度）

**作者**：Haoran Li, Yu-Hui Chen, Wenbo Cui  
**日期**：2025-08-21（v1），2025-11-12（v2）  
**arXiv**：2508.15201（中文论文）  
**关联选题**：`T008`（3D-VLA）/ `T010`（数据效率）/ `T011`（操作）/ `T012`（RL 训练）

## 一句话

> 从**五个关键维度**（架构/数据/预训练/后训练/评测）全面综述 VLA 操作模型，梳理架构发展轨迹，是国内首篇系统性 VLA 操作综述。

## 五维度分析框架

| 维度 | 核心问题 | 代表工作 | 与 wiki 交叉 |
|---|---|---|---|
| **模型架构** | Transformer → Diffusion → Flow → MoE 演进 | RT-2, π₀, RDT-1B, [[paper-2026-115-internvla-a15]] | T008 |
| **训练数据** | 数据规模/多样性/采集方法 | Open X-Embodiment, DROID, ABC-130K | T010 |
| **预训练方法** | 表征对齐、多模态预训练策略 | LAION, OpenVLA pretrain | T010 |
| **后训练方法** | 微调、RL 对齐、安全约束 | GRPO, PPO, RLHF | T012 |
| **模型评测** | 基准设计、评估指标、跨本体泛化 | LIBERO, RoboCasa, SIMPLER | T011 |

## 核心贡献

- **架构发展轨迹**：从 ACT → RT-1/2 → OpenVLA → π₀ → 最新 MoE 架构的完整时间线
- **后训练方法聚焦**：与我们 T012 选题高度吻合，涵盖 SFT → RL → 安全约束全链路
- **中文撰写**：对国内学术圈和教学场景友好（老板可能在教学中引用）

## 价值定位

- **操作聚焦**：比通用 VLA 综述更深入操作领域，与 T011 的 7 篇论文直接对话
- **五维度框架**：可作为 T011/T012 选题论文的**分类锚点**——每篇论文定位到具体维度
- 与 [[paper-2026-125-vla-survey-embodied-ai]] 形成互补：前者通用分类法，本文操作专题深挖
- 与 [[paper-2026-022-wam-survey]] 形成姊妹关系：WAM 综述看"世界模型"，本文看"操作执行"

## 与已录入论文的系统化交叉

### 架构维度
- [[paper-2026-038-dexora]] — 36-DoF 双臂（MoE 方向）
- [[paper-2026-050-qwen-vla]] — Qwen-VL 骨干
- [[paper-2026-115-internvla-a15]] — 潜在前瞻架构

### 数据维度
- [[paper-2026-079-abc-scalable-behavior-cloning]] — ABC-130K 数据集
- [[paper-2026-104-qwen-robotmanip-alignment]] — 38,100 小时预训练语料

### 后训练维度
- [[paper-2026-097-z1]] — GRPO RL 后训练
- [[paper-2026-072-force]] — 三阶段 RL 微调框架
- [[paper-2026-067-dvla-rl]] — 离散扩散 VLA 的 RL

### 评测维度
- [[paper-2026-122-dexverse]] — 100 任务灵巧操作基准
- [[paper-2026-063-libero-safety]] — LIBERO 安全基准

## 局限性

- 中文论文，国际可见度可能受限（但有 arXiv 英文摘要）
- 新发表（2025-08），引用数尚少
- 五维度框架对**导航**和**世界模型**覆盖不足（聚焦操作）

## 相关综述（姊妹篇）

- [[paper-2026-125-vla-survey-embodied-ai]] — VLA 学术综述（三条研究路线）
- [[paper-2026-126-vla-review-realworld]] — VLA 部署综述（六大维度）
- [[paper-2026-022-wam-survey]] — WAM 综述（六大支柱）

## 引用页

- [[concept-t011-manipulation]]
- [[concept-t012-rl-training]]
- [[concept-t010-data-efficiency]]
