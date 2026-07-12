---
title: "BORA: 灵巧 VLA 的离线-在线 RL 后训练框架"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, reinforcement-learning, training]
sources: [raw/papers/2026-053-bora-vla-dex-rl.md]
arxiv: "2605.30226"
date: 2026-05-28
related_topic: T011
confidence: high
---

# BORA 论文

**作者**：Zhongxi Chen, Yifan Han, Yanming Shao, Huanming Liu, Congsheng Xu, Xiaoyu Chen, Yao Mu, Wenzhao Lian
**日期**：2026-05-28 | arXiv: 2605.30226
**研究方向**：`T011`（Manipulation / Dexterous），交叉 `T009`（安全）、`T010`（数据效率）

## 核心一句话

> 提出**离线 RL + 在线残差适配**的 VLA 后训练框架，灵巧操作成功率绝对提升 **33%**，未见物体泛化提升 **43%**。

## 关键创新

1. **Consistency Policy 动作专家**——1-3 步生成动作 chunks，截断计算图实现高效梯度反传，解决生成式动作架构的信用分配问题
2. **Action-conditioned Critic**——融合 VLM 认知 tokens 和连续动作 chunks，避免 critic 因视觉遮挡过拟合背景特征
3. **冻结基座 + HiL 残差适配**——在线阶段冻结 VLA 基座防止灾难性漂移，轻量级残差 actor 从人类干预数据学习修正先验

## 实验结果

| 指标 | 提升 |
|---|---|
| 平均成功率（标准设置）| **+33%** 绝对提升 |
| 未见物体泛化 | **+43%** |
| 评测范围 | 5 个真实灵巧操作任务 |

显著优于纯模仿学习和传统解耦 RL 基线。

## 局限性

- ⚠️ 依赖人类干预数据（HiL），数据收集成本较高
- ⚠️ 仅灵巧手验证，其他形态未测试
- ⚠️ Consistency Policy 截断可能损失长程依赖

## 价值定位

BORA 是**灵巧 VLA + RL 后训练**的先驱工作，其"冻结基座 + 残差适配"范式与 PEFT 理念一致，为高 DoF 操作的可靠部署提供了可行路径。跨选题价值高：T011 核心 + T009 安全思路 + T010 数据效率。

## 相关页

- [[concept-t011-manipulation]]
- [[paper-2026-033-handitl]] — 同样使用人类干预数据，HandITL 关注在线修正，BORA 关注 RL 后训练
- [[paper-2026-038-dexora]] — Dexora 的数据质量感知训练可为 BORA 提供高质量离线数据
- [[concept-t009-safety-robustness]] — 冻结基座 + 残差修正的安全思路
- [[concept-t010-data-efficiency]] — HiL 残差适配是少样本在线适配方案
