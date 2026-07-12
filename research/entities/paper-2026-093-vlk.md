---
title: "VLK：从重建场景合成交互数据学习人形 Loco-Manipulation"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, navigation, manipulation, spatial-reasoning, dataset]
sources: [raw/papers/2026-093-VLK-humanoid-locomanipulation.md]
arxiv: "2606.30645"
date: 2026-06-29
related_topic: T013
confidence: high
---

# VLK 论文

**作者**：Yen-Jen Wang, Jiaman Li, Sirui Chen, Pieter Abbeel, Rocky Duan, Koushil Sreenath 等
**日期**：2026-06-29 | arXiv: 2606.30645
**研究方向**：`T013`（Navigation / Locomotion），交叉 `T008`（3D 视觉）、`T010`（数据效率）

## 核心一句话

> 用 **3D Gaussian Splatting** 重建室内场景 → 合成 48,000 条导航+交互轨迹 → 渲染配对 egocentric 观测 → 训练 Vision-Language-Kinematics 策略，零人工干预在 Unitree G1 上部署。

## 关键创新

1. **VLK 数据合成 pipeline**——3DGS 场景重建 → privileged 轨迹规划 → 事后渲染第一人称视角，48K 轨迹零人工
2. **VLA → VLK 转换**——用运动学轨迹替代底层动作，降低跨平台迁移难度
3. **Whole-body tracker**——将 VLK 策略输出的短时运动学轨迹转化为机器人关节动作
4. **三位一体**——导航 + 单物体运输 + 语言指令统一在同一策略内

## 实验结果

- Unitree G1 物理平台：导航和单物体运输成功验证
- 48,000 条配对轨迹，零人工采集成本
- Sim-to-real 迁移成功

## 价值定位

VLK 是 [[concept-t013-navigation]] 与 [[concept-t008-3d-vla]] 的关键交叉点。3DGS 合成数据方法为 locomotion 研究提供了可规模化的数据来源，与 Booster Lab（[[paper-2026-091-booster-lab]]）的真实数据筛选路线互补。

## 局限性

- ⚠️ VLK 将 action space 提升到运动学层面，对底层控制关注较少
- ⚠️ 3DGS 重建质量直接影响合成数据质量
- ⚠️ 仅验证导航和单物体运输，多物体交互未测

## 相关 wiki 页

- [[concept-t013-navigation]] — 本文所属选题总览
- [[concept-t008-3d-vla]] — 3D 视觉增强交叉
- [[paper-2026-090-cwi-humanoid-locomanipulation]] — 对比：CWI 用架构解耦解决类似问题
- [[paper-2026-001-3d-mix]] — 3D 信息注入 VLA 的另一路线（VGGT vs 3DGS）
- [[paper-2026-060-memorywam]] — 持久记忆 + 世界模型（导航中的记忆需求）
