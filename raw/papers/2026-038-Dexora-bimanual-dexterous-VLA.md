# Dexora: Open-source VLA for High-DoF Bimanual Dexterity
- 作者：Zongzheng Zhang, Jingrui Pang, Zhuo Yang, Kun Li, et al. (清华+BAAI+港大+上交+北大)
- 来源：arXiv (ICRA 2026)
- 日期：2026-05-18
- arxivId：2605.18722
- URL：https://arxiv.org/abs/2605.18722
- 相关选题：T008, T010
- 相关度：0.90

## 研究背景
现有VLA系统要么仅支持双臂夹爪（低DoF），要么仅支持单臂灵巧手操作，缺乏面向双臂双灵巧手高DoF操作的开源VLA系统。高维灵巧控制对端到端VLA学习至关重要。

## 核心方法
1. **混合遥操作管线**：外骨骼背包捕获粗手臂运动学，Apple Vision Pro提供无标记手指追踪，控制36-DoF双臂双灵巧手平台及MuJoCo数字孪生
2. **大规模数据集**：10万仿真轨迹(6.5M帧)+1万真实遥操作片段(2.92M帧)，200个任务
3. **数据质量感知训练**：离线判别器对演示质量打分，在扩散Transformer策略训练中降权低质量演示
4. **跨embodiment泛化**：同一策略可迁移至单臂夹爪、双臂夹爪和低DoF手

## 实验结果
- 基础任务成功率90%
- 灵巧任务平均成功率66.7% vs 基线51.7%（+15%）
- 强OOD泛化和跨embodiment迁移能力
- 数据质量判别器对灵巧性能关键

## 局限性
- 仅覆盖双臂场景，未涉及移动操作
- 仿真环境限于桌面场景
- 数据采集依赖专用硬件（外骨骼+Vision Pro）

## 与选题关联
- **T008（3D视觉+VLA）**：多视角RGB输入（4视图）+高DoF VLA系统，空间感知对灵巧操作至关重要
- **T010（VLA数据效率）**：质量感知训练策略、仿真-真实互补数据、跨embodiment迁移，直接相关数据效率问题

## 关键引用
- RT-2, OpenVLA, π₀, π₀.5, RDT等VLA基线
- DexMimicGen用于数据扩增
- Qwen2.5-VL用于自动任务生成
