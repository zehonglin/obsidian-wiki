# Behavior Prompting Policy: Demonstrations as Prompts for Manipulation

- **arXiv ID**: 2606.30457v1
- **Date**: 2026-06-29
- **Authors**: Austin Patel, Ben Pekarek, Joel Enrique Castro Hernandez, et al.
- **URL**: https://arxiv.org/abs/2606.30457v1
- **Source**: arXiv
- **Topic Match**: T010 (少样本适配)
- **Relevance**: 0.85

## Abstract

Behavior prompting enables robots to perform new tasks at inference time given a single human demonstration (behavior prompt). The authors present BPP, an in-context visuomotor architecture.

## Key Contributions

1. **Behavior Prompting范式**: 单次人类演示作为"行为提示"，推理时即时执行新任务
2. **BPP架构**: in-context visuomotor网络，将行为提示和当前观测转化为机器人动作
3. **iPhUMI数据接口**: 手持操作接口，用于收集多样化训练数据
4. **评估基准**: DrawAnything和LIBERO-Gen，评估test-time对未知任务的适应

## 方法亮点

- **任务多样性是关键**: 发现任务多样性（而非数据量）是prompting能力的核心驱动因素
- **无需fine-tuning**: 通过单次演示即可命令机器人完成已知任务或定义新能力
- **类似in-context learning**: 将LLM的in-context learning范式迁移到机器人操作领域

## 与选题关联

- **T010**: 直接关联少样本适配方向。单次演示即可执行新任务，是VLA few-shot learning的重要进展。任务多样性>数据量的发现对数据采集策略有指导意义。

## 个人评价

"Behavior prompting"的概念很优雅，将LLM的prompting范式自然延伸到机器人领域。iPhUMI作为低成本手持接口也很实用。关键insight——任务多样性是prompting能力的关键——对未来VLA数据集构建有重要指导价值。
