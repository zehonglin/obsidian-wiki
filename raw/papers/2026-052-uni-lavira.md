# Uni-LaViRA: Language-Vision-Robot Actions Translation for Unified Embodied Navigation
- 作者：Hongyu Ding, Sizhuo Zhang, Ziming Xu, Jinwen Guo, Hongxiu Liu, Xingzhi Cheng, Zixuan Chen, Haifei Qi, Duo Wang, Hao Xu, Jieqi Shi, Yifan Zhang, Jing Huo, Jian Cheng, Yang Gao, Jiebo Luo
- 来源：arXiv (cs.RO, cs.CV)
- 日期：2026-05-26
- arxivId：2605.27582
- URL：https://arxiv.org/abs/2605.27582
- 相关选题：T008（3D视觉+VLA空间感知）、T010（VLA数据效率与跨机器人适配）
- 相关度：0.85

## 研究背景
当前具身导航主流范式是训练越来越大的VLA基础模型，用海量机器人轨迹数据获得泛化性（scaling law思路）。但导航决策的本质结构——语言推理→视觉定位→空间动作——恰好落在预训练MLLM的自然输出流形内（方向语义+像素级目标），不需要端到端训练回归连续控制量。作者据此提出导航的泛化性可以"结构性地获得"而非仅靠数据规模。

## 核心方法
**三层Agent架构**（Language-Vision-Robot Actions Translation）：
1. **Language Action Model**（Gemini-3.1-Pro）：从任务指令+全景观测+历史中推理出离散方向动作（turn/backtrack/go_stair/double_check）
2. **Vision Action Model**（Qwen3.5-27B）：在选定方向视图上输出bounding box，直接在原始像素上定位目标
3. **Robot Action Controller**（确定性几何控制器）：bbox→深度反投影→3D点→FMM路径规划→执行

**两个关键机制**：
- **TODO List Memory (TDM)**：维护结构化子目标清单（content/status/result），每步更新并重读未完成项到注意力窗口，解决长指令注意力漂移
- **Second Chance Backtrack (SCB)**：回溯到错误前的航点，将失败子轨迹作为上下文重新规划，将错误转化为规划证据

**跨机器人部署**：仅替换底层控制器即可适配轮式（Agilex Cobot Magic）、四足（Unitree Go1）、人形（Unitree G1）、无人机（自建四旋翼）四种异构平台。

## 实验结果
**零训练**在6个基准上：
- VLN-CE R2R: 60.7% SR（接近需要训练的OmniNav 69.5%）
- VLN-CE RxR: 51.3% SR
- HM3D-v2: 77.7% SR（超越训练方法VLFM 63.0%）
- HM3D-OVON: 60.0% SR
- MP3D-EQA: 54.7% ACC
- OpenUAV: 40.0% SR（首个零训练方法，接近AerialVLA 37.6%）

消融实验证实TDM在长指令上提升显著，SCB在困难场景提供约3-5% SR增益。

## 局限性
1. 仅适用于**无接触导航**（contact-free navigation），不适用于接触密集型操作（如灵巧操控需要力矩/阻抗等不在MLLM流形内的动作）
2. 依赖商业API（Gemini-3.1-Pro），推理成本较高，延迟较大
3. 在R2R上仍落后最佳训练方法约9个百分点（60.7% vs 69.5%）
4. 底层控制器仍需为每种机器人单独实现

## 与选题关联
- **T008（3D视觉+VLA空间感知）**：Uni-LaViRA利用深度通道进行3D点反投影和地图构建，展示了纯视觉（无3D预训练）的替代路径，但空间理解依赖MLLM的隐式推理而非显式3D表示
- **T010（VLA数据效率）**：零训练跨4种机器人部署，是数据效率的极致案例。证明了对于导航任务，MLLM的预训练知识足以支撑跨具身迁移，无需额外机器人数据
- **核心启示**：导航动作空间落在MLLM自然输出流形内 → 不需要训练；操作动作空间在流形外 → 仍需训练。这一分界线对T008/T010选题的方法选择有重要指导意义

## 关键引用
- LaViRA (会议版, 本文前身)
- NavFoM, OmniNav, ABot-N0 (训练型导航基础模型)
- Reflexion (自我反思模式启发SCB)
- MemGPT (记忆管理启发TDM)
