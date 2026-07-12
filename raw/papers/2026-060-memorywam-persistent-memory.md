# MemoryWAM: Efficient World Action Modeling with Persistent Memory

- 作者：Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li, Linning Xu, Zhengrong Xue, Zhecheng Yuan, Dahua Lin, Jiangmiao Pang, Huazhe Xu
- 来源：arXiv
- 日期：2026-06-18
- arxivId：2606.20562v1
- URL：https://arxiv.org/abs/2606.20562
- 相关选题：T008, T010
- 相关度：0.92

## 研究背景

真实世界机器人操作不仅需要理解当前观测，还需要记忆和动力学建模。世界动作模型（WAM）通过联合建模视觉前瞻和动作来应对这一挑战。但现有WAM面临根本性权衡：高效推理方法仅依赖有限窗口的近期观测，在非马尔可夫环境中表现不佳；而保留长历史的方法计算和空间成本随序列长度急剧增长。

## 核心方法

1. **混合记忆设计**：
   - 近期帧：保留短时间窗口的完整信息
   - 事件边界锚帧：在关键事件转换点保存帧
   - 压缩Gist Token：用紧凑token总结长程历史
2. **定制注意力机制**：支持检索详细短期上下文和压缩长期上下文
3. 持续记忆支持记忆依赖的决策，同时降低推理延迟和GPU内存使用

## 实验结果

- 在长时间范围、记忆依赖的操作任务上（仿真+真实世界）
- 优于强VLA和WAM基线
- 保持良好的计算效率

## 局限性

- 事件边界检测依赖额外模块
- Gist token压缩可能导致部分历史信息丢失
- 主要在操作任务上验证，导航场景未充分探索

## 与选题关联

**T008（3D视觉+VLA空间感知）**：MemoryWAM的持续记忆机制为VLA模型提供了时间维度的感知增强，与3D空间感知形成互补——两者结合可实现更完整的场景理解（空间+时间）。

**T010（VLA数据效率）**：通过混合记忆设计高效利用历史信息，MemoryWAM减少了模型对大量训练数据的需求。记忆增强使模型能在更少的训练样本下做出更好的决策。

## 关键引用

- World Action Models (WAM) - 联合建模视觉前瞻和动作
- VLA baselines - 视觉语言动作模型
