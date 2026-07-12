---
title: "InternVLA-A1.5: 统一理解、潜在前瞻与动作"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, architecture]
sources: [raw/papers/2026-115-internvla-a15.md]
arxiv: "2607.04988"
date: 2026-07-10
related_topic: T008, T010, T014
confidence: high
---

# InternVLA-A1.5 论文

**来源**：arXiv 2607.04988v1
**日期**：2026-07-10
**研究方向**：`T008` + `T010` + `T014`

## 核心一句话

> 基于原生 VLM 骨干（Qwen3.5）构建策略，附加轻量级统一专家进行连续动作生成，提出「潜在前瞻（Latent Foresight）」将未来预测重构为潜在查询问题。

## 关键创新

1. **潜在前瞻（Latent Foresight）**——将未来预测重构为潜在查询问题，用少量可学习的前瞻 token 在冻结视频生成模型监督下，将任务相关未来压缩为紧凑潜在码
2. **世界模型动力学先验**——策略继承世界模型的动力学先验，无需学习像素级生成
3. **大规模训练**——120 万机器人 episode + 300 万多模态样本
4. **统一架构**——保持 VQA + 子任务预测 + 离散动作 token + 连续动作专家

## 实验结果

- 在 6 个仿真基准上取得**最佳整体结果**
- 基座模型：Qwen3.5 原生 VLM 骨干

## 价值定位

InternVLA-A1.5 的潜在前瞻思路连接了 VLA 与世界模型两个方向。被 [[paper-2026-127-vla-survey-manipulation]]（VLA 操作综述）引用为潜在前瞻架构代表。与 [[concept-t014-wm]]（世界模型选题）和 [[concept-t008-3d-vla]] 均相关。

## 局限性

- 技术报告信息有限（arXiv HTML 版本）
- 潜在前瞻 token 的可解释性有待研究
- 与 [[paper-2026-050-qwen-vla]] / [[paper-2026-104-qwen-robotmanip-alignment]] 的 Qwen 系列存在骨干竞争

## 关键引用 / 相关页

- [[concept-vla-model]]
- [[concept-t014-wm]]
- [[paper-2026-050-qwen-vla]] — 同为 VLA 基础模型，骨干竞争
- [[paper-2026-018-starry]] — 同为世界模型 + VLA 融合方向
