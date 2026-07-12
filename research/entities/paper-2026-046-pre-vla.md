---
title: "Pre-VLA：VLA 和世界模型的先发式运行时验证"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, inference]
sources: [raw/papers/2026-046-Pre-VLA.md]
arxiv: "2605.22446"
date: 2026-05-20
related_topics: [T009, T008]
authors: "Zhen Sun, Yongjian Guo, Haoran Sun, Luqiao Wang, Wei Lu, Jiachi Ji, Shengzhe Ji, Junwu Xiong, Zhijun Meng"
source_db: "arXiv"
confidence: high
---

# Pre-VLA 论文

**作者**：Zhen Sun, Yongjian Guo, Haoran Sun, Luqiao Wang, Wei Lu, Jiachi Ji, Shengzhe Ji, Junwu Xiong, Zhijun Meng  
**日期**：2026-05-20 | arXiv: 2605.22446  
**研究方向**：`T009`（VLA 安全）/ `T008`（3D 视觉）

## 核心一句话

> 在 VLA 候选动作执行物理操作或进入世界模型想象**之前**，进行先发式有效性评估：轻量双分支头预测安全置信度 + critic 优势分数，低质量动作触发自适应重采样。

## 关键创新

1. **先发式架构**——"动作执行前验证"而非"事后检测"，将安全检查嵌入推理管线
2. **多任务训练目标**——Focal 分类 + 优势回归 + 软阈值校准，解决类别不平衡和边界不稳定
3. **双模式重采样调度器**——在有限计算预算下过滤低质量动作，计算开销可控（~184ms/次）

## 实验结果

| 指标 | 数值 |
|---|---|
| LIBERO 成功率 | 30.79% → **37.62%**（+6.83pp） |
| 动作验证 F1 | **0.8303** |
| 无效动作误放率 | 仅 **0.0200** |
| 单次验证延迟 | ~183.9ms |

## 价值定位

- **运行时安全层**的代表工作：介于"训练时鲁棒性"（[[paper-2026-040-rovla]]）和"评测基准"（[[paper-2026-063-libero-safety]]）之间的第三层
- 直接呼应 [[concept-t009-safety-robustness]] 研究空白 #3："动作安全校验层"
- 同时适用于世界模型 rollout 验证，与 [[concept-world-model-distillation]] 相关

## 局限性

- ⚠️ 基于 RynnVLA-002 骨干，对其他 VLA 架构的适配待验证
- ⚠️ 增加推理延迟（~184ms），实时性敏感场景需权衡
- ⚠️ 仅 LIBERO 仿真验证

## 引用页

- [[concept-t009-safety-robustness]]
- [[paper-2026-040-rovla]] — 训练侧防御
- [[paper-2026-005-vla-fool]] — 攻击侧分析
