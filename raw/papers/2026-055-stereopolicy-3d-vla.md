# StereoPolicy: Improving Robotic Manipulation Policies via Stereo Perception
- 作者：Evans Han 等
- 来源：arXiv (cs.RO, cs.CV)
- 日期：2026-05-11
- arxivId：2605.09989
- URL：https://arxiv.org/abs/2605.09989
- 相关选题：T008
- 相关度：0.88

## 研究背景
当前机器人模仿学习主要依赖单目视觉输入，但单目观测本质上缺乏可靠的深度线索和空间感知，在杂乱或几何复杂场景的精确操作中受限。已有方法尝试用RGB-D或点云补充3D信息，但需要额外传感器标定或计算开销大。

## 核心方法
StereoPolicy提出直接利用同步立体图像对的视动策略学习框架：
1. **Stereo Transformer融合**：使用预训练2D视觉编码器分别处理左右图像，通过Stereo Transformer融合表征，隐式捕获空间对应和视差线索
2. **即插即用集成**：可与diffusion-based和VLA策略无缝集成
3. **无需显式3D重建或相机标定**

## 实验结果
- RoboMimic, RoboCasa, OmniGibson三个仿真基准上一致优于RGB, RGB-D, 点云和多视角基线
- 真实机器人实验验证：桌面和双臂移动操作场景
- 证明立体视觉是连接2D预训练表征与3D几何理解的可扩展鲁棒模态

## 局限性
- 需要双目相机硬件配置
- 立体匹配的计算开销
- 未在极端遮挡或弱纹理场景验证

## 与选题关联
- **T008（3D视觉+VLA）**：StereoPolicy的Stereo Transformer提供了无需显式3D重建的空间感知方案，是与VLA结合增强3D理解的重要路径。相比显式点云输入，双目融合更轻量且可利用2D预训练模型。

## 关键引用
- Diffusion Policy
- 3D Diffusion Policy (DP3)
- VLA models (OpenVLA, RT-2)
