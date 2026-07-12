---
title: "FurnitureVLA: 双臂家具组装的长时程 VLA"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, benchmark]
sources: [raw/papers/2026-110-furniturevla.md]
arxiv: "2607.01212"
date: 2026-07-07
related_topic: T011
confidence: high
---

# FurnitureVLA 论文

**作者**：未详细列出
**日期**：2026-07 | arXiv: 2607.01212
**研究方向**：`T011`（Manipulation / Long-horizon Bimanual）

## 核心一句话

> 首个系统性研究**双臂家具组装**的 VLA 模型，处理最多 7 个子任务、1550 步操作序列，进度增强架构实现子任务自动切换。

## 关键创新

1. **进度增强 VLA 架构**——引入进度估计模块，实时感知组装进度并自动触发子任务切换
2. **超长期任务处理**——1550 步操作序列，7 个子任务，远超一般 VLA 任务的时程
3. **层次化策略设计**——子任务分解 + 子任务内连续控制的双层架构
4. **Sim-to-real 验证**——仿真 + 真实 Kinova Gen3 机器人双环境验证

## 实验结果

| 指标 | 结果 |
|---|---|
| 仿真成功率 | 从 **48% → 80%** |
| 真实机器人 | sim-to-real 可行，最难任务下降 16% 但整体稳健 |
| 任务时程 | 最多 7 子任务、1550 步 |

## 局限性

- ⚠️ 最难任务真实环境成功率有 16% 下降
- ⚠️ 家具组装场景相对结构化，非结构化环境未验证
- ⚠️ 进度估计模块的鲁棒性在更长序列（>7 子任务）下未测试

## 价值定位

FurnitureVLA 将 VLA 的操作时程推到 **1550 步**的极致，是长时程双臂操作的标杆工作。其进度自动切换机制为工业装配场景提供了直接参考范式。

## 相关页

- [[concept-t011-manipulation]]
- [[paper-2026-106-cortex]] — 同为长时程操作，Cortex 用技能原语，FurnitureVLA 用进度估计
- [[paper-2026-038-dexora]] — 同为双臂操作，Dexora 关注灵巧，FurnitureVLA 关注长时程组装
- [[paper-2026-042-affordvla]] — 可供性感知可增强家具零件定位
