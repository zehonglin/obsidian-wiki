# OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation

- 作者：Arnav Balaji*, Arpit Bahety*, Sriniket Ambatipudi, Daniel Lam, Junhong Xu, Roberto Martín-Martín
- 来源：arXiv (RSS 2026)
- 日期：2026-06-30
- arxivId：2606.31993
- URL：https://arxiv.org/abs/2606.31993
- 相关选题：T009
- 相关度：0.92

## 研究背景
机器人操作能力快速进步，但物理安全仍是家庭机器人部署的主要障碍。仿真提供无风险的训练和评估环境，但现有仿真器缺乏检测、量化和表示损伤的通用机制。

## 核心方法
1. **DamageSim**：仿真器无关的损伤检测框架
   - 机械损伤：冲击力、压缩力、拉伸力导致的变形或断裂
   - 热损伤：极端温度接触
   - 流体损伤：液体接触导致腐蚀或短路
   - 统一损伤值计算，基于仿真器状态和物体特性
2. **OopsieBench**：32项家庭操作任务基准
   - 区分任务完成和安全执行
   - 包含不安全的目标达成捷径和安全替代策略
   - 跨平台：OmniGibson (17任务) + RoboCasa (15任务)
3. **应用场景**：实时损伤反馈遥操作、损伤条件IL/RL、VLA安全基准测试、sim-to-real安全转移

## 实验结果
- 在两个不同物理后端的仿真器中实现DamageSim
- 展示损伤感知数据收集、策略训练和安全评估的全流程
- 损伤感知策略在真实世界展示更安全行为

## 局限性
- 目前仅覆盖三类损伤（机械/热/流体）
- 家庭场景为主，未覆盖工业环境
- 损伤模型可能无法完全反映真实世界物理复杂性

## 与选题关联
- **T009（VLA安全）**：首个物理损伤感知仿真框架，直接评估VLA策略的安全性，为安全VLA研究提供标准化基准
