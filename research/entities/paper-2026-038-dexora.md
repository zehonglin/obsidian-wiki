---
title: "Dexora: 开源高自由度双臂灵巧 VLA 系统"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, dataset]
sources: [raw/papers/2026-038-Dexora-bimanual-dexterous-VLA.md]
arxiv: "2605.18722"
date: 2026-05-18
related_topic: T011
confidence: high
---

# Dexora 论文

**作者**：Zongzheng Zhang, Jingrui Pang, Zhuo Yang, Kun Li, et al.（清华 + BAAI + 港大 + 上交 + 北大）
**日期**：2026-05-18 | arXiv: 2605.18722 | ICRA 2026
**研究方向**：`T011`（Manipulation / Dexterous），交叉 `T010`（数据效率）

## 核心一句话

> 首个面向 **36-DoF 双臂双灵巧手**的开源 VLA 系统，混合遥操作管线 + 数据质量感知训练，灵巧任务成功率 **66.7%**（+15%）。

## 关键创新

1. **混合遥操作管线**——外骨骼背包捕获粗手臂运动 + Apple Vision Pro 无标记手指追踪，实现 36-DoF 数据采集
2. **数据质量感知训练**——离线判别器对 10 万仿真 + 1 万真实轨迹质量打分，降权低质量演示
3. **跨本体泛化**——同一策略迁移至单臂夹爪、双臂夹爪、低 DoF 手，验证 embodiment-agnostic 能力
4. **MuJoCo 数字孪生**——仿真-真实互补数据管线，200 个任务覆盖

## 实验结果

| 指标 | 结果 |
|---|---|
| 基础任务成功率 | **90%** |
| 灵巧任务平均成功率 | **66.7%** vs 基线 51.7%（**+15%**） |
| 数据规模 | 6.5M 仿真帧 + 2.92M 真实帧 |
| 跨本体迁移 | 有效（单臂/双臂/灵巧手） |

## 局限性

- ⚠️ 依赖专用硬件（外骨骼 + Vision Pro），数据采集门槛高
- ⚠️ 仅桌面场景，未涉及移动操作
- ⚠️ 仿真-真实 gap 未完全消除

## 价值定位

Dexora 是**双臂灵巧 VLA 的开源标杆**（ICRA 2026），在数据规模、质量评估、跨本体迁移三方面推进了领域。其数据质量感知训练思路与 [[concept-t010-data-efficiency]] 直接呼应。

## 相关页

- [[concept-t011-manipulation]]
- [[paper-2026-033-handitl]] — 同为双臂灵巧 VLA，关注人机交互修正
- [[paper-2026-122-dexverse]] — 灵巧操作评测基准，可直接评测 Dexora
- [[concept-t010-data-efficiency]] — 数据质量感知训练
