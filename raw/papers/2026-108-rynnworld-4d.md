# RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation

- **arXiv**: 2607.06559
- **Date**: 2026-07-07
- **Authors**: Haoyu Zhao, Xingyue Zhao, Siteng Huang, Xin Li, Deli Zhao, Zhongyu Li
- **URL**: https://arxiv.org/abs/2607.06559
- **Topics**: T008 (3D视觉+VLA)
- **Relevance**: 0.90

## 摘要

提出RynnWorld-4D，一个从单张RGB-D图像和语言指令联合生成未来RGB帧、深度图和光流的生成模型。核心观点是同步的RGB-DF（RGB+深度+光流）提供了物理基础的4D动态表示，比2D像素视频更接近机器人末端执行器动作。

## 核心贡献

1. **RGB-DF 4D世界模型**: 统一扩散过程中同时生成RGB、深度、光流，确保外观、几何和运动一致性
2. **三分支架构**: 跨模态注意力 + 帧级3D RoPE
3. **Rynn4DDataset 1.0**: 超过2.544亿帧的自中心人类和机器人操作视频数据集（含深度和光流伪标签）
4. **RynnWorld-4D-Policy**: 逆动力学头单次前向传播输出动作，绕过多步去噪

## 关键技术

- 灵巧双手操作任务达到SOTA
- 在需要空间精度和时间协调的任务上表现尤为出色

## 与选题关联

- **T008**: 4D世界模型显式建模3D几何（深度）和时间动态（光流），直接服务于机器人操作
