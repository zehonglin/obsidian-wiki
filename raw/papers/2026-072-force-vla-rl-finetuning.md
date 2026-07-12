# FORCE: Efficient VLA Reinforcement Fine-Tuning via Value-Calibrated Warm-up and Self-Distillation

- 作者：Shuyi Zhang, Yunfan Lou, Hongyang Cheng, Yichen Guo, Chuyao Fu, Yaoxu Lyu, Xiaojie Zhang, Haoran Li, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang
- 来源：arXiv
- 日期：2026-06-24
- arxivId：2606.26006
- URL：https://arxiv.org/abs/2606.26006
- 相关选题：T010
- 相关度：0.90

## 研究背景

VLA模型受限于次优数据的模仿学习天花板。RL微调可突破此限制，但样本效率极低，主要由于两个问题：(1) Q函数不稳定导致的灾难性初始遗忘；(2) 低质量探索数据导致的低效策略更新，常需昂贵的人工干预。

## 核心方法

提出FORCE——三阶段框架：
1. **Value-Calibrated Warm-Up**：利用on-policy rollout缓解Q函数的分布偏移
2. **Online Stage**：校准后的Q函数作为过滤器，同时筛选策略自身的动作提案和专家数据，确保仅高价值动作用于策略更新
3. **Self-Distillation**：结合自蒸馏进一步稳定训练

## 实验结果

- 在多种仿真和真实世界任务上评估
- 成功率绝对提升79%，超越先前RL方法10%
- 训练加速32.5%
- 关键：缓解了常见的成功率骤降问题，无需人工干预

## 局限性

- 三阶段训练流程较为复杂
- 仍依赖on-policy rollout，计算开销较大
- Value calibration的质量依赖初始Q函数的训练

## 与选题关联

**T010（VLA数据效率与少样本跨任务/跨机器人适配）**：FORCE解决了VLA从模仿学习到RL微调的关键效率瓶颈。通过value-calibrated warm-up避免灾难性遗忘，使VLA能够在少量数据下高效微调。这对降低VLA部署门槛、实现快速任务适配具有直接意义。

## 关键引用

- RL post-training在VLA上的系统化应用
- 与dVLA-RL (2026-067)形成互补：FORCE关注训练稳定性，dVLA-RL关注离散扩散动作空间
