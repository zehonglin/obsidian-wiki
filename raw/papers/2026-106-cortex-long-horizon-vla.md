# Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation

- 作者：Jiaqi Peng, Xiqian Yu, Delin Feng, Yuqiang Yang, Wenzhe Cai, Jing Xiong, Ganlin Yang, Jinliang Zheng, Jiafei Cao, Xueyuan Wei, Jiangmiao Pang, Yuan Shen, Tai Wang
- 来源：arXiv
- 日期：2026-07-06
- arxivId：2607.05377v1
- URL：https://arxiv.org/abs/2607.05377v1
- 相关选题：T010
- 相关度：0.90

## 研究背景

VLA模型在短时程操作任务上表现良好，但在长时程任务中因马尔可夫性质（仅依赖当前观测）而表现不佳。分层双系统方法（高层VLM规划+低层VLA执行）存在高层规划语义与低层执行运动学之间的鸿沟。

## 核心方法

Cortex提出**双向对齐的具身智能体框架**：
1. **32个标准技能原语**：将操作子任务标准化为32个规范技能原语，桥接高层规划与低层执行
2. **可控性原则注入**：在数据生成管线中注入代表性物体属性和改进的轨迹可达性
3. **大规模自动标注**：自动标注4k+小时开源视频数据，生成30小时仿真数据
4. **事件均衡采样策略**：构建训练数据以更好地处理子任务转换中的规划歧义
5. **推理时harness工程**：从任务上下文到技能约束的精心设计

## 实验结果

- Libero-long: 比单块基线高 **+3.1%**
- RoboTwin: 比基线高 **+4.1%**
- **零样本完成未见真实世界长时程任务**（如多阶段化学实验），仅通过VLM+微调VLA组合实现
- 证明了VLM+VLA组合的范式优势——仅靠VLA微调无法实现

## 局限性

- 32个技能原语的粒度可能不足以覆盖所有任务类型
- 依赖大规模自动标注质量
- 开环VLM评估与闭环系统评估之间仍有差距

## 与选题关联

**T010（VLA数据效率与跨任务适配）**：Cortex的核心理念——通过标准化技能原语和大规模自动数据标注来提升VLA的长时程任务能力——直接呼应T010的数据效率主题。4k+小时视频自动标注管线和事件均衡采样策略为降低VLA数据门槛提供了新方案。零样本长时程任务完成能力展示了VLM+VLA组合在减少对特定任务微调依赖方面的潜力。
