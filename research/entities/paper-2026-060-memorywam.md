---
title: "MemoryWAM：带持久记忆的高效世界动作模型"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, vla, training]
sources: [raw/papers/2026-060-memorywam-persistent-memory.md]
arxiv: "2606.20562"
date: 2026-06-18
related_topics: [T008, T010]
authors: "Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li, Linning Xu, Zhengrong Xue, Zhecheng Yuan, Dahua Lin, Jiangmiao Pang, Huazhe Xu"
source_db: "arXiv"
confidence: high
---

# MemoryWAM 论文

**作者**：Sizhe Yang, Juncheng Mu, ... Huazhe Xu (Shanghai AI Lab 等机构)  
**日期**：2026-06-18 | arXiv: 2606.20562  
**关联选题**：`T008`（3D 视觉）/ `T010`（数据效率）

## 一句话

> 用**混合记忆设计**（近期帧 + 事件边界锚帧 + 压缩 Gist Token）解决 WAM 的**根本性权衡**：高效推理 vs 长历史保留。

## 核心方法

### 1. 混合记忆三层
- **近期帧**：保留短时间窗口的完整信息
- **事件边界锚帧**：在关键事件转换点保存帧
- **压缩 Gist Token**：用紧凑 token 总结长程历史

### 2. 定制注意力机制
- 支持检索详细短期上下文
- 同时检索压缩长期上下文

### 3. 持续记忆
- 支持**记忆依赖的决策**
- 降低推理延迟和 GPU 内存使用

## 实验结果

- 在**长时间范围、记忆依赖**的操作任务上（仿真+真实世界）验证
- 优于强 VLA 和 WAM 基线
- 保持良好的计算效率

## 价值定位

- **解决 WAM 的根本性瓶颈**：让长时序任务变得可行
- 与 [[paper-2026-021-motubrain]]（同 WAM 方向，但无长记忆）形成"无记忆 vs 有记忆"对照
- 与 [[paper-2026-018-starry]]（时空扩散）一起：**两个 WAM 的不同实现路径**

## 局限性

- 事件边界检测依赖额外模块
- Gist token 压缩可能导致部分历史信息丢失
- 主要在操作任务上验证，**导航场景未充分探索**

## 引用页

- [[paper-2026-021-motubrain]] — 同样是 WAM
- [[paper-2026-018-starry]] — STARRY 时空动作
- [[concept-t008-3d-vla]]
