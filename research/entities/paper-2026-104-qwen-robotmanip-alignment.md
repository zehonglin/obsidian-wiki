---
title: "Qwen-RobotManip: Alignment Unlocks Scale for Robotic Manipulation Foundation Models"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, training]
sources: [raw/papers/2026-104-qwen-robotmanip-alignment.md]
arxiv: "2606.17846"
date: 2026-06-16
related_topic: T008, T010
confidence: high
---

# Qwen-RobotManip 论文

**作者**：Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, ... Xiong-Hui Chen（Qwen 团队）
**日期**：2026-06-16 | arXiv: 2606.17846
**研究方向**：`T008` + `T010`

## 核心一句话

> 基于 Qwen-VL 的可泛化 VLA 基础模型，提出三维对齐框架（表征 + 运动 + 行为），用 38,100 小时人-机器人合成预训练语料，在所有 OOD 设置上大幅超越 π₀.₅。

## 关键创新

1. **三维对齐框架**——表征对齐（统一视觉-语言空间）+ 运动对齐（统一动作空间）+ 行为对齐（统一行为语义）
2. **人-机器人合成管线**——将自我中心手部演示转换为 15 个平台的机器人轨迹，仅用开源数据
3. **38,100 小时预训练语料**——LLM scaling recipe 首次系统性应用于机器人操作
4. **OOD 评测体系**——发现标准基准无法反映预训练质量，提出 RoboCasa365 / LIBERO-Plus / EBench / RoboTwin-Clean2Rand/IF/XE

## 实验结果

| 指标 | 成绩 |
|---|---|
| RoboChallenge 排名 | **第 1**（相对 π₀.₅ +20%）|
| 涌现能力 | 零样本指令跟随、扰动鲁棒性、反应式错误恢复、跨本体迁移 |
| 真实机器人验证 | AgileX ALOHA, Franka, UR, ARX |

## 价值定位

Qwen-RobotManip 代表了 VLA 大模型 scaling 的最新里程碑。被 [[paper-2026-127-vla-survey-manipulation]]（VLA 操作综述）引用为跨 15 平台预训练代表；被 [[paper-2026-128-embodied-ai-sae]]（Embodied AI 白皮书）引用为多机器人平台标准化范例。与 [[paper-2026-050-qwen-vla]] 同属 Qwen VLA 系列。

## 局限性

- 38,100 小时训练成本极高
- 人-机器人转换可能在复杂任务中失真
- 15 个平台仍不能覆盖所有机器人形态
- 技术报告形式，部分细节可能省略

## 关键引用 / 相关页

- [[concept-t010-data-efficiency]]
- [[concept-t008-3d-vla]]
- [[paper-2026-050-qwen-vla]] — 同属 Qwen VLA 系列，统一操作+导航
- [[paper-2026-079-abc-scalable-behavior-cloning]] — 数据基础设施互补
