---
title: "RynnVLA-002：统一 VLA 与世界模型的双向增强框架"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, architecture]
sources: [raw/papers/2026-057-rynnvla002-unified-vla-wm.md]
arxiv: "2511.17502"
date: 2025-11-21
related_topics: [T008, T010, T014]
authors: "Jun Cen, Siteng Huang, Yuqian Yuan, Kehan Li, Hangjie Yuan, Chaohui Yu, Bohan Hou, Yuming Jiang, Jiayan Guo, Xin Li, Hao Luo, Fan Wang, Deli Zhao, Hao Chen"
source_db: "arXiv"
confidence: medium
---

# RynnVLA-002 论文

**作者**：Jun Cen, Siteng Huang, ... Deli Zhao, Hao Chen  
**日期**：2025-11-21 (v1), 2026-05-30 (v3) | arXiv: 2511.17502  
**关联选题**：`T008`（3D 视觉）/ `T010`（数据效率）/ `T014`（世界模型）

## 一句话

> 将 **VLA 和世界模型统一在单一自回归模型**中，action generation 和 future state prediction **双向增强**——LIBERO 97.4%（无预训练），LeRobot 真实世界成功率提升 50%。

## 核心方法

### 1. 统一自回归框架
- VLA 分支：从图像观测生成动作
- 世界模型分支：利用 action + visual 输入预测未来图像状态
- 两者在单一模型中联合训练，共享表征

### 2. 双向增强机制
- **WM → VLA**：学习环境物理规律来优化 action generation
- **VLA → WM**：增强视觉理解，支持世界模型的图像生成

### 3. 无需预训练
- 直接达到高性能，说明世界模型引入提供了更好的数据效率

## 实验结果

| 基准 | 结果 |
|---|---|
| LIBERO（仿真） | 97.4% 成功率（无预训练） |
| LeRobot（真实世界） | 集成 WM 后总体成功率 **提升 50%** |

## 价值定位

- **VLA × WM 统一的旗舰工作**：证明了动作预测和世界动力学预测可以互相增强
- 与 [[paper-2026-021-motubrain]]（统一世界动作模型）方向一致，但 RynnVLA-002 更强调**双向增强**机制
- 与 [[paper-2026-022-wam-survey]]（WAM 综述）中的"联合训练"路线对应
- 为 [[paper-2026-108-rynnworld-4d]]（同团队 4D 世界模型）奠定基础

## 局限性

- v3 版本更新于 2026-05-30，尚未经过同行评审
- 真实世界实验仅在 LeRobot 平台验证，泛化性待考察
- 对 3D 空间感知的整合未涉及

## 引用页

- [[paper-2026-021-motubrain]] — 同为统一 WAM
- [[paper-2026-022-wam-survey]] — WAM 综述
- [[paper-2026-108-rynnworld-4d]] — 同团队后续 4D 工作
- [[concept-t014-wm]] — 世界模型选题
