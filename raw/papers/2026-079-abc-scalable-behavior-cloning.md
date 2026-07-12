# Scalable Behavior Cloning with Open Data, Training, and Evaluation (ABC)
- 作者：Arthur Allshire, Himanshu Gaurav Singh, Ritvik Singh, Adam Rashid, Hongsuk Choi, et al.
- 来源：arXiv (cs.RO)
- 日期：2026-06-25
- arxivId：2606.27375v1
- URL：https://arxiv.org/abs/2606.27375
- 相关选题：T010
- 相关度：0.85

## 研究背景
行为克隆（BC）是机器人操作学习的主流方法，但缺乏完全开源的工具链：大规模遥操作数据集、硬件设计、训练基础设施和仿真评估管道。

## 核心方法
ABC——全开源行为克隆工具栈：
1. **ABC-130K**：迄今最大开源遥操作数据集，3500小时数据、130K+片段、195种任务
2. 开源硬件设置、训练基础设施和仿真管道
3. 400小时仿真遥操作数据 + 协同训练方案
4. 对比DiT和VLA模型的常见架构选择
5. 仿真-真实关联评估方案

## 实验结果
- 成功执行折纸、从钱包取信用卡等灵巧任务
- 提供可复现的工具链，为社区建立基础
- 项目页: https://abc.bot

## 局限性
- 硬件设置仍需一定成本
- 数据采集依赖遥操作质量
- VLA模型对比可能不涵盖最新方法

## 与选题关联
- **T010（VLA数据效率）**：ABC-130K是VLA数据效率研究的重要基础设施。大规模开源数据使得少样本适配、跨任务迁移等T010方向的研究有了可靠的数据基础和评估基准。
