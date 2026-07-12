---
title: "T009 选题：VLA 安全与鲁棒性"
created: 2026-07-12
updated: 2026-07-12
batch: 3
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [benchmark, evaluation, vla]
sources: [raw/files-from-research-workspace/literature/directions/vla/safety-robustness.md]
related_papers: [paper-2026-014-llm-safety-robot-care, paper-2026-005-vla-fool, paper-2026-040-rovla, paper-2026-046-pre-vla, paper-2026-063-libero-safety, paper-2026-080-foresight-safety-vla, paper-2026-096-oopsieverse]
confidence: high
novelty: 高
feasibility: 高
---

# T009 选题：VLA 安全与鲁棒性

## 一句话

> 研究 VLA 模型在真实世界部署时的安全隐患：对抗样本攻击 / 安全约束违反 / 异常场景鲁棒性。

## 核心问题

VLA 缺乏内置安全机制，视觉/语言扰动可能导致危险动作，真实部署风险高。

## 研究空白（来自科研助手盘点 + batch 3 更新）

1. **VLA 对抗攻击与防御**——[[paper-2026-005-vla-fool]] 首次系统覆盖攻击面，防御侧仅有 [[paper-2026-040-rovla]] 的训练时一致性约束
2. **安全评测基准**——三篇基准工作已初步覆盖：[[paper-2026-063-libero-safety]]（广度物理+语义）、[[paper-2026-080-foresight-safety-vla]]（诊断级过程度量）、[[paper-2026-096-oopsieverse]]（物理损伤感知）
3. **运行时安全层**——[[paper-2026-046-pre-vla]] 提出「先发式验证」范式，但仅 LIBERO 验证
4. 异常场景下的 VLA 错误检测与恢复机制仍缺失
5. 安全微调策略在 VLA 上的应用探索不足

## 实验设计方向

- **对抗鲁棒性**：像素级攻击 / 自然扰动 / 文本指令扰动 / OOD 物体
- **安全约束**：碰撞避免 / 禁区约束 / 力度控制 / 动作边界
- **异常场景**：传感器故障 / 物体移位 / 动态障碍 / 机械故障
- **防御方法**：输入预处理 / 动作安全校验层 / 安全微调（LoRA）

## 切入点

1. **定义 VLA 统一威胁模型** — 首次系统分类攻击面
2. **动作安全校验层** — 即插即用的安全模块
3. **VLA 安全微调方法** — 轻量级安全对齐

## Batch 3 新增论文（2026-07-12）

| 论文 | 维度 | 核心贡献 |
|---|---|---|
| [[paper-2026-005-vla-fool]] | 攻击 | 多模态对抗攻击（文本+视觉+跨模态），失败率 >93% |
| [[paper-2026-040-rovla]] | 训练防御 | 三重一致性约束（IC+EC+OC），显式建模鲁棒性 |
| [[paper-2026-046-pre-vla]] | 运行时 | 动作执行前验证 + 自适应重采样，+6.83pp |
| [[paper-2026-063-libero-safety]] | 基准 | 参数化安全基准（19,664 条），ECCV 2026 |
| [[paper-2026-080-foresight-safety-vla]] | 基准 | 13 类安全分类 + 过程级度量（CC/RET） |
| [[paper-2026-096-oopsieverse]] | 基准 | 物理损伤感知仿真（DamageSim），RSS 2026 |

## 安全研究三维框架

基于 batch 3 论文，T009 可按三个维度展开：

```
          攻击 ←→ 防御
              ↑
         评测基准
         （基准层）
```

- **攻击面**：[[paper-2026-005-vla-fool]]
- **防御面（训练时）**：[[paper-2026-040-rovla]]
- **防御面（运行时）**：[[paper-2026-046-pre-vla]]
- **评测基准**：[[paper-2026-063-libero-safety]] / [[paper-2026-080-foresight-safety-vla]] / [[paper-2026-096-oopsieverse]]

## 关联页

- [[paper-2026-014-llm-safety-robot-care]] — LLM 行为违规率评测（72 模型，54.4% vs 23.7%）
- [[prof-lin-zehong]] — 红线：不得直接使用 AI 生成论文/课题申报（来自《教师生成式人工智能应用指引》）
