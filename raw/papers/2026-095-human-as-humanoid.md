# Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments

- 作者：Xiaopeng Lin, Ruoqi Yang, Shijie Lian, Zhaolong Shen, Bin Yu, Changti Wu, Haibao Liu, Yuxiang Zhang, Hong Li, Qiyuan Su, Haochen Liu, Xuguo He, Yukun Shi, Cong Huang, Zhirui Zhang, Bojun Cheng, Kai Chen
- 来源：arXiv
- 日期：2026-06-30
- arxivId：2606.32009
- URL：https://arxiv.org/abs/2606.32009
- 相关选题：T008, T010
- 相关度：0.88

## 研究背景
VLA模型需要高质量观测-动作监督来学习可部署的动作分布，但扩展机器人数据困难，尤其对高自由度人形机器人。遥操作提供控制器对齐的监督，但效率低；人类自我中心视频包含多样双臂操作但无法直接提供可执行动作。

## 核心方法
1. **Human-as-Humanoid框架**：将人类演示转换为人形机器人可用的观测-动作监督
2. **基于PrimeU**：60-DoF上半身人形机器人，人类对齐的 embodiment
3. **自我-外部视频同步**：自我中心观测（部署对齐）+ 外部运动恢复
4. **分级IK重定向**：将恢复的人类运动通过IK转换为控制器对齐的60-DoF动作块
5. **FK感知监督**：训练VLA时保持腕部和指尖任务空间几何

## 实验结果
- 运动恢复、机器人动作空间、真实机器人部署三个层面验证
- 原始演示吞吐量比遥操作提升4.8-7.2倍
- 仅用转换后人类标签后训练的策略可在真实机器人部署，无需目标任务机器人演示

## 局限性
- IK重定向可能丢失人类运动的某些细微特性
- 依赖同步的多视角设置
- 需要特定的人形机器人硬件设计（人类对齐）

## 与选题关联
- **T008（3D+VLA）**：自我-外部视角转换涉及3D空间感知
- **T010（数据效率）**：人类视频作为VLA训练数据源，大幅提升数据采集效率，解决数据扩展瓶颈
