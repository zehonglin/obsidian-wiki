# VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes

- **arXiv ID**: 2606.30645v1
- **Date**: 2026-06-29
- **Authors**: Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu
- **URL**: https://arxiv.org/abs/2606.30645v1
- **Source**: arXiv
- **Topic Match**: T008 (3D视觉+VLA空间感知)
- **Relevance**: 0.85

## Abstract

Perception-based humanoid loco-manipulation requires connecting egocentric observations and task instructions to whole-body motion. The authors address the data bottleneck by generating vision-language-kinematics (VLK) supervision synthetically in reconstructed scenes.

## Key Contributions

1. **VLK Pipeline**: 3D Gaussian Splatting重建 → 合成导航和交互轨迹 → 渲染配对egocentric观测
2. **数据规模**: 48,000条配对轨迹，零人工干预
3. **VLK Policy**: 预测短时全身运动学轨迹，whole-body tracker转化为机器人动作
4. **Sim-to-real验证**: Unitree G1物理平台上的导航和单物体运输

## 方法亮点

- **3DGS场景重建**: 利用metric-scale室内环境重建
- **合成数据策略**: 利用privileged场景信息合成轨迹，事后渲染egocentric观测
- **将VLA问题转化为VLK**: 用运动学轨迹替代底层动作，降低跨平台迁移难度

## 与选题关联

- **T008**: 使用3D Gaussian Splatting进行场景重建，为人形机器人locomanipulation提供空间感知。这和T008方向（3D视觉驱动的VLA）高度契合。

## 个人评价

将3DGS用于合成训练数据的思路很实用。48000条轨迹零人工干预，成本极低。不过VLK本质上是将action space提升到kinematics层面，对底层控制的关注较少。对T008的空间感知方向有参考价值。
