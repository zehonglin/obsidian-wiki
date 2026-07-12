# Booster Lab: A Data-Centric Pipeline for Learning Deployable Humanoid Locomotion Policies
- 作者：Penghui Chen 等
- 来源：arXiv
- 日期：2026-06-26
- arxivId：2606.27813v1
- URL：https://arxiv.org/abs/2606.27813v1
- 相关选题：T010
- 相关度：0.85

## 研究背景
人形机器人运动学习不仅需要面向任务的控制策略，还需要物理可行且自然的运动以迁移到真实机器人。但机器人可行运动数据稀缺：原始人类演示可能不兼容机器人形态，开源片段质量参差不齐。

## 核心方法
Data-centric训练与部署流程：
1. **运动数据筛选**：数据导向的质量过滤与适配
2. **Real-to-sim模型适配**：缩小仿真-现实差距
3. **AMP-based强化学习**：基于对抗运动先验的策略训练
4. **Sim-to-real部署**：完整迁移流程

## 实验结果
- Booster T1机器人验证
- Booster K1跨平台初步验证
- 展示数据筛选对策略质量的显著影响

## 局限性
- 主要聚焦于行走/运动，上肢操作涉及较少
- 数据筛选标准依赖人工设计

## 与选题关联
**T010（VLA数据效率）**：Data-centric方法论直接回应T010"少样本数据质量对适配效果的影响"研究空白。运动数据筛选→AMP训练的pipeline可迁移到VLA操作数据流程。

## 关键引用
- AMP, sim-to-real
- Booster T1/K1 robots
