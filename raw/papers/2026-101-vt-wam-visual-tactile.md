# VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation

- 作者：Yupeng Zheng, Yuhang Zheng, Songen Gu, Yujie Zang, Yuxing Qin, Weize Li, Haoran Li, Wenchao Ding, Dongbin Zhao
- 来源：arXiv
- 日期：2026-07-02
- arxivId：2607.02503
- URL：https://arxiv.org/abs/2607.02503
- 相关选题：T008, T010
- 相关度：0.88

## 研究背景
Contact-rich操作要求策略能感知局部形变、压力、滑移和摩擦力，这些信息在视觉观测中时序稀疏且常不可见。现有视觉-触觉策略通常直接将触觉观测输入动作预测，但很少在动作生成过程中建模触觉形变动力学。

## 核心方法
VT-WAM是一个视觉-触觉世界动作模型，在统一的flow matching框架下联合学习：
1. **未来视觉预测** - 世界模型预测下一帧视觉
2. **触觉形变预测** - 预测触觉传感器形变
3. **动作预测** - 生成机器人动作

两大创新：
- **Asymmetric MoT注意力** - 用首帧视觉锚点桥接时序触觉动态
- **AVTAG (contact-gated Action-Visual-Tactile Attention Guidance)** - 在接触阶段引导动作查询依赖触觉证据

## 实验结果
- 6个真实世界contact-rich操作任务
- 平均成功率71.67%
- 超越Fast-WAM 26.67%，超越OmniVTLA 35.84%
- 消融实验证明触觉形变建模和接触阶段注意力引导均重要

## 局限性
- 仅验证6个任务，泛化性待考察
- 触觉传感器硬件依赖
- 接触检测阈值需调优

## 与选题关联
- **T008 (3D空间感知VLA)**：VT-WAM扩展了VLA的感知模态，触觉信息作为空间感知的重要补充
- **T010 (数据效率)**：触觉信息可减少对视觉数据的依赖，提供额外的物理交互信号

## 关键引用
- Fast-WAM (前作纯视觉WAM)
- flow matching框架
