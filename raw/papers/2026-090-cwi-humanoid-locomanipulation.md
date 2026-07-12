# CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation
- 作者：Wenqi Ge 等
- 来源：arXiv
- 日期：2026-06-26
- arxivId：2606.27676v1
- URL：https://arxiv.org/abs/2606.27663v1
- 相关选题：T008
- 相关度：0.86

## 研究背景
人形机器人完成日常任务需要协调稳定行走与灵活操作。现有全身控制器面临两难：纯命令采样训练难以收敛，全身体态捕捉模仿受数据集不平衡困扰。

## 核心方法
Composite Whole-Body Imitation (CWI) 框架：
1. **解耦策略**：上身操作用MoCap数据，下身行走用命令条件控制
2. 双判别器AMP训练下身（精选步行和深蹲片段）
3. Multi-critic架构减少行走、操作、动作风格目标间冲突
4. Teacher-student蒸馏：仅条件于双手位姿和速度/高度命令

## 实验结果
- LimX Oli全尺寸人形机器人部署
- 竞争性的loco-manipulation性能
- 稳健的全身协调
- 无需全身体态捕捉设备即可遥操作

## 局限性
- 解耦策略可能限制上下身协同的复杂动作
- 仅在上半身使用MoCap，下半身完全依赖AMP学习

## 与选题关联
**T008（3D视觉+VLA）**：全身协调操作对空间感知提出更高要求，CWI的解耦方法为VLA+空间感知在全身人形机器人上的部署提供参考框架。

## 关键引用
- AMP (Adversarial Motion Prior)
- Teacher-student distillation
