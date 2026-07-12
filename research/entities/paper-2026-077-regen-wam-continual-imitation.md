---
title: "REGEN：WAM 生成式回放实现持续模仿学习"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, imitation-learning]
sources: [raw/papers/2026-077-regen-wam-continual-imitation.md]
arxiv: "2606.27374"
date: 2026-06-25
related_topics: [T010, T014]
authors: "Manish Kumar Govind, Dominick Reilly, Smit Patel, Hieu Le, Srijan Das"
source_db: "arXiv"
confidence: medium
---

# REGEN 论文

**作者**：Manish Kumar Govind, ... Srijan Das  
**日期**：2026-06-25 | arXiv: 2606.27374  
**关联选题**：`T010`（数据效率）/ `T014`（世界模型）

## 一句话

> 利用世界动作模型的**生成能力合成伪回放轨迹**，无需存储原始人类演示即可抵抗灾难性遗忘——遗忘减少最高 **50%**。

## 核心方法

### 1. Recurrent Generative Replay
- 递归查询 WAM，仅需**先前任务指令 + 当前任务观察**即可生成回放轨迹
- 完全替代原始演示存储

### 2. 持续学习闭环
- WAM 同时承担两个角色：**动作预测**（当前任务）+ **回放生成**（历史任务）
- 新任务学习时，WAM 自动排练已学任务

### 3. 无需经验回放缓冲区
- 传统持续学习需存储原始数据
- REGEN 用生成替代存储

## 实验结果

- 相比顺序微调，**灾难性遗忘减少最高 50%**
- 接近有特权经验回放方法的性能
- 仿真 + 真实世界操作验证

## 价值定位

- **WAM 的新应用场景**：世界模型不仅用于预测/规划，还能用于**持续学习**
- 与 [[paper-2026-060-memorywam]]（持久记忆 WAM）互补：MemoryWAM 用记忆解决长时序，REGEN 用生成解决持续学习
- 识别出 WAM 生成的核心瓶颈：**长时间程视觉退化**和**动作-观察不一致**

## 局限性

- WAM 生成质量随 horizon 增加而退化（视觉质量下降）
- 动作-观察一致性在复杂任务中难以保证
- 需要训练额外的 WAM 模型

## 引用页

- [[paper-2026-060-memorywam]] — 持久记忆 WAM
- [[paper-2026-021-motubrain]] — 统一世界动作模型
- [[paper-2026-022-wam-survey]] — WAM 综述
- [[concept-t014-wm]] — 世界模型选题
