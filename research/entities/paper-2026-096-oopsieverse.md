---
title: "OopsieVerse：物理损伤感知安全基准（RSS 2026）"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [vla, benchmark, dataset, evaluation]
sources: [raw/papers/2026-096-oopsieverse-safety-benchmark.md]
arxiv: "2606.31993"
date: 2026-06-30
related_topics: [T009]
authors: "Arnav Balaji, Arpit Bahety, Sriniket Ambatipudi, Daniel Lam, Junhong Xu, Roberto Martín-Martín"
source_db: "arXiv (RSS 2026)"
confidence: high
---

# OopsieVerse 论文

**作者**：Arnav Balaji, Arpit Bahety, Sriniket Ambatipudi, Daniel Lam, Junhong Xu, Roberto Martín-Martín  
**日期**：2026-06-30 | arXiv: 2606.31993 | **RSS 2026**  
**研究方向**：`T009`（VLA 安全）

## 核心一句话

> 首个**物理损伤感知仿真框架**：DamageSim 仿真器无关地检测机械/热/流体三类损伤，OopsieBench 在 32 项家庭任务上区分"任务完成"与"安全执行"，揭示 VLA 可能通过不安全捷径达成目标。

## 关键创新

1. **DamageSim**——仿真器无关的损伤检测框架
   - 机械损伤：冲击力、压缩力、拉伸力导致的变形/断裂
   - 热损伤：极端温度接触
   - 流体损伤：液体接触导致腐蚀/短路
   - 统一损伤值计算
2. **OopsieBench**——32 项家庭操作任务（OmniGibson 17 + RoboCasa 15）
   - 区分任务完成 vs 安全执行
   - 包含不安全的目标达成捷径
3. **全流程应用**：损伤感知遥操作 → 损伤条件 IL/RL → VLA 安全基准 → sim-to-real 安全转移

## 实验结果

- 在两个不同物理后端的仿真器中验证 DamageSim
- 损伤感知策略在真实世界展示更安全行为
- 损伤感知数据收集全流程验证

## 价值定位

- **物理损伤量化**填补了仿真安全评估的关键空白：从"碰撞检测"升级到"损伤程度量化"
- 与 [[paper-2026-063-libero-safety]]（碰撞避免）和 [[paper-2026-080-foresight-safety-vla]]（过程级度量）形成三维评测体系
- "不安全捷径"概念：VLA 可能通过危险方式完成任务，挑战传统"成功率"指标

## 局限性

- ⚠️ 目前仅覆盖三类损伤（机械/热/流体），化学/电气等未覆盖
- ⚠️ 家庭场景为主，未覆盖工业环境
- ⚠️ 损伤模型可能无法完全反映真实物理复杂性

## 引用页

- [[concept-t009-safety-robustness]]
- [[paper-2026-063-libero-safety]] — 物理+语义安全基准
- [[paper-2026-080-foresight-safety-vla]] — 诊断级安全基准
