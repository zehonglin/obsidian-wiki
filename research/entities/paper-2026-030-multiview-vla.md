---
title: "MultiView-VLA：多视角潜空间先验 + 动作流形学习"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, spatial-reasoning, architecture, manipulation]
sources: [raw/papers/2026-030-MultiView-VLA-Action-Manifold.md]
arxiv: "2605.11832"
date: 2026-05
related_topic: T008
confidence: high
---

# MultiView-VLA（Action Manifold）论文

**作者**：Junjin Xiao, Dongyang Li, Yandan Yang, Shuang Zeng, Tong Lin, Xinyuan Chang, Feng Xiong, Mu Xu, Xing Wei, Zhiheng Ma, Qing Zhang, Wei-Shi Zheng
**日期**：2026-05 | arXiv: 2605.11832
**研究方向**：`T008`（3D+VLA）

## 核心一句话

> 利用预训练多视角扩散模型在潜空间合成新视角减少几何不确定性，并通过动作流形学习直接预测动作而非间接预测噪声/速度。

## 关键创新

1. **多视角扩散先验**——利用预训练多视角扩散模型在潜空间合成新视角，从单目输入减少深度模糊
2. **Geometry-Guided Gated Transformer (G³T)**——在单目 3D 几何先验引导下对齐多视角潜特征，自适应门控机制选择信息丰富的视角
3. **Action Manifold Learning (AML)**——基于"动作流形假设"，直接在动作流形上预测动作，绕过传统扩散/flow matching 的间接目标（噪声/速度），优化效率更高

## 实验结果

| 基准 | 表现 |
|---|---|
| LIBERO / LIBERO-Plus | 超越 SOTA |
| RoboTwin 2.0 | 超越 SOTA |
| 空间扰动 | 仅 8.0% 性能下降（baseline 显著更大） |
| 真实世界机器人 | 验证鲁棒性 |

## 价值定位

MultiView-VLA 开辟了**多视角合成 + 动作流形**的全新路线——不从传感器或特征层面解决 3D 感知，而是用生成模型"想象"缺失的视角。AML 的直接动作预测理念与主流扩散策略形成对比。

## 局限性

- ⚠️ 依赖多视角扩散模型的质量，生成视角的准确性上限
- ⚠️ 动作流形假设在极端场景（如接触丰富任务）可能不完全成立
- ⚠️ 单目 RGB 输入仍有物理上限

## 关键引用 / 相关页

- [[concept-t008-3d-vla]]
- [[paper-2026-001-3d-mix]] — 特征融合 vs 多视角生成路线
- [[paper-2026-055-stereopolicy-3d-vla]] — 立体视觉 vs 多视角合成
- [[paper-2026-013-world2vlm]] — 世界模型想象视角，生成思路类似
