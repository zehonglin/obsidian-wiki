---
title: "T014 选题总览：世界模型（World Models）"
created: 2026-07-12
updated: 2026-07-12
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [survey, model, architecture]
sources: []
related_topics: [T008, T010, T011, T012]
confidence: high
---

# T014 选题：世界模型（World Models）

> 世界模型是 VLA 的"想象力引擎"——让机器人不仅能看到现在，还能**预测未来**、**理解物理规律**、**在脑中排练**。

## 为什么世界模型是核心方法论

世界模型贯穿 VLA 研究的**所有维度**：

| 维度 | 世界模型的作用 | 代表论文 |
|---|---|---|
| **3D 感知（T008）** | 用 3D/4D 表示预测未来场景 | 3D-VLA, GaussianDream, RynnWorld-4D |
| **安全（T009）** | 预测动作后果来避免危险 | Pre-VLA, ForesightSafety-VLA |
| **数据效率（T010）** | 生成合成数据 / 想象训练 | World-Env, RISE, MotuBrain |
| **操作（T011）** | 预测接触结果指导操作 | VT-WAM |
| **RL 训练（T012）** | 提供 RL 虚拟环境 | WorldSample, World-Env |
| **导航（T013）** | 预测导航后果 | （待发掘） |

## 四条技术路线

### 路线 1：生成式世界模型（视频/场景预测）
**核心**：从当前观测 + 动作预测未来视觉帧

- [[paper-2026-108-rynnworld-4d]] — 4D 联合生成 RGB + 深度 + 光流（2.544 亿帧数据集）
- [[paper-2026-018-starry]] — 时空扩散 + GASAM 动作中心化
- [[paper-2024-001-3d-vla]] — 开山之作：3D 点云 + 图像生成

**特点**：视觉预测质量是关键瓶颈；计算开销大但信息最丰富

### 路线 2：VLA × 世界模型统一训练
**核心**：在单一模型中联合训练动作预测和世界动力学预测

- [[paper-2026-057-rynnvla002-unified-vla-wm]] — VLA ↔ WM 双向增强（LIBERO 97.4%）
- [[paper-2026-021-motubrain]] — 统一世界动作模型（RoboTwin 95%+）
- [[paper-2026-060-memorywam]] — 带持久记忆的 WAM

**特点**：两个目标互相监督，数据效率最高；但训练复杂度高

### 路线 3：世界模型知识蒸馏
**核心**：将世界模型知识蒸馏到 VLA/VLM，推理时不需运行世界模型

- [[paper-2026-013-world2vlm]] — 世界模型→VLM 空间想象力蒸馏
- [[paper-2026-107-bridge-wa]] — 未来变化预测→三个紧凑先验蒸馏
- [[paper-2026-056-gaussiandream-3d-vla]] — 3D 高斯前缀查询（训练时学，推理时丢弃）

**特点**：推理零额外开销；蒸馏质量决定上限

### 路线 4：世界模型驱动的新范式
**核心**：利用 WAM 的独特能力开启全新应用场景

- [[paper-2026-077-regen-wam-continual-imitation]] — WAM 生成式回放 → 持续学习（遗忘↓50%）
- [[paper-2026-071-icwm-in-context-world-model]] — 上下文世界建模 → 零微调跨环境适配
- [[paper-2026-020-world-env]] — 世界模型做 RL 后训练虚拟环境
- [[paper-2026-019-rise]] — 组合世界模型 + 想象空间自改进
- [[paper-2026-103-worldsample]] — 世界模型增强真实机器人 RL
- [[paper-2026-101-vt-wam-visual-tactile]] — 视觉-触觉 WAM → contact-rich 操作

**特点**：每种应用解决不同瓶颈；WAM 的多功能性使其成为"瑞士军刀"

## 与已有 WAM 类论文的知识图谱

### 世界动作模型（WAM）谱系

```
WAM Survey (T008/T009/T010)
├── MotuBrain — 统一 WAM（纯视觉，RoboTwin 95%+）
│   ├── MemoryWAM — +持久记忆（长时序）
│   ├── VT-WAM — +触觉（contact-rich）
│   └── REGEN — +生成式回放（持续学习）
├── STARRY — 时空扩散 WAM（GASAM）
├── World2VLM — WM→VLM 蒸馏
│   └── Bridge-WA — WM→VLA 先验蒸馏
├── RISE — 组合 WM + 想象自改进
├── World-Env — WM 做 RL 环境
│   └── WorldSample — WM 增强真实 RL
└── ICWM — WM 做上下文适配
```

### 关键 cross-link

| 本批论文 | 已有论文 | 关系 |
|---|---|---|
| 3D-VLA | OG-VLA, 3D-Mix | 开山→后续延伸 |
| RynnVLA-002 | MotuBrain | 统一训练（不同路线） |
| GaussianDream | 3D-Mix, OG-VLA | 3D 增强不同实现 |
| RynnWorld-4D | RynnVLA-002 | 同团队 VLA+WM→4D |
| VT-WAM | MotuBrain, MemoryWAM | 纯视觉→+触觉 |
| Bridge-WA | World2VLM | 空间蒸馏→变化蒸馏 |
| REGEN | MemoryWAM | 记忆→生成回放 |
| ICWM | World-Env | 训练环境→推理适配 |

## 研究空白

1. **世界模型 + 导航**：当前 WM 集中在操作，导航场景的 WM 几乎空白
2. **多本体世界模型**：不同机器人共享一个 WM？迁移性未验证
3. **长时程预测质量**：REGEN 揭示 horizon 增加时视觉退化
4. **世界模型 + RL 闭环**：WorldSample/World-Env 初步验证，但 sim-to-real gap 未完全解决
5. **触觉世界模型扩展**：VT-WAM 是首个，其他模态（力、声音）未涉及

## 选题统计

- **本批录入**：8 篇（3D-VLA, RynnVLA-002, ICWM, REGEN, VT-WAM, RynnWorld-4D, GaussianDream, Bridge-WA）
- **已有 WAM 相关**：World2VLM, STARRY, RISE, MotuBrain, MemoryWAM, World-Env, WAM Survey, WorldSample（8 篇，跨多批）
- **总计**：16 篇论文与世界模型直接相关

## 引用页

- [[concept-t008-3d-vla]] — 3D 视觉增强 VLA
- [[concept-t010-data-efficiency]] — 数据效率
- [[concept-t012-rl-training]] — RL 训练
- [[concept-world-model-distillation]] — 世界模型蒸馏（具体概念）
- [[paper-2026-022-wam-survey]] — WAM 综述（200+ 论文）
