# RoVLA: Multi-Consistency Constraints for Robust Vision-Language-Action Models
- 作者：Jingzhou Luo, Yifan Wen, Yongjie Bai, Xinshuai Song, Yang Liu, Liang Lin (中山大学)
- 来源：arXiv
- 日期：2026-05-25
- arxivId：2605.19678
- URL：https://arxiv.org/abs/2605.19678
- 相关选题：T009（VLA安全性与鲁棒性）、T008（3D视觉+VLA）
- 相关度：0.95

## 研究背景
现有VLA模型在标准基准上表现优异，但在视觉观察变化（视角、光照、背景）、语义等价指令改写、以及复合扰动下表现脆弱。LIBERO-Plus揭示三种典型失败模式：伪视觉理解、伪语言跟随、伪组合泛化。根本原因在于模型依赖浅层跨模态关联而非稳定的任务相关不变性。

## 核心方法
RoVLA提出三种互补的一致性约束机制：
1. **Instructional Consistency (IC)**：语义等价指令改写下保持稳定的行为接地
2. **Evolutionary Consistency (EC)**：在flow-matching生成过程中保持一致的动作意图
3. **Observational Consistency (OC)**：视觉和本体感受扰动前后保持一致预测

核心思想：在端到端策略学习中显式建模不变性，而非将鲁棒性作为大规模数据训练的副产品。

## 实验结果
- LIBERO-Plus、RoboTwin 2.0、真实世界任务上全面超越基线
- 在多样化任务和观察偏移下展现更强鲁棒性
- 比π0、π0.5等现有VLA显著提升
- 代码将开源：https://github.com/HCPLPLab-SYSU/RoVLA

## 局限性
- 三种一致性约束的超参数调优可能较复杂
- 训练计算开销增加（需要三种一致性损失）
- 仅在有限的真实世界场景验证

## 与选题关联
- **T009（VLA安全性）**：直接解决VLA鲁棒性问题，三种一致性约束为对抗防御提供新思路
- **T008（3D视觉+VLA）**：OC约束可扩展到3D观察扰动，增强空间感知鲁棒性

## 关键引用
- LIBERO-Plus (Fei et al.) - VLA鲁棒性评测基准
- π0/π0.5 - 主流VLA基线
- DrQ, Mean Teacher - 一致性学习经典方法
