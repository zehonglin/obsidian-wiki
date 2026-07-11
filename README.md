# 📚 obsidian-wiki

> **多 agent 协同的私有知识库** —— 由三个 AI 助手（大总管 / 科研 / 教学）与老板共建，
> 基于 Karpathy LLM Wiki 模式 + Hermes Agent 的 llm-wiki skill v2.1.0。

---

## 🎯 这是什么

不是传统的文档仓库，**是一个"会自己长"的 wiki**：

- **三个 agent 各管一摊**（日常 / 科研 / 教学），但跨域共享一个 schema
- **每页 YAML frontmatter 严格化**（含 `agent:` 字段标归属）
- **Tag 字典封闭**（20 个一级 tag，新增要先登记）
- **每次操作 log 留痕**（append-only，`log.md`）
- **本地 agent 可直连**（通过 git，无云依赖）

## 🏗️ 目录结构

```
.
├── SCHEMA.md                 # wiki 规范（agent 边界、frontmatter、tag 字典）
├── index.md                  # 内容目录（按 agent + type 分区）
├── log.md                    # 操作日志（append-only，500 条按年轮转）
│
├── shared/                   # 跨 agent 共享
│   ├── entities/             #   人、组织、跨域项目
│   ├── concepts/             #   通用概念
│   ├── comparisons/
│   └── queries/
│
├── manager/                  # 大总管 (main agent)
│   ├── entities/
│   ├── concepts/
│   └── queries/
│
├── research/                 # 科研助手
│   ├── entities/
│   ├── concepts/
│   ├── comparisons/
│   └── queries/
│
├── teaching/                 # 教学助手
│   ├── entities/
│   ├── concepts/
│   └── queries/
│
├── raw/                      # 原始资料（不可变）
│   ├── articles/             #   网页、剪报
│   ├── papers/               #   PDF、arxiv 论文
│   ├── transcripts/          #   会议、访谈
│   └── assets/               #   图片、图表
│
└── _meta/                    # 元数据
    ├── topic-map.md          #   主题地图（破 200 页时建）
    ├── conflicts.md          #   待裁决矛盾
    └── archive/              #   归档页
```

## 🤖 三个 Agent 怎么协作

| Agent | 领域 | 可写位置 |
|---|---|---|
| **大总管** (OpenClaw main) | 日常事务、待办、人脉、会议 | `manager/`, `shared/` |
| **科研助手** (research-manager) | AI/ML 论文、研究方向、技术对比 | `research/`, `shared/` |
| **教学助手** (teaching-manager) | 课程、学生、知识点、教学方法 | `teaching/`, `shared/` |
| **老板 + 本地 agent** | 全部（git 合并）| 全部 |

**写入共享区 (shared/) 必须先标 `[proposed-by:<agent>]`，等老板确认** —— 防止 agent 互相覆盖。
详细边界规则见 [`SCHEMA.md`](./SCHEMA.md)。

## 📖 每页必须满足

- ✅ YAML frontmatter（10+ 字段，含 `agent:` 归属）
- ✅ Tag 必须从 SCHEMA.md 字典选（封闭词表，防 tag 爆炸）
- ✅ 至少 2 个 `[[wikilinks]]` 交叉引用
- ✅ 综合 3+ 来源的页面，段落末尾标 `^[raw/articles/source.md]` 溯源
- ✅ 修改必 bump `updated` 字段
- ✅ 新页必登 `index.md`
- ✅ 每次操作必追加 `log.md`

## 🚀 接入方式

### 1. 直接在 GitHub 上浏览
👉 https://github.com/zehonglin/obsidian-wiki

### 2. 本地 Clone
```bash
git clone git@github.com:zehonglin/obsidian-wiki.git ~/wiki-local
```

### 3. Obsidian 打开（推荐）
Obsidian → **Open vault as folder** → 选 `~/wiki-local/` 即可
- `[[wikilinks]]` 自动渲染
- Graph View 看知识图谱
- Dataview 跑 frontmatter 查询

### 4. 本地 Agent 接入（Claude Code / Codex / Work Buddy 等）
```bash
cd ~/wiki-local
# 直接启动 Claude Code / Codex，它会自动读 SCHEMA.md
claude     # 或 codex，或你喜欢的工具
```
本地 agent 会按 SCHEMA 规范自动：
- 写新页时填 frontmatter + tag + wikilinks
- 写完自动 commit + push（设好 hook）

### 5. 多设备同步（可选，付费）
用 **Obsidian Sync**：在云端 `~/wiki` 跑 `obsidian-headless sync --continuous`，
Obsidian 桌面/手机几秒内自动同步。

## 🔧 配套 Skill

本仓库依赖 [`llm-wiki`](https://github.com/NousResearch/hermes-agent/blob/main/skills/research/llm-wiki/SKILL.md) skill（v2.1.0）：

```
~/.openclaw/skills/llm-wiki/SKILL.md   # 在 openclaw agent 运行时
```

提供：
- Ingest / Query / Lint 三大操作流程
- 12 项 lint 健康检查（孤儿页、断链、stale 内容、矛盾页...）
- 规模化阈值（200 行/页、500 条日志、200 条索引）

## 📊 当前进度

**Last updated**: 2026-07-11

| 指标 | 值 |
|---|---|
| 总页数 | 7 |
| Raw 资料 | 5 |
| 研究方向覆盖 | T008（3D+VLA）5 篇论文 |
| 远端同步 | ✅ GitHub |

→ 详见 [`index.md`](./index.md) 和 [`log.md`](./log.md)。

## 🪜 Roadmap

- [ ] 大总管继续 ingest：另外 121 篇论文分批（每批 5-10）
- [ ] 科研助手接手后续研究页（不再由大总管代行）
- [ ] 教学助手首批：建课程 + 学生体系
- [ ] 老板本地 agent（Claude Code / Codex）配 git hooks 自动 commit
- [ ] 第一次 lint 全量健康检查

## 📜 哲学

> Karpathy 在他的 LLM Wiki gist 里写道：
>
> *"The wiki is a persistent, compounding artifact. The cross-references are already there.
> The contradictions have already been flagged. The synthesis already reflects everything
> you've read."*

我们不全采用 Hermes skill 的"严格规范"，也不全退回 Karpathy 的"自由协作"。
**卡中间**：用 schema 当骨架，让 agent 在上面自由长肉，遇到好模式再写进 schema。

## 📄 协议

- **License**：私有，Copyright © 2026 林泽洪
- **协作**：通过 git PR / direct push
- **争议**：`log.md` 标 `[needs-review]`
- **更新**：每次 commit 前 append log.md 一行

---

_本 README 由大总管 (OpenClaw main) 起草于 2026-07-11_
