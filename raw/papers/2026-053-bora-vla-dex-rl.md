# BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models
- 作者：Zhongxi Chen, Yifan Han, Yanming Shao, Huanming Liu, Congsheng Xu, Xiaoyu Chen, Yao Mu, Wenzhao Lian
- 来源：arXiv (cs.RO, cs.AI)
- 日期：2026-05-28
- arxivId：2605.30226
- URL：https://arxiv.org/abs/2605.30226
- 相关选题：T008, T009, T010
- 相关度：0.90

## 研究背景
VLA模型在灵巧操作中面临高维控制（多自由度手部）和累积执行误差的挑战。模仿学习难以从高度多模态的灵巧动作数据中提取广义物理交互意图，需要RL后训练来提升部署可靠性。但现有VLA后训练方案在灵巧场景中存在两个核心问题：(1) 生成式动作架构的信用分配失败（去噪链过长导致梯度噪声累积）；(2) 灵巧操作中严重视觉遮挡导致critic过拟合背景特征。

## 核心方法
BORA提出离线到在线的RL后训练框架：
1. **离线阶段**：使用Consistency Policy作为动作专家（1-3步生成动作chunks），截断计算图实现高效梯度反传。设计action-conditioned critic，融合VLM认知tokens和连续动作chunks，确保价值估计基于实际物理交互而非虚假视觉特征。
2. **在线阶段**：冻结离线训练的VLA基座防止灾难性特征漂移，引入轻量级Human-in-the-Loop (HiL) chunk-wise残差适配机制。继承离线critic保证稳定价值估计，引导残差actor从人类干预数据中安全提取修正先验。

## 实验结果
- 5个真实世界灵巧操作任务全面评估
- 标准设置下平均成功率绝对提升33%
- 未见物体泛化提升高达43%
- 显著优于纯模仿学习和传统解耦RL基线

## 局限性
- 依赖人类干预数据（HiL），数据收集成本较高
- 仅在灵巧手操作上验证，其他机器人形态未测试
- 在线阶段的安全性和鲁棒性仍有提升空间

## 与选题关联
- **T008（3D视觉+VLA）**：action-conditioned critic融合VLM认知tokens的思路可扩展到3D视觉信息融合
- **T009（VLA安全）**：残差适配机制本质上是一种安全策略，在冻结基座上做轻量修正，防止灾难性漂移
- **T010（数据效率）**：HiL残差适配是少样本在线适配的有效方案，冻结基座+残差学习的范式与PEFT理念一致

## 关键引用
- Consistency Policy (CP)
- Diffusion Policy
- Flow Matching for VLA
- 各VLA基座模型（OpenVLA, Pi0等）
