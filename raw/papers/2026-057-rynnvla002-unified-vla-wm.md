# RynnVLA-002: A Unified Vision-Language-Action and World Model

- 作者：Jun Cen, Siteng Huang, Yuqian Yuan, Kehan Li, Hangjie Yuan, Chaohui Yu, Bohan Hou, Yuming Jiang, Jiayan Guo, Xin Li, Hao Luo, Fan Wang, Deli Zhao, Hao Chen
- 来源：arXiv (cs.RO)
- 日期：2025-11-21 (v1), 2026-05-30 (v3)
- arxivId：2511.17502v3
- DOI：10.48550/arXiv.2511.17502
- URL：https://arxiv.org/abs/2511.17502
- 相关选题：T008, T010
- 相关度：0.92

## 研究背景
VLA模型在机器人控制中展现出强大能力，但观察到动作的映射和环境的动态预测是割裂的。现有的world model和VLA model各自独立训练，缺乏统一的联合学习框架。如何将action generation和future state prediction统一在一个模型中，使两者互相增强，是一个关键问题。

## 核心方法
- **统一框架**：RynnVLA-002将VLA和World Model统一在单一自回归模型中
- **双向增强**：
  - World Model利用action+visual输入预测未来图像状态，学习环境物理规律来优化action generation
  - VLA Model从图像观测生成action，增强视觉理解并支持World Model的图像生成
- **自回归Action World Model**：统一action和image的理解与生成
- 无需预训练即可达到高性能

## 实验结果
- **LIBERO仿真**：97.4%成功率（无预训练）
- **LeRobot真实世界**：集成的world model将总体成功率提升50%
- 证明了VLA和World Model的互相增强效应

## 局限性
- v3版本更新于2026-05-30，尚未经过同行评审
- 真实世界实验仅在LeRobot平台上验证，泛化性待验证
- 对3D空间感知的整合未涉及

## 与选题关联
- **T008（3D视觉+VLA）**：RynnVLA-002的world model预测未来图像状态，与空间感知增强方向互补。若world model能融合3D表示（点云/深度），可能进一步提升空间理解精度
- **T010（VLA数据效率）**：无需预训练即达97.4%，说明world model的引入提供了更好的数据效率。统一框架下的知识共享减少了数据需求

## 关键引用
- 属于VLA+World Model融合的新兴方向
- 与Continuous Reasoning (2606.00229)互补：CR关注推理链，RynnVLA关注动力学预测
