---
title: "VLA 部署综述：A Review Towards Real-World Applications"
created: 2026-07-12
updated: 2026-07-12
forward_ref_fixed: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [survey, vla, benchmark, dataset]
sources: [raw/papers/2026-126-VLA-Review-RealWorld.md]
doi: "10.1109/access.2025.3609980"
date: 2025
related_topics: [T008, T009, T010, T011]
authors: "Kento Kawaharazuka, Jihoon Oh, Jun Yamada, Ingmar Posner, Yuke Zhu"
source_db: "IEEE Access"
confidence: high
---

# VLA 部署综述论文（Real-World Applications 视角）

**作者**：Kento Kawaharazuka¹, Jihoon Oh¹, Jun Yamada², Ingmar Posner², Yuke Zhu³  
¹U Tokyo, ²U Oxford, ³UT Austin  
**日期**：2025 | **发表**：IEEE Access  
**项目页**：[vla-survey.github.io](https://vla-survey.github.io/)  
**关联选题**：`T008`（3D-VLA）/ `T009`（安全）/ `T010`（数据效率）/ `T011`（操作）

## 一句话

> 从**实际部署**视角系统综述 VLA，覆盖架构演进、模态处理、学习范式、机器人平台、数据采集策略与评测基准，提供交互式可搜索 VLA 数据库。

## 六大核心维度

| 维度 | 关键内容 | 与 wiki 选题交叉 |
|---|---|---|
| **架构演进** | 分离模型 → 统一 VLA 架构的过渡 | T008, T014 |
| **构建模块** | 骨干网络（LLM/VLM）、动作头设计 | T008 |
| **模态处理** | 视觉编码器、语言理解、动作表征 | T011 |
| **学习范式** | 预训练 → 微调 → 对齐 | T010, T012 |
| **机器人平台** | Franka, UR, AgileX ALOHA, xArm 等 | T011, T013 |
| **数据生态** | Open X-Embodiment, DROID, 遥操作管线 | T010 |

## 特色：交互式综述表

项目页提供**可搜索/筛选的 VLA 模型数据库**：
- 按**任务类型**过滤（导航/操作/交互）
- 按**模态**过滤（RGB/RGBD/点云/触觉）
- 按**机器人平台**过滤
- 按**骨干网络**排序

## 价值定位

- **部署视角**：不同于纯学术综述，聚焦真实世界落地的工程问题
- **实用指南**：数据采集策略、硬件选型、评估方法一应俱全
- **资源整合**：交互式表格是快速查找相关工作的最佳工具
- 补充 [[paper-2026-125-vla-survey-embodied-ai]] 的学术分类法，形成**理论+实践**双视角

## 与已录入论文的交叉

- **机器人平台**部分涵盖 T011 论文中使用的所有平台（Dexora 双臂、FurnitureVLA 家具组装）
- **数据采集**部分与 T010 选题的 [[paper-2026-079-abc-scalable-behavior-cloning]]（ABC-130K 数据集）直接相关
- **安全部署**部分与 T009 的 [[paper-2026-046-pre-vla]]（运行时验证）交叉

## 局限性

- 综述文章，非原创方法
- 交互式表格需手动维护，可能滞后于最新工作
- 部署案例集中于工业/服务机器人，特种场景覆盖有限

## 相关综述（姊妹篇）

- [[paper-2026-125-vla-survey-embodied-ai]] — VLA 学术综述（IEEE TNNLS）
- [[paper-2026-127-vla-survey-manipulation]] — VLA 操作综述（五维度）
- [[paper-2026-022-wam-survey]] — WAM 综述

## 引用页

- [[concept-t009-safety-robustness]]
- [[concept-t010-data-efficiency]]
- [[concept-t011-manipulation]]
