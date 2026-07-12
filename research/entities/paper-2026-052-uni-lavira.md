---
title: "Uni-LaViRA：零训练统一具身导航——三层 Agent 跨四类机器人"
created: 2026-07-12
updated: 2026-07-12
type: entity
agent: research
domain: ai-research
visibility: shared
tags: [model, navigation, vla, mllm, benchmark]
sources: [raw/papers/2026-052-uni-lavira.md]
arxiv: "2605.27582"
date: 2026-05-26
related_topic: T013
confidence: high
---

# Uni-LaViRA 论文

**作者**：Hongyu Ding, Sizhuo Zhang, Ziming Xu 等 16 人
**日期**：2026-05-26 | arXiv: 2605.27582
**研究方向**：`T013`（Navigation / Locomotion）

## 核心一句话

> 导航动作落在 MLLM 的自然输出流形内（方向语义 + 像素定位），因此**零训练**三层 Agent 架构即可在 6 个基准上接近/超越训练方法——HM3D-v2 上 77.7% SR 超越 VLFM（63.0%）。

## 关键创新

1. **三层解耦架构**：Language Action Model（Gemini-3.1-Pro 推理方向）→ Vision Action Model（Qwen3.5-27B 定位目标）→ 确定性几何控制器（路径执行）
2. **TODO List Memory (TDM)**：结构化子目标清单解决长指令注意力漂移
3. **Second Chance Backtrack (SCB)**：失败子轨迹作为重规划上下文，将错误转化为规划证据
4. **跨机器人零适配**：仅替换底层控制器即适配轮式 / 四足 / 人形 / 无人机四种平台

## 实验结果

| 基准 | Uni-LaViRA（零训练） | 对比 |
|---|---|---|
| VLN-CE R2R | 60.7% SR | 接近 OmniNav 69.5%（需训练） |
| HM3D-v2 | **77.7% SR** | 超越 VLFM 63.0%（需训练） |
| HM3D-OVON | 60.0% SR | — |
| MP3D-EQA | 54.7% ACC | — |
| OpenUAV | 40.0% SR | 首个零训练方法 |

## 价值定位

Uni-LaViRA 的核心洞见——**导航动作在 MLLM 流形内、操作动作在流形外**——为 [[concept-t013-navigation]] 提供了关键理论分界线。这一分界直接解释了为什么导航可以零训练而操作不能。

## 局限性

- ⚠️ 仅适用无接触导航（contact-free），力矩/阻抗控制不在 MLLM 流形内
- ⚠️ 依赖商业 API（Gemini-3.1-Pro），推理成本高、延迟大
- ⚠️ R2R 上仍落后最佳训练方法 ~9pp

## 相关 wiki 页

- [[concept-t013-navigation]] — 本文所属选题总览
- [[paper-2026-006-metanav]] — 同为零训练导航，MetaNav 侧重元认知、Uni-LaViRA 侧重架构解耦
- [[paper-2026-093-vlk]] — 人形 loco-manipulation 的合成数据路线（VLK）
- [[paper-2026-022-wam-survey]] — WAM 综述中的导航部分
