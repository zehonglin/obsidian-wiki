---
title: "VLA 模型总览（Vision-Language-Action Models）"
created: 2026-07-12
updated: 2026-07-12
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [vla, survey, model, architecture]
sources: []
related_topics: [T008, T009, T010, T011, T012, T013, T014]
confidence: high
status: stub
---

# VLA 模型总览（Vision-Language-Action Models）

> 🚧 **Stub 页面** — 跨选题综述入口，等专门 batch 扩展。
> 覆盖 T008-T014 全部 7 个选题。

## 简短定义

Vision-Language-Action（VLA）模型将视觉感知、语言理解和机器人动作生成统一在一个基础模型中。
核心思想：借鉴 LLM/VLM 的互联网规模预训练，直接输出机器人可执行动作。

**输入**：视觉观测 + 自然语言任务指令  
**输出**：末端执行器动作

## 已有的相关综述

- [[paper-2026-022-wam-survey]] — WAM 综述（T008/T009/T010 地图）
- [[paper-2026-125-vla-survey-embodied-ai]] — VLA 学术综述（IEEE TNNLS，三研究路线）
- [[paper-2026-126-vla-review-realworld]] — VLA 部署综述（IEEE Access）
- [[paper-2026-127-vla-survey-manipulation]] — VLA 操作综述（中文）
- [[paper-2026-128-embodied-ai-sae]] — 行业白皮书（SAE World Congress 2026）

## 已有的相关论文（部分）

- 首批 5 篇 T008 论文（3D 增强）：[[paper-2026-001-3d-mix]], [[paper-2025-002-og-vla]], [[paper-2026-013-world2vlm]], [[paper-2026-018-starry]], [[paper-2026-019-rise]]
- 全部 67+ 论文分布在 7 个选题中

## 待扩展

- [ ] VLA 架构演进史（RT-2 → OpenVLA → π₀ → ...）
- [ ] 各架构的优缺点对比
- [ ] VLA 与传统机器人控制（PID/阻抗控制）的边界
