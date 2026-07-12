# WARP-RM: Warp-Augmented Relative Progress Reward Model for Data Curation
- 作者：Justin Yu, Ken Goldberg 等 (UC Berkeley)
- 来源：arXiv
- 日期：2026-06-26
- arxivId：2606.28320v1
- URL：https://arxiv.org/abs/2606.28320v1
- 相关选题：T010
- 相关度：0.90

## 研究背景
扩大模仿学习规模需要大量数据，但人类遥操作不可避免产生混合质量演示（包含犹豫顿和恢复动作）。现有帧级进度奖励模型存在标签噪声或需要昂贵人工标注。

## 核心方法
提出WARP (Warp-Augmented Relative Progress)，全自监督算法：
1. 通过时间扭曲增强（变速播放和倒放）生成逐帧进度目标
2. 训练WARP-RM预测输入帧间归一化经过时间
3. 聚合重叠窗口预测产生密集帧级进度信号
4. WARP-BC：利用标量奖励估计在行为克隆中加权高优势动作块

## 实验结果
- 物理双臂机器人T恤折叠任务（从随机揉皱开始）
- 数据集质量下降时，WARP-BC维持19/20成功率，而vanilla BC降至2/20
- 吞吐量提升最高18倍

## 局限性
- 目前仅在单一长时序任务上验证
- 时间扭曲增强策略可能不适用于所有类型操作

## 与选题关联
**T010（VLA数据效率）**：WARP直接解决数据质量问题对VLA训练的影响，自监督进度评估减少对高质量标注的依赖，与T010"降低VLA数据门槛"目标高度一致。

## 关键引用
- Bimanual robot manipulation
- Imitation learning, behavior cloning
