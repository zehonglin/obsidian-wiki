# World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays (REGEN)
- 作者：Manish Kumar Govind, Dominick Reilly, Smit Patel, Hieu Le, Srijan Das
- 来源：arXiv (cs.RO, cs.CV)
- 日期：2026-06-25
- arxivId：2606.27374v1
- URL：https://arxiv.org/abs/2606.27374
- 相关选题：T010
- 相关度：0.85

## 研究背景
世界动作模型（WAMs）不仅预测机器人动作，还能生成未来视觉观察。持续学习中的灾难性遗忘是VLA实际部署的关键瓶颈，传统方法需存储原始人类演示进行经验回放。

## 核心方法
REGEN（Recurrent Generative Replay）：
1. 利用WAM的生成能力合成伪回放轨迹
2. 递归查询WAM，仅需先前任务指令和当前任务观察即可生成回放
3. 无需存储原始人类演示即可排练已学任务
4. 在仿真和真实世界操作中验证

## 实验结果
- 相比顺序微调，灾难性遗忘减少最高50%
- 接近有特权经验回放方法的性能
- 识别出生成回放的主要瓶颈：长时间程视觉退化和动作-观察不一致

## 局限性
- WAM生成质量随horizon增加而退化
- 动作-观察一致性在复杂任务中难以保证
- 需要训练额外的WAM模型

## 与选题关联
- **T010（VLA数据效率）**：REGEN直接解决VLA持续学习中的数据效率问题——无需存储原始演示即可抵抗遗忘，为VLA的跨任务适配提供了新范式。
