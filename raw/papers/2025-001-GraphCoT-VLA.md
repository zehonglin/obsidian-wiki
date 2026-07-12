---
id: 2025-001
title: "A 3D Spatial-Aware Reasoning VLA for Robotic Manipulation with Ambiguous Instructions (GraphCoT-VLA)"
year: 2025
arxiv: 2508.07650
direction: vla
tags: [3D Pose-Object graph, Chain-of-Thought, ambiguous instructions, dropout hybrid reasoning]
related_topic: T008
---

# GraphCoT-VLA 论文笔记

## 核心问题
现有VLA处理模糊指令能力差，感知局限于2D静态观测，缺乏3D交互建模。

## 核心方法
- **3D Pose-Object图**: 实时构建，捕获机器人关节空间配置和物体间3D拓扑关系
- **结构化CoT推理**: 三层推理——高层任务理解规划 → 失败任务反馈 → 底层未来物体位置和机器人动作想象
- **Dropout混合推理策略**: 实现高效控制输出

## 实验结果
- 多个真实世界机器人任务验证
- 任务成功率和响应速度显著优于现有方法
- 开放环境和不确定指令下表现出强泛化和鲁棒性

## 局限性
- 3D图构建依赖已知物体位姿估计
- 未在标准benchmark（LIBERO/SIMPLER）上对比
- 真实世界任务偏简单

## 与T008关系
**相关但不同路线**。图结构建模3D空间关系是独特角度，但偏向推理层而非感知层。
