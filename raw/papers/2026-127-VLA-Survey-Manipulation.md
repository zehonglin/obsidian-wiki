# Survey of Vision-Language-Action Models for Embodied Manipulation

- 作者：Haoran Li, Yu-Hui Chen, Wenbo Cui
- 来源：arXiv (中文语言论文)
- 日期：2025-08-21 (v1), 2025-11-12 (v2)
- arxivId：2508.15201
- DOI：10.48550/arXiv.2508.15201
- 类型：综述 (Survey, 中文)

## 摘要

受大基础模型进展启发，VLA 模型作为通用机器人控制框架，大幅提升了具身智能系统的环境交互能力。本综述从**五个关键维度**全面回顾 VLA 模型：

1. **VLA 模型架构** — 架构发展轨迹（Transformer → Diffusion → Flow Matching → MoE）
2. **训练数据集** — 数据规模、多样性、采集方法
3. **预训练方法** — 表征对齐、多模态预训练
4. **后训练方法** — 微调、RL 对齐、安全约束
5. **模型评测** — 基准设计、评估指标、跨本体泛化

## 核心贡献

- 梳理 VLA 架构**发展轨迹**（chronological trajectory）
- 从数据到训练到评测的**端到端覆盖**
- 聚焦**操作任务**（embodied manipulation），比通用 VLA 综述更聚焦

## 引用数据

- cited_by: 0 (新发表，2025-08)
- 中文撰写，对国内学术圈友好

## 与现有 wiki 的关联

- 五维度框架与 T008-T014 选题体系形成互补
- 后训练方法部分与 T012（RL Training）高度相关
- 数据集部分与 T010（数据效率）交叉
- 与 [[paper-2026-022-wam-survey]] 形成姊妹综述（操作 vs 世界模型）
