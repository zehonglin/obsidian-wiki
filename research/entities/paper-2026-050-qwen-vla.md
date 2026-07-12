---
title: "Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation, navigation, mllm]
sources: [raw/papers/2026-050-Qwen-VLA.md]
arxiv: "2605.30280"
date: 2026-05-28
related_topic: T008, T009, T010
confidence: high
---

# Qwen-VLA 论文

**作者**：Qiuyue Wang, Mingsheng Li, Jian Guan, Jinhui Ye, ... （Qwen 团队）
**日期**：2026-05-28 | arXiv: 2605.30280
**研究方向**：`T008` + `T009` + `T010`

## 核心一句话

> 统一 VLA 基础模型，通过 DiT-based action decoder 和 embodiment-aware prompt conditioning，将操作、导航、轨迹预测统一到同一框架，跨任务/环境/机器人平台泛化。

## 关键创新

1. **统一具身基础模型**——扩展 Qwen 视觉语言建模栈，支持连续动作和轨迹生成
2. **大规模联合预训练**——融合机器人操作轨迹、egocentric 演示、合成仿真数据、VLN 数据
3. **Embodiment-aware Prompt Conditioning**——通过机器人特定文本描述指定当前 embodiment，支持多平台
4. **统一动作-轨迹预测**——操作 + 导航 + 轨迹预测统一到同一框架

## 实验结果

| 基准 | 成绩 |
|---|---|
| LIBERO | **97.9%** |
| Simpler-WidowX | 73.7% |
| RoboTwin-Easy/Hard | 86.1% / 87.2% |
| R2R 导航 | 69.0% OSR |
| RxR 导航 | 59.6% SR |
| 真实 ALOHA OOD | 76.9% 平均 |

## 价值定位

Qwen-VLA 是 VLA 统一化的里程碑工作——首次在单一模型中同时覆盖操作和导航。被 [[paper-2026-127-vla-survey-manipulation]]（VLA 操作综述）引用为 Qwen-VL 骨干代表。与 [[paper-2026-104-qwen-robotmanip-alignment]] 同属 Qwen VLA 系列，后者专注操作对齐。

## 局限性

- 模型规模大，部署成本高
- 动态操作零样本性能仍然较低（DOMINO 26.6%）
- 跨 embodiment 迁移能力有待进一步验证

## 关键引用 / 相关页

- [[concept-vla-model]]
- [[concept-t010-data-efficiency]]
- [[paper-2026-104-qwen-robotmanip-alignment]] — 同系列，操作专精
- [[paper-2026-115-internvla-a15]] — 同为 VLA 基础模型竞争者
