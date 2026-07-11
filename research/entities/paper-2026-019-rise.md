---
title: "RISE: 用组合世界模型做机器人策略自我改进"
created: 2026-07-11
updated: 2026-07-11
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, reinforcement-learning, self-supervised]
sources: [raw/papers/2026-019-RISE.md]
arxiv: "2602.11075v2"
date: 2026-02-11
venue: RSS 2026
related_topic: [T008, T010]
confidence: high
---

# RISE 论文

**作者**：Jiazhi Yang, Kunyang Lin, et al.（OpenDriveLab 团队）
**日期**：2026-02-11（v2: 2026-04-28）| arXiv: 2602.11075v2
**会议**：RSS 2026
**研究方向**：`T008`（3D+VLA）+ `T010`（VLA 数据效率）
**官网**：https://opendrivelab.com/RISE/

## 核心一句话

> 用**组合式世界模型**（动力学 + 价值两个子模型）在**想象空间**做策略自我改进——闭环生成 rollout、估计优势、在想象空间更新策略，**无需物理交互**。

## 三个核心组件

| 组件 | 作用 |
|---|---|
| **可控动力学模型** | 预测多视角未来 |
| **进度价值模型** | 评估想象结果，算信息量优势 |
| **闭环自我改进管线** | 想象 rollout → 评估优势 → 在想象空间更新策略 |

## 实验结果（真实世界）

| 任务 | 性能提升 |
|---|---|
| 动态砖块排序 | **+35%** |
| 背包打包 | **+45%** |
| 纸箱关闭 | **+35%** |

## 局限性

- ⚠️ 世界模型质量 = 策略改进上限
- ⚠️ 多视角预测开销大
- ⚠️ 组合设计增加系统复杂度

## 与其它论文关系

- vs [[paper-2026-018-starry]]：同样引世界模型，RISE 用组合（动力学+价值分开），STARRY 用统一扩散
- vs [[paper-2026-013-world2vlm]]：RISE 在**想象空间更新策略**，World2VLM 在**想象空间训练 VLM**——一个训模型、一个训策略

## 关键引用

- RSS 2026 接收
- OpenDriveLab 团队作品
