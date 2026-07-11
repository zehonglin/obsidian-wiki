---
title: "世界模型蒸馏：用想象训练替代物理交互"
created: 2026-07-11
updated: 2026-07-11
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [training, self-supervised, vision-language, manipulation]
sources: [raw/papers/2026-013-World2VLM.md, raw/papers/2026-019-RISE.md, raw/papers/2026-018-STARRY.md]
confidence: medium
---

# 概念：世界模型蒸馏

## 定义

> 用一个**生成式世界模型**作为教师，把它对未来的"想象能力"**转移到下游策略**（VLM / VLA），让策略获得空间想象力，同时**避免推理时的生成开销**或**物理交互成本**。

## 三种实操形态（基于首批 5 篇）

| 形态 | 代表论文 | 蒸馏目标 |
|---|---|---|
| **蒸到 VLM** | [[paper-2026-013-world2vlm]] | 双向空间推理（动作↔结果）|
| **联合扩散时空+动作** | [[paper-2026-018-starry]] | 时空动作潜变量 |
| **组合世界模型 + 想象空间训练策略** | [[paper-2026-019-rise]] | 策略参数本身 |

## 共同价值

- 🚀 **训练成本下降**：物理交互 → 想象空间
- 🚀 **数据效率提升**：on-policy RL 的安全/硬件瓶颈绕开
- 🚀 **可扩展性**：世界模型可以无限 rollout

## 共同风险

- ⚠️ 世界模型质量 = 策略上限
- ⚠️ 现实与想象的 distribution gap
- ⚠️ 组合设计增加系统复杂度

## 还没人做的（潜在机会）

- 世界模型蒸馏 + 触觉/力觉信号
- 世界模型蒸馏 + 多机协作
- 世界模型蒸馏 + 长期任务（10+ 步）

## 相关 wiki 页

- 3 个 paper 实体页（见 sources）
- [[concept-t008-3d-vla]] — 该概念的主要应用场景
