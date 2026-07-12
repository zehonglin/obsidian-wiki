---
title: "World Models and World Action Models (WAM) 综述"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [survey, model, training, vla]
sources: [raw/papers/2026-022-wam-survey-world-models.md]
arxiv: "W7160423702"
date: 2026-05-06
related_topics: [T008, T009, T010]
authors: "Xin Jin et al."
source_db: "OpenAlex"
confidence: high
---

# WAM 综述论文

**作者**：Xin Jin 等  
**日期**：2026-05-06  
**来源**：OpenAlex  
**关联选题**：`T008`（3D 视觉增强）/ `T009`（VLA 安全）/ `T010`（数据效率）

## 一句话

> 综述 200+ 论文，统一分类世界模型/WAM，提出**六大支柱**框架（基础模型 / VLA / 统一生成与动作 / 自动驾驶 / 效率与评测 / 数据生态）。

## 六大支柱

| # | 支柱 | 关键内容 |
|---|---|---|
| 1 | **基础模型** | 通用模拟器（Genie, Cosmos, Sora）；游戏环境（Oasis, Matrix-Game） |
| 2 | **VLA 模型** | 架构演进（RT-2, π₀, OpenVLA）；驾驶专用 VLA；操作策略 |
| 3 | **统一生成与动作** | 零样本策略；可控仿真；学习范式 |
| 4 | **自动驾驶** | 视频生成；闭环仿真；规划；几何占据 / BEV 表示 |
| 5 | **效率与评测** | 计算加速；评测协议；合理性验证 |
| 6 | **数据集与生态** | 机器人学习语料；行业技术报告 |

## 关键观察

- 从**像素预测器**到**主动推理模拟器**的进化路径
- 预测性世界模拟 + 动作驱动多模态推理 = WAM
- **明确指出安全验证是 T009 的关键开放挑战**
- **跨机器人泛化（cross-embodiment）+ sim-to-real 评测差距仍是 T010 的核心问题**

## 价值定位

- 一篇概览整个 WAM 生态的"地图"
- 与 [[concept-t008-3d-vla]]（已有 5 篇首批论文）配套——综述 + 实证结合
- 与 [[concept-world-model-distillation]]（已有世界模型蒸馏概念）形成"概念-论文-综述"三层

## 局限性

- 综述文章，非原创方法
- 快速发展的领域，部分最新工作可能未覆盖
- 部分二级目录链接已 404（OpenAlex 引用）

## 引用页

- [[concept-t008-3d-vla]]
- [[concept-world-model-distillation]]
