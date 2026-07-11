---
title: Wiki Schema
created: 2026-07-11
updated: 2026-07-11
agent: shared
type: schema
---

# Wiki Schema

> **本 schema 由三个 agent（大总管 / 科研 / 教学）与老板共同维护。**
> 修改需在 log.md 提议，等老板批准。
>
> **2026-07-11 例外**：首批 ingest 由大总管代行科研助手职责（老板直接指令），
> 后续科研页面理应由科研助手创建。



## Domain

本 wiki 服务于老板的日常工作沉淀，覆盖三大领域：

- **manager**：日常事务、待办、人脉、会议、行程
- **research**：AI/ML 学术论文、研究方向、技术对比、科研动态
- **teaching**：教学课程、知识点、学生答疑、教材方法论

跨域通用知识（如"老板"、"电子信息学院"、"林泽洪课题"）放 `shared/`。

## Agent 写入边界

| Agent | 可写 | 不可写 | 备注 |
|---|---|---|---|
| **大总管** (main) | `manager/`, `shared/` | `research/` 私有页, `teaching/` 私有页 | 跨域读 OK |
| **科研助手** (research-manager) | `research/`, `shared/` | `manager/` 私有页, `teaching/` 私有页 | |
| **教学助手** (teaching-manager) | `teaching/`, `shared/` | `manager/` 私有页, `research/` 私有页 | |
| **老板本地 agent** (Claude Code 等) | 全部（git 合并） | — | 写入通过 git push 走 PR 流程 |
| **写入 `shared/`** | 任何 agent 可提议 | — | 必须标 `[proposed-by:<agent>]`，等老板确认 |

**例外**：质量修正（typo、broken link、过期日期）任何 agent 静默修，不需提议。

## 文件命名

- 小写 + 短横线，无空格：`transformer-architecture.md`
- 中文也用短横线：`林泽洪教授.md` → 实际推荐 `prof-lin-zehong.md`（避免编码问题）
- 单数概念：`vla-model.md`，不复数

## Frontmatter（必填）

```yaml
---
title: 页面标题
created: YYYY-MM-DD              # 创建日期
updated: YYYY-MM-DD              # 最后修改日期（每次更新必 bump）
type: entity | concept | comparison | query | summary | schema
agent: manager | research | teaching | shared   # 谁拥有这页
domain: ai-research | teaching | management | ...  # 业务域
visibility: shared | private      # 是否对其他 agent 可见
tags: [from taxonomy]            # 必须从下方字典选
sources: [raw/articles/xxx.md]   # 原始资料引用
confidence: high | medium | low  # 主张证据强度（可选）
contested: true                  # 有未解决矛盾（可选）
contradictions: [page-slug]      # 与哪些页冲突（可选）
---
```

## Tag 字典（核心 20 个，要新 tag 先在这里登记）

### 模型与方法
- `model` — 具体的模型/系统（如 GPT-4, 3D-Mix）
- `architecture` — 架构设计（如 Transformer, Mamba）
- `training` — 训练方法（如预训练、SFT、RLHF）
- `inference` — 推理优化（如量化、KV cache）

### 多模态与机器人
- `vla` — Vision-Language-Action 模型
- `mllm` — Multimodal Large Language Model
- `vision-language` — 视觉-语言预训练
- `spatial-reasoning` — 空间智能、3D 理解
- `navigation` — 机器人导航
- `manipulation` — 机器人操作

### 学习范式
- `imitation-learning` — 模仿学习
- `reinforcement-learning` — 强化学习
- `self-supervised` — 自监督

### 评测与实体
- `benchmark` — 评测基准
- `evaluation` — 评测方法
- `dataset` — 数据集
- `person` — 研究者
- `lab` — 实验室/机构
- `company` — 公司

### 元数据
- `comparison` — 横向对比
- `survey` — 综述
- `timeline` — 时间线

**新增 tag 流程**：在 SCHEMA.md 这里登记 → 告知所有 agent → 才能用。

## 页面门槛

| 动作 | 条件 |
|---|---|
| **创建新页** | 实体/概念被 2+ 来源提到，或某来源的核心主题 |
| **更新已有页** | 来源提到该主题的新信息 |
| **不创建页** | 脚注里的路过提及、与领域无关 |
| **拆分页** | 单页 > 200 行 |
| **归档页** | 内容完全过时 → 移到 `_meta/archive/` |

## 每页强制要求

- ✅ YAML frontmatter（完整字段）
- ✅ 至少 2 个 `[[wikilinks]]` 指向其它页
- ✅ 综合 3+ 来源的页面，段落末尾标 `^[raw/articles/xxx.md]`
- ✅ 修改必须 bump `updated` 字段
- ✅ 新页必须在 `index.md` 注册

## 矛盾处理流程

1. 检查日期：更新来源通常优先
2. 真矛盾：两个主张都保留，标日期和来源
3. Frontmatter 标 `contested: true` 和 `contradictions: [other-page]`
4. log.md 标 `[needs-review]`
5. 等老板裁决

## 更新政策

- 改自己的页：静默 commit，log 写一行
- 改别人的页：先 PR 提议（git branch），让对方 agent 知道
- 改 SCHEMA.md：必须老板批准
- 改 index.md：写入页的同时同步
- 改 log.md：只追加，不修改

## 三个 agent 协作礼仪

- 写入前先 `grep -r "关键词" ~/wiki/` 看有没有重复页
- 发现别人领域的相关页 → 在 log 写 `[related-to:research]` 提示
- 写完一个源，至少 cross-reference 2 个相关页
- 每周一次"邻居会议"：每个 agent 提 1-3 个 schema 改进建议
