# DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation

- 作者：Yunchao Yao, Zhuxiu Xu, Tianqi Zhang, Zixian Liu, Sikai Li, et al. (15 authors)
- 来源：arXiv
- 日期：2026-07-09
- arxivId：2607.08751v1
- URL：https://arxiv.org/abs/2607.08751v1
- 相关选题：T010（VLA数据效率与少样本跨任务/跨机器人适配）
- 相关度：0.88

## 研究背景

通用灵巧操作策略需要超越单一任务的系统化评测基准。现有基准在任务多样性、本体覆盖和可控视觉变化方面仍然有限，阻碍了跨任务和跨本体泛化的研究。

## 核心方法

DexVerse是一个大规模模块化灵巧操作基准：
- **100个任务**：覆盖抓取与重置、铰接物体交互、工具使用、双臂协调、非抓取控制、接触丰富行为、多目标执行和长时程多阶段任务
- **3个机械臂 + 6个灵巧手**：支持多种本体，可扩展新本体
- **可配置视觉变化**：纹理、背景、光照和相机视角
- **VR遥操作界面**：3,180条示范数据，含本体感知、RGB、深度、点云和状态观测
- 基线评测：Diffusion Policy, DP3, OpenVLA, π₀.₅ 在19个任务上测试

## 实验结果

结果显示任务泛化和视觉运动鲁棒性方面存在重大挑战。OpenVLA和π₀.₅等VLA模型在跨任务泛化上仍有显著困难，确立了DexVerse作为通用灵巧操作测试平台的价值。

## 局限性

- 基准主要面向仿真环境，sim-to-real gap未被完全覆盖
- 任务虽多但可能无法完全反映真实世界的复杂物理交互
- 本体种类仍有限（3臂6手），真实机器人形态更多样

## 与选题关联

**T010（VLA数据效率与少样本跨任务/跨机器人适配）**：DexVerse直接评估VLA模型的跨任务和跨本体泛化能力。其多本体设计（3臂6手）为研究少样本跨机器人适配提供了理想测试平台。基准揭示OpenVLA等现有VLA在任务泛化上的不足，凸显了高效适配方法的重要性。3,180条多模态示范数据可支撑少样本学习研究。

## 关键引用

- 项目页面：https://ycyao216.github.io/DexVerse.site
- 评测模型：Diffusion Policy, DP3, OpenVLA, π₀.₅
