---
title: "Cortex: 双向对齐的具身智能体长时程操作框架"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, architecture]
sources: [raw/papers/2026-106-cortex-long-horizon-vla.md]
arxiv: "2607.05377"
date: 2026-07-06
related_topic: T011
confidence: high
---

# Cortex 论文

**作者**：Jiaqi Peng, Xiqian Yu, Delin Feng, Yuqiang Yang, Wenzhe Cai, Jing Xiong, Ganlin Yang, Jinliang Zheng, Jiafei Cao, Xueyuan Wei, Jiangmiao Pang, Yuan Shen, Tai Wang
**日期**：2026-07-06 | arXiv: 2607.05377v1
**研究方向**：`T011`（Manipulation / Long-horizon），交叉 `T010`（数据效率）

## 核心一句话

> 提出**双向对齐的 VLM+VLA 框架**，用 32 个标准化技能原语桥接高层规划与低层执行，实现零样本真实世界长时程操作。

## 关键创新

1. **32 个标准技能原语**——将操作子任务标准化，桥接高层 VLM 规划语义与低层 VLA 执行运动学
2. **可控性原则注入 + 自动标注 4k+ 小时视频**——大规模数据管线生成 30 小时仿真数据
3. **事件均衡采样策略**——解决子任务转换处的规划歧义
4. **推理时 harness 工程**——从任务上下文到技能约束的精心设计

## 实验结果

| 基准 | 提升 |
|---|---|
| LIBERO-long | **+3.1%** vs 单块基线 |
| RoboTwin | **+4.1%** vs 基线 |
| 真实世界 | **零样本**完成多阶段化学实验等长时程任务 |

关键发现：VLM + 微调 VLA 组合范式 > 纯 VLA 微调。

## 局限性

- ⚠️ 32 个技能原语粒度可能不足，无法覆盖所有任务类型
- ⚠️ 依赖大规模自动标注质量
- ⚠️ 开环 VLM 评估与闭环执行之间仍有差距

## 价值定位

Cortex 是**长时程操作 VLA** 的最新代表，其"双向对齐"思路（高层→低层 + 低层→高层）为解决 VLA 的马尔可夫假设局限提供了新范式。4k+ 小时视频自动标注管线对 [[concept-t010-data-efficiency]] 有直接参考价值。

## 相关页

- [[concept-t011-manipulation]]
- [[paper-2026-110-furniturevla]] — 同为长时程操作，FurnitureVLA 用进度估计，Cortex 用技能原语
- [[concept-t010-data-efficiency]] — 4k+ 小时自动标注管线
- [[paper-2026-022-wam-survey]] — WAM 综述框架可定位 Cortex 的分层设计
