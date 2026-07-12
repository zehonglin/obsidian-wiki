---
title: "T010 选题：VLA 数据效率与少样本适配"
created: 2026-07-12
updated: 2026-07-12
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [training, vla]
sources: [raw/files-from-research-workspace/literature/directions/vla/data-efficiency.md]
related_papers: [paper-2026-020, paper-2026-021, paper-2026-060]
confidence: high
novelty: 高
feasibility: 高
---

# T010 选题：VLA 数据效率与少样本适配

## 一句话

> 用**极少量 demo** 让预训练 VLA 快速适配新任务和新机器人，降低 VLA 实际部署的数据门槛。

## 核心问题

VLA 微调需要大量数据，灾难性遗忘严重，跨机器人/跨任务泛化难。

## 研究空白

1. **跨机器人/跨任务的通用少样本适配框架缺乏**
2. **PEFT 方法**（LoRA / Adapter）在 VLA 上的系统对比不足
3. VLA 微调时的灾难性遗忘问题刚被触及
4. 主动学习在 VLA 场景下的探索空白
5. 少样本数据质量对适配效果的影响未被研究

## 切入点

1. **PEFT for VLA 系统对比** — LoRA / Adapter 等方法的 VLA 适配性评估
2. **元学习框架** — 让 VLA 快速适配新任务
3. **主动学习策略** — VLA 自动选择最有价值的 demo

## 三个最新工作的角度对比

| 论文 | 少样本数量 | 方法 |
|---|---|---|
| [[paper-2026-020-world-env]] | **5 demo** | 世界模型 + RL 后训练 |
| [[paper-2026-021-motubrain]] | **50-100 轨迹** | 跨机器人共享动作表示 |
| [[paper-2026-060-memorywam]] | 长时序记忆 | 持续记忆 + 混合设计 |

## 关联页

- [[paper-2026-022-wam-survey]] — WAM 综述明确指出 sim-to-real 是核心挑战
- [[concept-t008-3d-vla]]
