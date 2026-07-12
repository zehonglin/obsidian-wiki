# WorldSample: Closed-loop Real-robot RL with World Modelling

- 作者：Yuquan Xue, Le Xu, Zeyi Liu, Zhenyu Wu, Zhengyi Gu, Xinyang Song, Bofang Jia, Ziwei Wang
- 来源：arXiv
- 日期：2026-07-02
- arxivId：2607.02431
- URL：https://arxiv.org/abs/2607.02431
- 相关选题：T010
- 相关度：0.90

## 研究背景
强化学习可以通过试错交互克服模仿学习的演示覆盖限制，但在真实机器人上部署RL仍受高交互成本约束。每次物理rollout昂贵，且只反映一条实现化的动作-结果路径。

## 核心方法
WorldSample — 物理奠基的数据增强框架，在真实rollout、世界模型生成和策略改进之间闭环：

1. **真实rollout** → 收集物理交互数据
2. **世界模型生成** → 基于真实rollout后训练的世界模型生成高保真合成转移
3. **策略改进** → 用合成数据增强训练

核心创新：
- **Policy-Paced Learning (PPL)** — 通过样本选择和调度调节训练过程，平衡有用增强和价值过估计，减轻幻觉引入的噪声
- 世界模型后训练基于真实rollout，大幅降低视觉幻觉
- 与简单数据增广不同，合成转移不被直接当作真实经验

## 实验结果
- 接触丰富和精密操作任务
- 策略成功率提升28%
- 训练步数减少59%
- 世界模型视觉保真度：PSNR提升19.4dB，SSIM提升0.47

## 局限性
- 世界模型质量直接影响增强效果
- 仍需一定量的真实rollout
- PPL调度参数需调优

## 与选题关联
- **T010 (VLA数据效率)**：WorldSample提供了一种全新思路——用世界模型做数据增强而非直接做策略，降低真实数据需求。real-synthetic闭环对VLA数据效率研究有重要参考价值。PSNR/SSIM指标可用于评估合成数据质量。

## 关键引用
- World model post-training
- RL on real robots
- Data augmentation for robotics
