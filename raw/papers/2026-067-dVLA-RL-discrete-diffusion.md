# dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion VLA Models

- 作者：Yuhao Wu, Yitian Liu, Weijie Shen et al. (Yao Mu group)
- 来源：arXiv
- 日期：2026-06-22
- arxivId：2606.23623v1
- URL：https://arxiv.org/abs/2606.23623
- 相关选题：T010
- 相关度：0.88

## 研究背景

Discrete Diffusion VLA（dVLA）通过masked generative modeling将视觉、语言、动作统一到离散token空间，结合了迭代精炼和统一表示的优势。但现有dVLA仅限于监督微调（SFT），RL在dVLA上的潜力未被探索。核心挑战：dVLA最终动作的边际概率难以计算。

## 核心方法

1. **轨迹级目标**：将学习目标从边际动作概率转移到采样生成路径的联合概率
2. **MDP建模**：将去噪过程建模为马尔可夫决策过程（MDP），路径概率 = step-wise transitions的乘积
3. **统一步调度**：为不同复杂度任务自适应调整去噪步数，平衡成功率和计算效率

## 关键创新

- 数学上严格formulate了dVLA的RL训练目标
- 变步数调度：简单任务少步去噪、复杂任务多步去噪
- 统一框架原生支持可变去噪步数

## 实验结果

- **LIBERO: 99.7%成功率**
- RoboTwin 2.0: 比SFT baseline提升30.6%
- 与World-Action Model baselines竞争

## 局限性

- 离散diffusion架构的通用性vs连续diffusion的对比
- RL训练的计算开销
- RoboTwin以外更广泛的benchmark验证

## 与选题关联

**T010（VLA数据效率）**：RL post-training是提升VLA数据效率的重要途径。dVLA-RL解决了离散diffusion VLA上RL训练的理论难题，99.7%的LIBERO成功率展示了RL优化的巨大潜力。自适应步调度对计算效率的提升也与T010的数据/计算效率方向一致。

## 关键引用

- LIBERO 99.7% SOTA
- 离散diffusion VLA + RL的首个工作
