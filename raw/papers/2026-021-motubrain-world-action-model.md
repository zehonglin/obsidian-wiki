# MotuBrain: An Advanced World Action Model for Robot Control
- 作者：MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan 等
- 来源：arXiv (cs.RO)
- 日期：2026-04-30
- arxivId：2604.27792
- URL：https://arxiv.org/abs/2604.27792
- 相关选题：T008, T009, T010
- 相关度：0.85

## 研究背景
VLA模型在语义泛化方面表现良好，但缺乏对世界动态的细粒度建模。现有VLA难以有效整合视频预测与动作生成，且跨机器人适配需要大量数据。

## 核心方法
- **统一世界动作模型（World Action Model）**：基于UniDiffuser框架，联合建模视频和动作
- **三流Mixture-of-Transformers架构**：单一模型支持策略学习、世界建模、视频生成、逆动力学、联合视频-动作预测
- **统一多视角建模**：处理异构多模态数据（纯视频、任务无关、跨机器人数据）
- **独立文本流**：增强语言-动作耦合
- **共享跨机器人动作表示**
- **高效推理栈**：步数减少、编译、FP8量化、DiT缓存、V2A动作推理、实时分块闭环执行，50x加速，11Hz推理

## 实验结果
- RoboTwin 2.0: 清洁环境95.8%、随机环境96.1%平均成功率
- WorldArena EWMScore最强
- 新人形机器人适配仅需50-100条轨迹

## 局限性
- 计算资源需求仍然较大
- 实验主要在仿真环境
- 长时序任务的闭环执行稳定性需进一步验证

## 与选题关联
- **T008（3D视觉+VLA）**：多视角3D建模与VLA的融合，统一视频-动作预测框架
- **T009（VLA安全）**：统一世界模型可提供动作安全校验基础，世界预测能力有助于异常检测
- **T010（VLA数据效率）**：跨机器人适配仅需50-100条轨迹，显著降低数据门槛；共享动作表示支持零样本迁移

## 关键引用
- UniDiffuser: 统一扩散框架
- RoboTwin 2.0: 双臂操作benchmark
- 基于Motus模型进一步扩展
