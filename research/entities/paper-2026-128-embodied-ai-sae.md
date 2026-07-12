---
title: "Embodied AI in Action: SAE World Congress 2026 行业白皮书"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [survey, evaluation, vla]
sources: [raw/papers/2026-128-Embodied-AI-SAE.md]
arxiv: "2605.10653"
date: 2026-05-11
related_topics: [T009, T010, T013]
authors: "SAE World Congress 2026 Panel (Arpan Kusari et al.)"
source_db: "arXiv (White Paper)"
confidence: medium
---

# Embodied AI in Action：SAE World Congress 2026 行业综述

**来源**：SAE World Congress 2026 Panel "Embodied AI in Action"  
**日期**：2026-05-11 | **arXiv**：2605.10653  
**关联选题**：`T009`（安全）/ `T010`（数据效率）/ `T013`（导航/部署）

## 一句话

> 来自汽车、机器人、AI 和安全工程领域专家的**行业共识白皮书**，指出具身 AI 长期成功取决于"不仅 AI 能力进步，更需安全可信部署"。

## 五大核心议题

| 议题 | 核心主张 | 与 wiki 选题交叉 |
|---|---|---|
| **系统工程** | 具身 AI 是系统工程挑战，需工程严谨性 | 全部 |
| **生命周期治理** | 设计→部署→退役的全生命周期管理 | T010（持续学习） |
| **安全与信任** | 功能安全 + SOTIF + 可信 AI 三位一体 | T009 |
| **人因设计** | 人机协作中的人类中心设计 | T011, T013 |
| **标准演进** | ISO/SAE 标准持续发展 | T009 |

## 核心观点

> "Long-term success will depend not only on advances in AI capability, but equally on safe and trustworthy deployment."

这一观点与 T009 选题的[[concept-t009-safety-robustness|安全研究三维框架]]高度一致——学术界的攻击-防御-评测框架需要与行业标准对接。

## 价值定位

- **行业视角**：补充纯学术论文缺失的工程实践和标准化维度
- **跨域共识**：汽车（SAE）+ 机器人 + AI 三领域的交叉视角
- **政策参考**：对老板参与教研室 AI 治理/标准化讨论有参考价值
- 与 T009 安全论文组（[[concept-t009-safety-robustness]]）形成**学术-工业**双视角

## 与已录入论文的交叉

### 安全维度
- [[paper-2026-088-ppo-eal]] — PPO 安全约束控制（学术对应工业安全标准）
- [[paper-2026-046-pre-vla]] — 运行时验证（学术对应全生命周期治理）
- [[paper-2026-063-libero-safety]] — 安全基准（学术对应 SOTIF）

### 部署维度
- *abc scalable behavior cloning*（待 ingest） — 开源工具链（数据采集对应行业标准实践）
- *qwen robotmanip alignment*（待 ingest） — 跨 15 平台（对应多机器人平台标准化需求）

## 局限性

- 白皮书/panel 总结，非系统性学术综述
- 偏重汽车/自动驾驶视角（SAE 背景），机器人操作覆盖有限
- 缺少具体技术方案的深度对比

## 与学术综述的互补关系

| 维度 | 学术综述 | 本白皮书 |
|---|---|---|
| 视角 | 自上而下的分类法 | 自下而上的行业共识 |
| 重点 | 架构/训练/评测 | 安全/治理/标准化 |
| 受众 | 研究者 | 高管/政策制定者/技术领导者 |
| 代表 | [[paper-2026-125-vla-survey-embodied-ai]] | 本文 |

## 引用页

- [[concept-t009-safety-robustness]]
- [[concept-t010-data-efficiency]]
- [[concept-t013-navigation]]
