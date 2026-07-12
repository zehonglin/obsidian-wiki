---
title: "MotuBrain：统一世界动作模型（WAM）用于机器人控制"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, mllm, training]
sources: [raw/papers/2026-021-motubrain-world-action-model.md]
arxiv: "2604.27792"
date: 2026-04-30
related_topics: [T008, T009, T010]
authors: "MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan et al."
source_db: "arXiv"
confidence: high
---

# MotuBrain 论文

**作者**：MotuBrain Team（含 Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan）  
**日期**：2026-04-30 | arXiv: 2604.27792  
**关联选题**：`T008`（3D 视觉）/ `T009`（VLA 安全）/ `T010`（数据效率）

## 一句话

> **统一世界动作模型（WAM）**：基于 UniDiffuser 框架，联合建模视频和动作，三流 Mixture-of-Transformers 架构，让单一模型支持策略学习、世界建模、视频生成、逆动力学、联合视频-动作预测。

## 关键创新

1. **三流 MoT 架构**（multi-view + text + action）
   - 视频流：处理纯视频、任务无关、跨机器人数据
   - 文本流：增强语言-动作耦合
   - 动作流：共享跨机器人动作表示
2. **统一多视角建模**：异构多模态数据同一模型处理
3. **高效推理栈**：50× 加速、11Hz 实时推理
   - 步数减少 + 编译 + FP8 量化
   - DiT 缓存 + V2A 动作推理 + 实时分块闭环执行

## 实验结果

| 基准 | 表现 |
|---|---|
| RoboTwin 2.0（清洁环境）| 95.8% 成功率 |
| RoboTwin 2.0（随机环境）| 96.1% 成功率 |
| WorldArena EWMScore | **最强** |
| 新人形机器人适配 | **仅需 50-100 条轨迹** |

## 价值定位

- **最全面的 WAM 实现**：比 [[paper-2026-018-starry]]（单流时空扩散）更通用
- **跨机器人适配成本**：50-100 条轨迹，**显著降低数据门槛**（呼应 T010）
- **世界模型可作为动作安全校验基础**（呼应 T009）

## 局限性

- 计算资源需求仍然较大
- 实验主要在仿真环境
- 长时序任务的闭环执行稳定性需进一步验证

## 引用页

- [[paper-2026-022-wam-survey]] — 同一系列综述
- [[paper-2026-060-memorywam]] — 同样的 WAM 思路，记忆增强版
- [[concept-t008-3d-vla]]
