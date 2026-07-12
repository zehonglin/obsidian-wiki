---
title: "Bridge-WA：世界模型知识蒸馏增强 VLA 泛化"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, training]
sources: [raw/papers/2026-107-bridge-wa.md]
arxiv: "2607.02195"
date: 2026-07-07
related_topics: [T008, T010, T014]
authors: "未详细列出"
source_db: "arXiv"
confidence: medium
---

# Bridge-WA 论文

**日期**：2026-07-07 | arXiv: 2607.02195  
**关联选题**：`T008`（3D 视觉）/ `T010`（数据效率）/ `T014`（世界模型）

## 一句话

> 将**冻结的未来变化预测教师模型**蒸馏为三个紧凑先验模块（位置 + 变化 + 语义），通过 WorldBridge 注意力注入动作生成——OOD 视觉偏移场景泛化显著提升。

## 核心方法

### 1. 两阶段蒸馏框架
- **Stage 1**：冻结大规模未来变化预测模型作为教师，蒸馏出三个紧凑先验：
  - **位置先验**（where）：变化发生在哪
  - **变化先验**（how）：怎样变化
  - **语义先验**（what）：语义含义
- **Stage 2**：WorldBridge 多源注意力注入动作 Transformer

### 2. 轻量设计
- **不修改原始动作模型参数**
- 蒸馏先验模块参数量小，推理开销低
- 兼容任何 VLA 架构

### 3. 与世界模型蒸馏的关联
- 与 [[paper-2026-013-world2vlm]]（World2VLM）理念一致：将世界模型知识蒸馏到 VLA
- World2VLM 蒸馏空间想象力，Bridge-WA 蒸馏变化预测能力

## 实验结果

- 在 **VLABench、RoboTwin2.0、LIBERO-Plus** 三个仿真基准上均取得 SOTA 或接近 SOTA
- 真实机器人实验验证 sim-to-real 迁移
- **OOD 视觉偏移测试**中显著优于基线方法

## 价值定位

- **世界模型知识蒸馏的新范式**：不在线运行大世界模型，而是蒸馏为紧凑先验
- 与 [[paper-2026-013-world2vlm]]（世界模型→VLM 蒸馏）形成对照：
  - World2VLM：蒸馏**空间想象力**到 VLM
  - Bridge-WA：蒸馏**变化预测**能力到 VLA 动作头
- OOD 泛化能力对实际部署至关重要

## 局限性

- 蒸馏质量依赖教师模型的选择
- 三个先验的设计是否覆盖所有世界动态维度有待验证
- 论文细节待完整阅读

## 引用页

- [[paper-2026-013-world2vlm]] — 世界模型→VLM 蒸馏（概念类似）
- [[paper-2026-021-motubrain]] — 统一世界动作模型
- [[paper-2026-022-wam-survey]] — WAM 综述
- [[concept-t014-wm]] — 世界模型选题
- [[concept-world-model-distillation]] — 世界模型蒸馏概念
