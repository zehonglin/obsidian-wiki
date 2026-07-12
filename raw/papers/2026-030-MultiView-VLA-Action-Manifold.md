# Learning Action Manifold with Multi-view Latent Priors for Robotic Manipulation
- 作者：Junjin Xiao, Dongyang Li, Yandan Yang, Shuang Zeng, Tong Lin, Xinyuan Chang, Feng Xiong, Mu Xu, Xing Wei, Zhiheng Ma, Qing Zhang, Wei-Shi Zheng
- 来源：arXiv
- 日期：2026-05
- arxivId：2605.11832
- URL：https://arxiv.org/html/2605.11832v1
- 相关选题：T008
- 相关度：0.90

## 研究背景
VLA模型面临两大瓶颈：(1) 单目输入下的深度模糊导致空间感知受限；(2) 传统扩散/flow matching方法预测噪声或速度等间接目标，优化效率低。

## 核心方法
1. **多视角扩散先验**：利用预训练多视角扩散模型在潜空间合成新视角，减少几何不确定性
2. **Geometry-Guided Gated Transformer (G³T)**：在单目3D几何先验引导下对齐多视角潜特征，自适应门控机制选择信息丰富的视角
3. **Action Manifold Learning (AML)**：基于"动作流形假设"，直接在动作流形上预测动作，而非间接预测噪声/速度

## 实验结果
- LIBERO、LIBERO-Plus、RoboTwin 2.0 上超越SOTA
- 真实世界机器人实验验证鲁棒性
- 在空间扰动下仅8.0%性能下降（baseline更大）

## 局限性
- 依赖多视角扩散模型的质量
- 动作流形假设在极端情况下可能不完全成立
- 单目RGB输入仍有物理上限

## 与选题关联
- **T008 (具身智能VLA架构)**: 提出全新的VLA空间感知+动作生成框架，G³T和AML是架构创新

## 关键引用
- RT-2, OpenVLA, π0
- DP3, DepthVLA (3D感知VLA)
- VGGT (3D基础模型)
