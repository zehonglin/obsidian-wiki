# LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

- 作者：Rongxu Cui, Zongzheng Zhang, Jingrui Pang, Haohan Chi, Jinbang Guo et al.
- 来源：arXiv (ECCV 2026)
- 日期：2026-06-22
- arxivId：2606.23686v1
- URL：https://arxiv.org/abs/2606.23686
- 相关选题：T009
- 相关度：0.90

## 研究背景

VLA模型在机器人操作中展现了强大的能力，但其运行安全性几乎未被系统性验证。现有评测缺乏对安全关键场景的覆盖，特别是在碰撞避免、语义误解等场景下VLA模型的鲁棒性。

## 核心方法

1. **参数化安全基准**：开发了程序化生成安全关键场景的系统，支持全面随机化
2. **Keypose驱动数据生成管道**：克服遥操作瓶颈，自动生成安全场景演示数据
3. **大规模安全数据集**：19,664条严格无碰撞演示，含大量域随机化
4. **跨范式评测**：系统评测8个VLA模型和2个具身基础模型

## 关键发现

- **泛化-安全张力**：高多样性训练数据能促进更安全的轨迹，但任务成功率受限于次优轨迹合成和语义对齐问题
- 高多样性训练 fosters safer trajectories 但 success rate 仍为瓶颈
- 语义误解是导致安全违规的重要原因

## 实验结果

- 覆盖物理安全（碰撞、约束违反）和语义安全（指令误解、场景误判）
- 发现现有VLA模型在安全关键场景下表现不佳
- 提供可扩展的安全评测pipeline和数据集

## 局限性

- 基准限于LIBERO环境，真实世界迁移待验证
- Keypose驱动生成的轨迹可能不同于人类遥操作
- 未提出安全防御方法，仅提供评测工具

## 与选题关联

**T009（VLA安全）**：直接相关。LIBERO-Safety填补了VLA安全评测的重要空白，提供了系统化的物理+语义安全基准。其发现的"泛化-安全张力"为T009选题的核心研究方向提供了重要实证支持。可作为安全评测的标准化工具。

## 关键引用

- ECCV 2026 录用
- Project Page: https://libero-safety.github.io/
