---
title: "LIBERO-Safety：VLA 物理与语义安全综合基准（ECCV 2026）"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [vla, benchmark, dataset, evaluation]
sources: [raw/papers/2026-063-LIBERO-Safety-VLA-safety-benchmark.md]
arxiv: "2606.23686"
date: 2026-06-22
related_topics: [T009]
authors: "Rongxu Cui, Zongzheng Zhang, Jingrui Pang, Haohan Chi, Jinbang Guo et al."
source_db: "arXiv (ECCV 2026)"
confidence: high
---

# LIBERO-Safety 论文

**作者**：Rongxu Cui, Zongzheng Zhang, Jingrui Pang, Haohan Chi, Jinbang Guo et al.  
**日期**：2026-06-22 | arXiv: 2606.23686 | **ECCV 2026**  
**研究方向**：`T009`（VLA 安全）

## 核心一句话

> **首个参数化 VLA 安全基准**：程序化生成安全关键场景，含 19,664 条无碰撞演示，覆盖物理安全（碰撞/约束违反）和语义安全（指令误解/场景误判），系统评测 8 个 VLA + 2 个具身基础模型。

## 关键创新

1. **参数化安全场景生成**——支持全面随机化，克服遥操作数据瓶颈
2. **Keypose 驱动数据管道**——自动生成安全场景演示，无需人工遥操作
3. **大规模安全数据集**——19,664 条严格无碰撞演示 + 大量域随机化
4. **跨范式系统评测**——8 个 VLA 模型 + 2 个具身基础模型

## 实验结果

| 发现 | 内容 |
|---|---|
| **泛化-安全张力** | 高多样性训练促进更安全轨迹，但任务成功率下降 |
| 语义误解 | 是导致安全违规的重要原因 |
| 现有 VLA | 在安全关键场景下表现不佳 |

Project Page: https://libero-safety.github.io/

## 价值定位

- **安全评测基础设施**：为 T009 提供标准化评测工具
- 与 [[paper-2026-080-foresight-safety-vla]] 互补：LIBERO-Safety 侧重广度（物理+语义综合），ForesightSafety 侧重深度（诊断性 + 过程级度量）
- 发现的"泛化-安全张力"是 T009 的**核心研究问题**之一

## 局限性

- ⚠️ 仅 LIBERO 环境，真实世界迁移待验证
- ⚠️ Keypose 驱动生成的轨迹可能不同于人类遥操作
- ⚠️ 仅提供评测工具，未提出防御方法

## 引用页

- [[concept-t009-safety-robustness]]
- [[paper-2026-080-foresight-safety-vla]] — 诊断级安全基准
- [[paper-2026-096-oopsieverse]] — 物理损伤感知仿真
