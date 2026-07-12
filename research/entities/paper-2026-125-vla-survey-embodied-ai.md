---
title: "VLA 综述：A Survey on Vision-Language-Action Models for Embodied AI"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [survey, vla, mllm, architecture]
sources: [raw/papers/2026-125-VLA-Survey-Embodied-AI.md]
arxiv: "2405.14093"
date: 2024-05-22
related_topics: [T008, T009, T010, T011, T012, T013, T014]
authors: "Yueen Ma, Zixing Song, Yuzheng Zhuang"
source_db: "arXiv → IEEE TNNLS"
confidence: high
---

# VLA 综述论文（Embodied AI 视角）

**作者**：Yueen Ma, Zixing Song, Yuzheng Zhuang  
**日期**：2024-05-22（v1），2025 年更新至 v8  
**发表**：IEEE Transactions on Neural Networks and Learning Systems (TNNLS)  
**arXiv**：2405.14093 | **GitHub**：[Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA)  
**关联选题**：`T008`–`T014`（全覆盖）

## 一句话

> 首篇 VLA 综述，提出**三条研究路线**分类法（组件→控制策略→高层规划），系统梳理 VLA 架构、数据集、模拟器与评测基准。

## 三条研究路线分类法

| 路线 | 核心问题 | 代表工作 | 对应选题 |
|---|---|---|---|
| **组件级** | VLA 各模块（感知/语言/动作）如何设计？ | RT-2, OpenVLA backbone 分析 | T008 |
| **控制策略** | 如何预测低层动作？ | π₀, RDT-1B, Diffusion Policy | T011, T012 |
| **高层规划** | 如何分解长时程任务？ | SayCan, Inner Monologue | T011（长时程） |

## 覆盖范围

- **架构**：从 LLM-based → VLM-based → Native VLA 的演进
- **动作生成**：Token 预测 vs Diffusion vs Flow Matching
- **数据集**：Open X-Embodiment, DROID, RH20T 等
- **模拟器**：Habitat, AI2-THOR, RoboSuite, LIBERO 等
- **评测基准**：按任务类型（导航/操作/交互）分类

## 价值定位

- **领域地图**：一篇概览整个 VLA 生态，是进入 VLA 领域的首选入口
- **与我们选题体系的对应**：三条路线正好对应 T008（组件增强）→ T011（操作控制）→ T012（训练优化）
- 与 [[paper-2026-022-wam-survey]] 形成互补：本文侧重 VLA 架构分类，WAM 综述侧重世界模型生态
- 与 [[paper-2026-126-vla-review-realworld]] 互补：本文偏学术分类法，后者偏部署实践

## 局限性

- 综述文章，非原创方法
- 2024 年首发，部分 2025-2026 最新工作（如 MoE VLA、视频-动作预训练）未覆盖
- 分类法较宏观，对具体架构设计细节的对比有限

## 相关综述（姊妹篇）

- [[paper-2026-022-wam-survey]] — WAM 综述（200+ 论文，六大支柱）
- [[paper-2026-126-vla-review-realworld]] — VLA 部署综述（IEEE Access 2025）
- [[paper-2026-127-vla-survey-manipulation]] — VLA 操作综述（五维度）

## 引用页

- [[concept-t008-3d-vla]]
- [[concept-t011-manipulation]]
- [[concept-t012-rl-training]]
- [[concept-t014-wm]]
