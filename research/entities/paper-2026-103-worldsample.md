---
title: "WorldSample：世界模型增强的真实机器人闭环 RL"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, training, reinforcement-learning]
sources: [raw/papers/2026-103-worldsample-real-robot-rl.md]
arxiv: "2607.02431"
date: 2026-07-02
related_topics: [T010, T012]
authors: "Yuquan Xue, Le Xu, Zeyi Liu, Zhenyu Wu, Zhengyi Gu, Xinyang Song, Bofang Jia, Ziwei Wang"
source_db: "arXiv"
confidence: high
---

# WorldSample 论文

**作者**：Yuquan Xue 等（王紫薇组）  
**日期**：2026-07-02 | arXiv: 2607.02431  
**关联选题**：`T010`（数据效率）、`T012`（RL Training）

## 核心一句话

> 在真实 rollout → 世界模型生成 → 策略改进之间建立**闭环**，用世界模型做物理奠基的数据增强，策略成功率提升 **28%**，训练步数减少 **59%**。

## 关键创新

1. **三阶段闭环** — 真实 rollout 收集物理数据 → 世界模型后训练生成高保真合成转移 → 合成数据增强策略训练
2. **Policy-Paced Learning (PPL)** — 通过样本选择和调度调节训练过程，平衡有用增强和价值过估计，减轻世界模型幻觉引入的噪声
3. **世界模型后训练** — 基于真实 rollout 微调世界模型，大幅降低视觉幻觉（PSNR +19.4dB, SSIM +0.47）

## 实验结果

| 指标 | 数值 |
|---|---|
| 策略成功率提升 | **+28%** |
| 训练步数减少 | **59%** |
| 世界模型 PSNR | **+19.4dB** |
| 世界模型 SSIM | **+0.47** |
| 任务类型 | 接触丰富 + 精密操作 |

## 局限性

- ⚠️ 世界模型质量直接决定增强效果
- ⚠️ 仍需一定量的真实 rollout（非零交互成本）
- ⚠️ PPL 调度参数需调优

## 价值定位

WorldSample 与 [[paper-2026-020-world-env]] 代表两种不同的"世界模型 + RL"思路：World-Env 用世界模型**替代**真实环境做 RL，WorldSample 用世界模型**增强**真实数据做 RL。WorldSample 的闭环设计更安全（始终有真实数据锚定），但成本更高。

## 相关页

- [[concept-t012-rl-training]]
- [[paper-2026-020-world-env]] — 直接对比：替代 vs 增强真实环境
- [[paper-2026-097-z1]] — Z-1 纯仿真 GRPO，WorldSample 用真实+合成混合
- [[paper-2026-021-motubrain]] — MotuBrain 的世界动作模型可为 WorldSample 提供更好的世界模型
- [[paper-2026-060-memorywam]] — MemoryWAM 的持久记忆与 WorldSample 的世界模型互补
- [[concept-t010-data-efficiency]]
