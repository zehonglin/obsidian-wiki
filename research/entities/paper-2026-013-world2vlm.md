---
title: "World2VLM: 把世界模型的空间想象力蒸馏到 VLM"
created: 2026-07-11
updated: 2026-07-11
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vision-language, spatial-reasoning, training]
sources: [raw/papers/2026-013-World2VLM.md]
arxiv: "2604.26934"
date: 2026-04-29
related_topic: T008
confidence: medium
---

# World2VLM 论文

**日期**：2026-04-29 | arXiv: 2604.26934
**研究方向**：`T008`（3D+VLA）
**笔记级别**：Level 1（摘要级）

## 核心一句话

> 用生成式世界模型当老师，把"空间想象力"**蒸馏到 VLM**，让 VLM 获得双向空间推理能力（动作→结果 / 结果→动作），且**推理时无需生成**。

## 关键特性

| 特性 | 说明 |
|---|---|
| **教师** | 生成式世界模型（生成视频作为训练信号）|
| **学生** | VLM |
| **蒸馏模式** | 学空间想象力 |
| **推理时延** | 无需生成步骤（快）|
| **推理方向** | 双向（forward + inverse）|

## 价值

- 推理效率高（直接出答案）vs [[paper-2026-018-starry]] 需扩散生成
- 双向推理对机器人规划有用（"做这动作会怎样" / "要这结果该做啥"）

## 待补内容

⚠️ 笔记是 Level 1（快速摘要）。老板 review 后若要深入，对比 [[paper-2026-019-rise]] 的想象空间训练思路。

## 相关 wiki 页

- [[concept-t008-3d-vla]]
- [[paper-2026-019-rise]] — 同样用世界模型做想象训练
