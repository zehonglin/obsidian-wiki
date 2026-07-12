---
title: "T009 选题：VLA 安全与鲁棒性"
created: 2026-07-12
updated: 2026-07-12
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [benchmark, evaluation, vla]
sources: [raw/files-from-research-workspace/literature/directions/vla/safety-robustness.md]
related_papers: [paper-2026-014]
confidence: high
novelty: 高
feasibility: 高
---

# T009 选题：VLA 安全与鲁棒性

## 一句话

> 研究 VLA 模型在真实世界部署时的安全隐患：对抗样本攻击 / 安全约束违反 / 异常场景鲁棒性。

## 核心问题

VLA 缺乏内置安全机制，视觉/语言扰动可能导致危险动作，真实部署风险高。

## 研究空白（来自科研助手盘点）

1. **VLA 对抗攻击与防御几乎空白**（仅 2 篇）
2. 缺乏统一的 VLA 安全性评测基准和威胁模型
3. 视觉/语言扰动对 VLA 动作输出的影响未被系统研究
4. 异常场景下的 VLA 错误检测与恢复机制缺失
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

## 关联页

- [[paper-2026-014-llm-safety-robot-care]] — LLM 行为违规率评测（72 模型，54.4% vs 23.7%）
- [[prof-lin-zehong]] — 红线：不得直接使用 AI 生成论文/课题申报（来自《教师生成式人工智能应用指引》）
