---
title: "T013 选题总览：导航与运动（Navigation / Locomotion）"
created: 2026-07-12
updated: 2026-07-12
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [navigation, manipulation, vla, survey, reinforcement-learning, imitation-learning]
sources: [raw/papers/2026-006-MetaNav.md, raw/papers/2026-052-uni-lavira.md, raw/papers/2026-073-moe-rl-fault-tolerant.md, raw/papers/2026-090-cwi-humanoid-locomanipulation.md, raw/papers/2026-091-booster-lab-data-centric.md, raw/papers/2026-093-VLK-humanoid-locomanipulation.md, raw/papers/2026-095-human-as-humanoid.md]
confidence: high
---

# T013：导航与运动（Navigation / Locomotion）

> **7 篇论文覆盖 3 条技术路线 + 2 个应用域，从零训练导航到人形 loco-manipulation。**

## 选题定义

T013 聚焦**机器人在空间中的自主移动能力**，包括：
- **导航（Navigation）**：从 A 到 B 的路径规划与执行（室内 VLN、室外探索）
- **运动（Locomotion）**：腿足/轮式/飞行的底层运动控制（四足行走、人形平衡）
- **Loco-manipulation**：行走 + 操作的协同（人形全身控制）

与 T008（3D 视觉增强）的区别：T008 关注**感知**（如何看懂 3D 空间），T013 关注**行动**（如何在空间中移动）。

## 7 篇论文矩阵

| 论文 | 子方向 | 核心方法 | 训练需求 | 交叉选题 |
|---|---|---|---|---|
| [[paper-2026-006-metanav]] | 室内导航 VLN | 元认知推理 + 3D 语义记忆 | 零训练 | — |
| [[paper-2026-052-uni-lavira]] | 统一导航 | 三层 Agent 解耦 + 跨 4 平台 | 零训练 | — |
| [[paper-2026-073-moe-rl-fault-tolerant]] | 腿足运动 | MoE 故障路由 + RL | RL 训练 | T009, T012 |
| [[paper-2026-090-cwi-humanoid-locomanipulation]] | 人形 loco-manip | 解耦策略 + Multi-critic AMP | IL + RL | T011 |
| [[paper-2026-091-booster-lab]] | 人形运动 | Data-centric pipeline + AMP | IL + RL | T010 |
| [[paper-2026-093-vlk]] | 人形 loco-manip | 3DGS 合成数据 + VLK 策略 | 监督学习 | T008, T010 |
| [[paper-2026-095-human-as-humanoid]] | 人形 loco-manip | 人类视频 → IK 重定向 | IL | T010, T011 |

## 三条技术路线

### 路线 A：零训练 / Training-free 导航
- **代表**：MetaNav、Uni-LaViRA
- **核心洞见**（来自 Uni-LaViRA）：导航动作在 MLLM 自然输出流形内 → 不需要端到端训练
- **关键机制**：元认知反思（MetaNav） / 架构解耦（Uni-LaViRA）
- **优势**：零数据采集、跨平台即插即用
- **瓶颈**：性能上限受基座模型限制，R2R 上仍落后训练方法 ~9pp

### 路线 B：合成 / 转换数据驱动
- **代表**：VLK（3DGS 合成）、Human-as-Humanoid（人类视频转换）
- **核心思路**：绕过遥操作低效率瓶颈，用自动化数据管线规模化
- **数据量级**：VLK 48K 轨迹零人工 / Human-as-Humanoid 吞吐量提升 4.8-7.2×
- **优势**：数据成本极低，可规模化
- **瓶颈**：3DGS 重建质量 / IK 重定向精度限制

### 路线 C：RL + 模块化控制
- **代表**：MoE-RL（故障容忍）、CWI（解耦策略）、Booster Lab（data-centric RL）
- **核心思路**：用 RL 优化运动策略，模块化设计处理多目标冲突
- **优势**：可处理训练方法无法覆盖的边缘场景（故障、复杂地形）
- **瓶颈**：sim-to-real gap，训练数据质量依赖

## 与其他选题的交叉

| 交叉选题 | 关联论文 | 关系 |
|---|---|---|
| **T008（3D+VLA）** | VLK | 3DGS 场景重建为导航提供空间感知基础 |
| **T009（安全/鲁棒性）** | MoE-RL | 故障容忍 = 安全性的另一维度 |
| **T010（数据效率）** | Booster Lab, Human-as-Humanoid, VLK | 数据规模化三条路线 |
| **T011（操作）** | CWI, Human-as-Humanoid | Loco-manipulation = 导航 + 操作 |
| **T012（RL 训练）** | MoE-RL, Booster Lab | RL 在 locomotion 中的应用 |

## 研究空白识别

1. **导航 × 操作深度耦合**——现有 loco-manipulation 多为「走到位置再操作」，真正的边走边操作（如行进中抓取）尚未解决
2. **跨域迁移**——室内 VLN 方法在户外复杂场景的迁移验证空白
3. **多机器人协作导航**——本文 7 篇均聚焦单机器人，多 agent 协同导航未涉及
4. **长期导航中的安全保证**——MetaNav 的元认知 + MoE-RL 的故障容忍都是局部方案，长期（>1h）导航的安全退化未系统研究

## 关键 wikilinks

- [[concept-t008-3d-vla]] — 3D 感知为导航提供输入
- [[concept-t009-safety-robustness]] — 导航安全是安全的子集
- [[concept-t010-data-efficiency]] — 数据效率在导航中的体现
- [[concept-t011-manipulation]] — Loco-manipulation 的操作维度
- [[concept-t012-rl-training]] — RL 在 locomotion 中的应用
- [[concept-world-model-distillation]] — 世界模型用于导航预测
