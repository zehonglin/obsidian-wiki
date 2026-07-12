---
title: "VLA-Fool：多模态对抗攻击下的 VLA 对齐失效"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [vla, benchmark, evaluation]
sources: [raw/papers/2026-005-VLA-Fool.md]
arxiv: "2511.16203"
date: 2025-11-19
related_topics: [T009]
authors: "Yuping Yan, Yuhan Xie, Yixin Zhang, Lingjuan Lyu, Handing Wang, Yaochu Jin"
source_db: "arXiv / ACM 2026"
confidence: high
---

# VLA-Fool 论文

**作者**：Yuping Yan, Yuhan Xie, Yixin Zhang, Lingjuan Lyu, Handing Wang, Yaochu Jin  
**机构**：西湖大学 TGAI Lab / Penn State / Sony Research / 西安电子科技大学  
**日期**：2025-11-19（arXiv），2026-04（ACM 2026）  
**研究方向**：`T009`（VLA 安全）

## 核心一句话

> 首个针对 VLA 的**多模态对抗攻击综合框架**：覆盖文本（SGCG 语义梯度 + prompt 注入）、视觉（patch + 噪声）、跨模态不对齐三条攻击线，在 LIBERO 上可导致 >60% 失败率（长时序任务 100%）。

## 关键创新

1. **SGCG（语义贪婪坐标梯度）**——将 GCG 扩展到 VLA 语义空间，4 种扰动模式（指代消歧 / 属性弱化 / 范围模糊 / 否定混淆）
2. **跨模态不对齐攻击**——不直接优化动作损失，仅破坏内部视觉-语言特征对齐，平均失败率 >93%
3. **黑盒 + 白盒双覆盖**——从完全白盒（梯度访问）到纯黑盒（随机噪声 / prompt 注入）的完整威胁模型

## 实验结果

| 攻击维度 | 最强失败率 |
|---|---|
| Suffix2 注入（黑盒文本） | 83.3% |
| 机械臂 patch（白盒视觉） | **100%** |
| 跨模态不对齐 | **>93% 平均** |
| Long-horizon 任务 | **100%** |

## 价值定位

- **揭示 VLA 根本脆弱性**：跨模态对齐不稳定是动作失败的底层原因
- 为 [[concept-t009-safety-robustness]] 提供了**攻击面**的完整地图
- 与 [[paper-2026-040-rovla]] 形成攻防对照：VLA-Fool 从攻击侧揭示弱点，RoVLA 从训练侧增强鲁棒性

## 局限性

- ⚠️ 仅在 OpenVLA (7B) 单模型验证，泛化性未知
- ⚠️ 仅 LIBERO 仿真，无真实机器人
- ⚠️ 纯攻击研究，未提出防御方案
- ⚠️ 跨模态攻击需白盒访问（embedding 级别）

## 引用页

- [[concept-t009-safety-robustness]]
- [[paper-2026-040-rovla]] — 防御侧：多一致性约束增强鲁棒性
- [[paper-2026-046-pre-vla]] — 运行时侧：动作执行前过滤
