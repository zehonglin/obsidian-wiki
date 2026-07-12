---
title: "ICWM：上下文世界建模实现零微调跨环境适配"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, inference]
sources: [raw/papers/2026-071-icwm-in-context-world-model.md]
arxiv: "2606.26025"
date: 2026-06-24
related_topics: [T010, T014]
authors: "Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji, Jingjing Gong, Xipeng Qiu"
source_db: "arXiv"
confidence: medium
---

# ICWM 论文

**作者**：Siyin Wang, ... Xipeng Qiu (复旦大学)  
**日期**：2026-06-24 | arXiv: 2606.26025  
**关联选题**：`T010`（数据效率）/ `T014`（世界模型）

## 一句话

> 将**系统辨识转化为上下文适应问题**——机器人从短历史自生成交互中推断当前系统动态，**无需参数更新**即可适配新相机视角、新配置。

## 核心方法

### 1. In-Context World Modeling 框架
- 不同于传统 ICL 用演示告诉模型"做什么"，ICWM 利用上下文窗口理解"**系统如何运作**"
- 从任务无关的自生成交互中自主推断关键系统变量

### 2. 隐式世界动态捕获
- 通过处理自生成交互，模型隐式捕获当前系统的世界动态
- 无需参数更新实现对新配置的适应

### 3. 范式创新
- **系统辨识的神经化实现**：将经典控制理论的系统辨识思想迁移到 VLA 时代
- 与参数高效微调（LoRA/Adapter）形成互补：ICWM 适配配置，PEFT 适配任务

## 实验结果

- 仿真和真实机器人平台验证
- 在**新相机视角**上显著优于标准 VLA 基线
- 无需参数更新实现适配

## 价值定位

- **世界模型的非传统用法**：不用于生成未来帧，而用于**理解当前系统**
- 与 [[paper-2026-020-world-env]]（世界模型做 RL 后训练环境）互补：World-Env 用 WM 做训练环境，ICWM 用 WM 做推理时适配
- 为 VLA 的**零样本跨环境部署**开辟新路径

## 局限性

- 需要任务无关的探索交互，可能不适用于安全敏感场景
- 上下文窗口长度限制了可推断的系统复杂度
- 系统辨识精度依赖探索交互质量

## 引用页

- [[paper-2026-020-world-env]] — 世界模型做 RL 后训练环境
- [[paper-2026-021-motubrain]] — 统一世界动作模型
- [[concept-t014-wm]] — 世界模型选题
- [[concept-t010-data-efficiency]] — 数据效率选题
