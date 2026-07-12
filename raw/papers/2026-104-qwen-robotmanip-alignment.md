# Qwen-RobotManip: Alignment Unlocks Scale for Robotic Manipulation Foundation Models

- 作者：Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, Haoyang Li, Pei Lin, Yiyang Huang, Zixing Lei, Tong Zhang, Jiazhao Zhang, Jie Zhang, Jingyang Fan, Gengze Zhou, Qihang Peng, Chenxu Lv, Xiaoyue Chen, An Yang, Fei Huang, Junyang Lin, Dayiheng Liu, Jingren Zhou, Chenfei Wu, Xiong-Hui Chen
- 来源：arXiv (Qwen团队技术报告)
- 日期：2026-06-16 (v2: 2026-06-17)
- arxivId：2606.17846
- URL：https://arxiv.org/abs/2606.17846
- 相关选题：T008, T010
- 相关度：0.95

## 研究背景
语言和多模态基础模型通过对齐异构数据并大规模训练实现强泛化。但操作数据本质异构、采集昂贵、多样性窄，使对齐和规模同时实现困难。能否将LLM的scaling recipe应用到机器人操作？

## 核心方法
Qwen-RobotManip — 基于Qwen-VL的可泛化VLA基础模型，提出统一对齐框架：

### 三维对齐
1. **表征对齐 (Representation)** — 统一不同来源的视觉-语言表征空间
2. **运动对齐 (Motion)** — 统一不同机器人平台的动作空间表示
3. **行为对齐 (Behavioral)** — 统一不同任务和场景的行为语义

### 数据工程
- **人-机器人合成管线** — 将自我中心手部演示转换为15个平台的机器人轨迹
- **严格数据治理** — 统一异构数据集
- 仅用开源数据集+人类视频，无专有数据采集
- 构建~38,100小时预训练语料

### 评测创新
- 发现标准基准无法反映预训练质量
- 采用OOD设置：RoboCasa365, LIBERO-Plus, EBench, RoboTwin-Clean2Rand, RoboTwin-IF, RoboTwin-XE

## 实验结果
- 在所有OOD设置上大幅超越π0.5等SOTA
- RoboChallenge排名第1，相对提升20%
- 涌现能力：零样本指令跟随、扰动鲁棒性、反应式错误恢复、跨本体迁移
- 真实机器人验证：AgileX ALOHA, Franka, UR, ARX

## 局限性
- 38,100小时训练成本极高
- 人-机器人转换可能在复杂任务中失真
- 15个平台仍不能覆盖所有机器人形态
- 技术报告形式，部分细节可能省略

## 与选题关联
- **T008 (3D空间感知VLA)**：Qwen-RobotManip作为新一代VLA基础模型，其三维对齐框架为T008研究提供了更好的基座模型。跨15平台的能力意味着3D感知增强可在多平台上验证。
- **T010 (数据效率)**：人-机器人合成管线直接解决数据效率问题——从人类视频生成机器人轨迹。38K小时预训练语料的构建方法对T010研究有直接参考价值。涌现的跨本体迁移能力正是T010追求的目标。

## 关键引用
- Qwen-VL系列
- π0.5基线
- Open X-Embodiment数据集
