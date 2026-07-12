---
title: "VT-WAM：视觉-触觉世界动作模型"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, manipulation]
sources: [raw/papers/2026-101-vt-wam-visual-tactile.md]
arxiv: "2607.02503"
date: 2026-07-02
related_topics: [T008, T010, T011, T014]
authors: "Yupeng Zheng, Yuhang Zheng, Songen Gu, Yujie Zang, Yuxing Qin, Weize Li, Haoran Li, Wenchao Ding, Dongbin Zhao"
source_db: "arXiv"
confidence: high
---

# VT-WAM 论文

**作者**：Yupeng Zheng, ... Dongbin Zhao  
**日期**：2026-07-02 | arXiv: 2607.02503  
**关联选题**：`T008`（3D 视觉）/ `T010`（数据效率）/ `T011`（操作）/ `T014`（世界模型）

## 一句话

> 首个**视觉-触觉世界动作模型**：在统一 flow matching 框架下联合预测视觉未来、触觉形变和动作——contact-rich 操作平均成功率 **71.67%**。

## 核心方法

### 1. 三联合预测框架
在统一 flow matching 下联合学习：
- **未来视觉预测**（世界模型分支）
- **触觉形变预测**（触觉动力学分支）
- **动作预测**（策略分支）

### 2. Asymmetric MoT 注意力
- 用首帧视觉锚点桥接时序触觉动态
- 解决触觉信号时序稀疏问题

### 3. AVTAG 接触门控注意力
- **Contact-gated** Action-Visual-Tactile Attention Guidance
- 在接触阶段引导动作查询依赖触觉证据
- 非接触阶段主要依赖视觉

## 实验结果

| 指标 | 结果 |
|---|---|
| 6 个真实 contact-rich 任务平均 | **71.67%** |
| vs Fast-WAM（纯视觉 WAM） | **+26.67%** |
| vs OmniVTLA | **+35.84%** |

消融实验证明：触觉形变建模和接触阶段注意力引导**均不可或缺**。

## 价值定位

- **WAM 的多模态扩展**：从纯视觉 WAM 扩展到**视觉-触觉 WAM**，填补 contact-rich 操作的感知空白
- 与 [[paper-2026-021-motubrain]]（MotuBrain 纯视觉 WAM）形成"视觉 vs 视觉+触觉"对照
- 为 [[paper-2026-022-wam-survey]]（WAM 综述）中"多模态 WAM"方向提供首个实证

## 局限性

- 仅验证 6 个任务，泛化性待考察
- 触觉传感器硬件依赖（需特定 DIGIT tactile sensor）
- 接触检测阈值需手动调优

## 引用页

- [[paper-2026-021-motubrain]] — 纯视觉统一 WAM
- [[paper-2026-022-wam-survey]] — WAM 综述
- [[paper-2026-060-memorywam]] — 持久记忆 WAM
- [[concept-t014-wm]] — 世界模型选题
- [[concept-t011-manipulation]] — 操作选题
