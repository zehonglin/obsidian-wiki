---
title: "T012 选题：VLA 的强化学习训练"
created: 2026-07-12
updated: 2026-07-12
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [training, reinforcement-learning, vla]
sources: [raw/papers/2026-097-z1-vla-rl.md, raw/papers/2026-072-force-vla-rl-finetuning.md, raw/papers/2026-067-dVLA-RL-discrete-diffusion.md, raw/papers/2026-087-warp-rm-progress-reward.md, raw/papers/2026-100-sarl-semantic-rl.md, raw/papers/2026-103-worldsample-real-robot-rl.md, raw/papers/2026-088-ppo-eal-safe-rl.md]
related_papers: [paper-2026-097-z1, paper-2026-072-force, paper-2026-067-dvla-rl, paper-2026-087-warp-rm, paper-2026-100-sarl, paper-2026-103-worldsample, paper-2026-088-ppo-eal, paper-2026-020-world-env, paper-2026-053-bora]
confidence: high
novelty: 高
feasibility: 中
---

# T012 选题：VLA 的强化学习训练

## 一句话

> 用 **RL 后训练**突破模仿学习的演示质量天花板，涵盖 GRPO、离线-在线 RL、奖励建模、语义 RL、世界模型增强和安全 RL 六条技术路线。

## 核心问题

VLA 模型依赖模仿学习（SFT），受限于演示数据的质量和覆盖范围。RL 后训练可突破此限制，但面临三大挑战：(1) 灾难性初始遗忘；(2) 样本效率极低；(3) 奖励信号难以获取。

## 六条技术路线

### 路线 1：GRPO 式策略优化
- **代表**：[[paper-2026-097-z1|Z-1]] — Shared-prefix rollout + completion-aware 奖励校准
- **核心**：提升 RL 采样效率，降低 GRPO 计算开销
- **指标**：RoboCasa 80.6%（+13.2pp）

### 路线 2：训练稳定化
- **代表**：[[paper-2026-072-force|FORCE]] — Value-calibrated warm-up + 自蒸馏
- **核心**：解决 RL 初期的灾难性遗忘和成功率骤降
- **指标**：成功率 +79%，训练加速 32.5%

### 路线 3：架构特定 RL 目标
- **代表**：[[paper-2026-067-dvla-rl|dVLA-RL]] — 离散扩散 VLA 的轨迹级 RL
- **核心**：将去噪建模为 MDP，绕过边际概率不可解问题
- **指标**：LIBERO 99.7%，RoboTwin +30.6%

### 路线 4：自监督奖励建模
- **代表**：[[paper-2026-087-warp-rm|WARP-RM]] — 时间扭曲增强生成进度奖励
- **核心**：完全自监督的密集帧级进度信号，无需人工标注
- **指标**：数据质量下降时维持 19/20 成功率

### 路线 5：语义空间 RL
- **代表**：[[paper-2026-100-sarl|SARL]] — 优化语言提示而非动作空间
- **核心**：范式转变——在语义空间做 RL 激发预训练技能
- **指标**：解锁复杂长时程任务新能力

### 路线 6：世界模型增强 RL
- **代表**：[[paper-2026-103-worldsample|WorldSample]] — 真实 rollout + 世界模型生成闭环
- **核心**：世界模型做数据增强而非环境替代
- **指标**：成功率 +28%，训练步数 -59%
- **对比**：[[paper-2026-020-world-env|World-Env]] 用世界模型**替代**真实环境（仅 5 demo）

## 与 T010/T011 的交叉

- **T010（数据效率）**：所有 RL 后训练方法本质上都在提升数据利用效率——从自身经验中学习。World-Env 仅需 5 demo 是极致案例。
- **T011（操作/灵巧）**：[[paper-2026-053-bora|BORA]] 的离线-在线 RL 框架已在灵巧操作上验证（+33% 成功率），是 T011 × T012 的交叉代表。
- **T009（安全）**：[[paper-2026-088-ppo-eal|PPO-EAL]] 提供训练时安全约束保证，是 T009 × T012 的交叉。

## 研究空白

1. **真实世界 RL 迁移** — 大部分工作仅在仿真验证（Z-1、dVLA-RL），真实世界 RL 仍受高交互成本约束
2. **长时程任务的信用分配** — 现有 RL 方法在 >500 步任务上效果未知
3. **RL + 多本体迁移** — 不同机器人形态间的 RL 策略迁移尚未探索
4. **奖励鲁棒性** — 自监督奖励（WARP-RM）和 VLM 奖励（World-Env）在 adversarial 场景下的表现未验证

## 技术路线收敛趋势

VLA RL 训练正在形成两层共识：
- **工程层**：Warm-up（FORCE）+ 采样效率（Z-1）+ 自适应调度（dVLA-RL）
- **范式层**：从动作空间 RL → 语义空间 RL（SARL）→ 世界模型增强 RL（WorldSample/World-Env）

## 相关页

- [[concept-t010-data-efficiency]]
- [[concept-t009-safety-robustness]]
- [[concept-t011-manipulation]]
- [[concept-t008-3d-vla]]
