---
title: "RoVLA：多一致性约束增强 VLA 鲁棒性"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, training]
sources: [raw/papers/2026-040-RoVLA-robust-multi-consistency.md]
arxiv: "2605.19678"
date: 2026-05-25
related_topics: [T009, T008]
authors: "Jingzhou Luo, Yifan Wen, Yongjie Bai, Xinshuai Song, Yang Liu, Liang Lin"
source_db: "arXiv"
confidence: high
---

# RoVLA 论文

**作者**：Jingzhou Luo, Yifan Wen, Yongjie Bai, Xinshuai Song, Yang Liu, Liang Lin  
**机构**：中山大学（HCPLPLab）  
**日期**：2026-05-25 | arXiv: 2605.19678  
**研究方向**：`T009`（VLA 安全）/ `T008`（3D 视觉）

## 核心一句话

> 通过三种互补的一致性约束——**指令一致性 (IC)**、**进化一致性 (EC)**、**观察一致性 (OC)**——在端到端策略学习中显式建模不变性，使 VLA 在视角扰动、指令改写、组合变化下保持稳健。

## 关键创新

1. **三重一致性约束框架**——首次将鲁棒性从训练副产品提升为显式学习目标
   - IC：语义等价指令改写下行为接地稳定
   - EC：flow-matching 生成过程中动作意图一致
   - OC：视觉/本体感受扰动前后预测一致
2. **LIBERO-Plus 失败诊断**——揭示三种失败模式：伪视觉理解、伪语言跟随、伪组合泛化
3. **超越 π₀/π₀.₅**：在多样化任务和观察偏移下显著优于主流 VLA 基线

## 实验结果

| 基准 | 表现 |
|---|---|
| LIBERO-Plus | 全面超越基线 |
| RoboTwin 2.0 | 更强鲁棒性 |
| 真实世界任务 | 验证通过 |

代码开源：https://github.com/HCPLPLab-SYSU/RoVLA

## 价值定位

- **防御侧代表**：与 [[paper-2026-005-vla-fool]] 的攻击侧形成完整攻防画面
- 三种一致性约束为**VLA 安全微调**提供了可操作框架（呼应 T009 研究空白 #5）
- OC 约束可扩展到 3D 观察扰动，与 [[concept-t008-3d-vla]] 交叉

## 局限性

- ⚠️ 三种一致性损失的超参数调优复杂
- ⚠️ 训练计算开销增加
- ⚠️ 真实世界场景验证有限

## 引用页

- [[concept-t009-safety-robustness]]
- [[paper-2026-005-vla-fool]] — 攻击侧：揭示 VLA 跨模态脆弱性
- [[paper-2026-046-pre-vla]] — 运行时侧：动作过滤验证
