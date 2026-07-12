---
title: "ForesightSafety-VLA：过程级诊断安全基准（13 类安全分类）"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [vla, benchmark, evaluation]
sources: [raw/papers/2026-080-foresight-safety-vla.md]
arxiv: "2606.27079"
date: 2026-06-25
related_topics: [T009]
authors: "Mingyang Lyu, Yinqian Sun, Yiyang Jia, Sicheng Shen, Moquan Sha, Huangrui Li, Feifei Zhao, Yi Zeng"
source_db: "arXiv"
confidence: high
---

# ForesightSafety-VLA 论文

**作者**：Mingyang Lyu, Yinqian Sun, Yiyang Jia, Sicheng Shen, Moquan Sha, Huangrui Li, Feifei Zhao, Yi Zeng  
**机构**：中科院自动化所 / 人民大学  
**日期**：2026-06-25 | arXiv: 2606.27079  
**研究方向**：`T009`（VLA 安全）

## 核心一句话

> **安全不是事后过滤层，而是场景级内生属性**：提出 13 类安全分类体系（3 族：Safe-Core / Safe-Lang / Safe-Vis），基于 RoboTwin 构建 66 个安全增强场景，首次引入过程级安全度量（累积安全代价 CC + 风险暴露时间 RET）。

## 关键创新

1. **13 类安全分类体系**——覆盖物理交互（5 类）、指令侧（4 类）、感知侧（4 类）
2. **过程级度量**——累积安全代价 (CC) 基于双阈值监控，风险暴露时间 (RET) 量化不安全状态占比
3. **四象限分解**——安全成功 / 不安全成功 / 安全失败 / 不安全失败，区分"真正安全"与"侥幸成功"
4. **诊断性评估**——结构变异 (L0-L2)、语言变异 (W0-W4)、视觉变异 (V0-V4) 三维度系统诊断

## 实验结果

| 核心发现 | 内容 |
|---|---|
| 不安全的"名义成功" | 即使最强策略也产生不可忽略的安全代价 |
| 弱模型更危险 | 失败方式更危险而非更保守 |
| **结构和视觉变异** | 引起的安全退化 **远大于** 语言变异 |

## 价值定位

- 与 [[paper-2026-063-libero-safety]] 互补：LIBERO-Safety 做广度，ForesightSafety 做深度
- **过程级度量**是安全评估的方法论升级：从"成功/失败"二元到连续安全代价
- "结构和视觉变异 > 语言变异"的发现，重新定义了 VLA 安全的优先攻击面

## 局限性

- ⚠️ 仅 RoboTwin 仿真验证
- ⚠️ 66 个基础场景，复杂长时序任务覆盖有限
- ⚠️ 评估的 VLA 基线数量有限

## 引用页

- [[concept-t009-safety-robustness]]
- [[paper-2026-063-libero-safety]] — 广度安全基准
- [[paper-2026-096-oopsieverse]] — 物理损伤感知
