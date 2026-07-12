---
title: "Human-as-Humanoid：从人类视频零样本迁移人形机器人技能"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, navigation, manipulation, imitation-learning, dataset]
sources: [raw/papers/2026-095-human-as-humanoid.md]
arxiv: "2606.32009"
date: 2026-06-30
related_topic: T013
confidence: high
---

# Human-as-Humanoid 论文

**作者**：Xiaopeng Lin, Ruoqi Yang, Shijie Lian, Zhaolong Shen 等 17 人
**日期**：2026-06-30 | arXiv: 2606.32009
**研究方向**：`T013`（Navigation / Locomotion），交叉 `T010`（数据效率）、`T011`（操作）

## 核心一句话

> 将 ego-exo 人类视频通过分级 IK 重定向转换为 60-DoF 人形机器人动作监督，数据吞吐量比遥操作提升 **4.8-7.2 倍**，无需目标任务机器人演示即可部署。

## 关键创新

1. **Human-as-Humanoid 转换框架**——同步自我中心（部署对齐）+ 外部（运动恢复）视频 → 分级 IK → 60-DoF 控制器对齐动作块
2. **FK 感知监督**——训练 VLA 时保持腕部和指尖任务空间几何，减少重定向误差传播
3. **基于 PrimeU**——60-DoF 上半身人形机器人，人类对齐的 embodiment 设计
4. **跨任务零样本部署**——仅用转换后人类标签训练，策略可直接迁移到真实机器人

## 实验结果

| 维度 | 结果 |
|---|---|
| 数据吞吐量 | 比遥操作提升 **4.8-7.2×** |
| 验证层面 | 运动恢复 + 动作空间 + 真实机器人部署 |
| 真实部署 | ✅ 无需目标任务机器人演示 |

## 价值定位

为 [[concept-t013-navigation]] 提供了 **数据规模化** 的关键方案。人类视频→机器人动作的转换 pipeline 直接回应 T010 数据效率核心问题（[[concept-t010-data-efficiency]]），与 VLK 的合成数据路线（[[paper-2026-093-vlk]]）互补。

## 局限性

- ⚠️ IK 重定向可能丢失人类运动的细微特性（如手指精细操控）
- ⚠️ 需要同步的多视角拍摄设置
- ⚠️ 需要人形机器人硬件设计接近人体比例（human-aligned embodiment）

## 相关 wiki 页

- [[concept-t013-navigation]] — 本文所属选题总览
- [[concept-t010-data-efficiency]] — 数据效率方法论交叉
- [[paper-2026-093-vlk]] — 对比：VLK 用 3DGS 合成 vs 本文用人类视频
- [[paper-2026-091-booster-lab]] — 对比：Booster Lab 筛选真实数据 vs 本文转换人类数据
- [[paper-2026-090-cwi-humanoid-locomanipulation]] — CWI 的 MoCap 数据路线对比
