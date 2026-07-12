# PPO-EAL: Exact Augmented Lagrangian Proximal Policy Optimization for Safe Robotic Control
- 作者：Jiatao Ding 等
- 来源：arXiv
- 日期：2026-06-26
- arxivId：2606.27861v1
- URL：https://arxiv.org/abs/2606.27861v1
- 相关选题：T009
- 相关度：0.88

## 研究背景
强化学习在机器人控制中前景广阔，但大多数工作忽略安全约束。安全RL旨在最大化性能的同时满足物理约束，现有算法难以高效学习且精确满足约束。

## 核心方法
PPO-EAL：将精确增广拉格朗日优化集成到PPO中：
1. 结合裁剪策略更新与精确二次惩罚项
2. 理论保证约束执行，无需不切实际的极大惩罚因子
3. 动量调节乘子更新提升对偶变量稳定性
4. 减少约束振荡和不安全行为，保持任务性能

## 实验结果
- GPU加速机器人基准验证：cart-pole平衡、双摆稳定、7-DoF Franka末端到达、四足行走
- 安全精度和奖励性能均优于SOTA一阶安全RL方法
- 零样本sim-to-real部署于接触丰富的齿轮装配任务
- 提高任务成功率，降低峰值接触力

## 局限性
- 一阶方法，可能在高度非线性约束上效果受限
- sim-to-real迁移仍存在gap

## 与选题关联
**T009（VLA安全性与鲁棒性）**：PPO-EAL提供了安全RL的通用框架，可直接应用于VLA策略训练中的安全约束。精确约束满足对机器人物理安全至关重要。

## 关键引用
- PPO, constrained policy optimization
- Sim-to-real transfer
