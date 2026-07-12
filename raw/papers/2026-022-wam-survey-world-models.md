# World Models and World Action Models (WAM): From Foundation Simulators to Embodied Action
- 作者：Xin Jin 等
- 来源：OpenAlex
- 日期：2026-05-06
- URL：https://openalex.org/W7160423702
- 相关选题：T008, T009, T010
- 相关度：0.90

## 研究背景
世界模型作为具身AI的基础范式，从模型强化学习发展而来，经大规模生成模型推动发生根本性变革。VLA模型建立了将高层语言意图映射到低层运动控制的框架。预测性世界模拟与动作驱动的多模态推理的自然融合催生了世界动作模型（WAM）。

## 核心方法
- **综述覆盖200+论文**，统一分类体系（taxonomy）
- **六大支柱**：
  1. 基础模型：通用模拟器（Genie, Cosmos, Sora）、游戏环境（Oasis, Matrix-Game）
  2. VLA模型：架构演进（RT-2, π₀, OpenVLA）、驾驶专用VLA、操作策略
  3. 统一生成与动作：零样本策略、可控仿真、学习范式
  4. 自动驾驶：视频生成、闭环仿真、规划、几何占据/BEV表示
  5. 效率与评测：计算加速、评测协议、合理性验证
  6. 数据集与生态：机器人学习语料、行业技术报告

## 实验结果
- 综述性质，无直接实验
- 系统梳理了从像素预测器到主动推理模拟器的进化路径

## 局限性
- 综述文章，非原创方法
- 快速发展的领域，部分最新工作可能未覆盖

## 与选题关联
- **T008（3D视觉+VLA）**：全面梳理VLA架构演进，3D感知增强是重要发展方向
- **T009（VLA安全）**：明确指出安全验证（safety verification）是关键开放挑战
- **T010（VLA数据效率）**：跨机器人泛化（cross-embodiment generalization）是核心挑战，sim-to-real评测差距仍大

## 关键引用
- Genie, Cosmos, Sora: 基础模拟器
- RT-2, π₀, OpenVLA: VLA里程碑模型
- HippoRAG, WebDreamer: 记忆与规划
