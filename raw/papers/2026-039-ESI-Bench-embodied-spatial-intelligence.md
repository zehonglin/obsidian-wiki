# ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop
- 作者：Yining Hong, Jiageng Liu, Han Yin, Manling Li, Leonidas Guibas, Li Fei-Fei, Jiajun Wu, Yejin Choi
- 来源：arXiv
- 日期：2026-05-18
- arxivId：2605.18746
- URL：https://arxiv.org/abs/2605.18746
- 相关选题：T008
- 相关度：0.88

## 研究背景
空间智能通过感知-动作循环展开，现有评估假设oracle观测。本文将观察者重新定义为行动者，提出主动空间智能基准。

## 核心方法
1. **ESI-Bench基准**：基于OmniGibson构建，10个任务类别+29个子类别，基于Spelke核心知识系统
2. **主动探索框架**：智能体需决定部署感知、移动、操作能力的时机和序列
3. **评估维度**：主动vs被动、随机多视角、3D grounding效果

## 实验结果
- 主动探索显著优于被动方法
- 随机多视角反而引入噪声
- 多数失败源于"动作盲"而非感知弱：糟糕的动作选择→糟糕的观测→级联错误
- 显式3D grounding稳定了深度敏感任务，但不完美的3D表示比2D基线更有害
- 人类研究揭示元认知差距：模型过早高置信度承诺

## 局限性
- 仅在OmniGibson仿真环境中评估
- 未涉及真实机器人部署

## 与选题关联
- **T008（3D视觉+VLA）**：直接评估3D空间感知在具身任务中的作用，3D表示质量对VLA下游任务的影响，为T008提供评估框架

## 关键引用
- Spelke核心知识系统理论
- OmniGibson仿真环境
