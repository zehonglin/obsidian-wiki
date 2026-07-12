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

### 4. 本地 Coding Agent 接入（Claude Code / Codex / Work Buddy）
详见下面 [🛠️ Wiki 接入手册](#️-wiki-接入手册其他-agent-怎么认领) 路径 B。

### 5. 多人多设备同步（用 git 代替 Obsidian Sync）
这个 wiki 的同步**不靠** Obsidian Sync 付费服务，而是 **git = 同步**。
所有 agent（云端 + 老板本机）push 到 GitHub，互相 pull 即可。免费、可靠、完整历史。

---

## 🛠️ Wiki 接入手册（其他 Agent 怎么认领）

老板的 wiki 跑在 git 上，**任何能读 markdown + 会改文件的 agent** 都能用。
但要"识别 wiki"而不是"自己写自己的"，关键有 3 件套：

| 配件 | 作用 | 必需？ |
|---|---|---|
| **SKILL.md（llm-wiki）** | 让 agent 知道 wiki 模式 + 三大操作（Ingest/Query/Lint） | ⭐ 强烈推荐 |
| **SCHEMA.md** | wiki 的"宪法"，frontmatter / tag 字典 / agent 边界 | ✅ 必读 |
| **WIKI_PATH 环境变量** | 让 agent 知道 wiki 在哪 | ✅ 必设 |

### 路径 A：另一个 OpenClaw agent 接入（推荐）

比如你想让一个新装的「财务 agent」或「个人写作 agent」也来写 wiki：

**步骤 1：装 skill**（让它知道 wiki 模式）

```bash
# 默认就在 ~/.openclaw/skills/llm-wiki/
ls ~/.openclaw/skills/llm-wiki/SKILL.md

# 不存在就装：把 hermes-agent/skills/research/llm-wiki/SKILL.md
# 复制到 ~/.openclaw/skills/llm-wiki/SKILL.md
```

**步骤 2：告诉 agent wiki 在哪**（2 种方式选 1）

```bash
# 方式 1：环境变量（推荐，一次性配，所有 agent 都生效）
echo 'WIKI_PATH=/root/wiki' >> ~/.openclaw/.env

# 方式 2：在新 agent 的 SOUL.md / AGENTS.md 顶部加：
# "你管理的 wiki 位置：/root/wiki（读 SCHEMA.md 开始）"
```

**步骤 3：新 agent 首次启动时必读 3 项**（30 秒）

- `SCHEMA.md`（写入规则）
- `index.md`（现有内容）
- `log.md` 最后 30 行（最近动态）

**步骤 4：创建 agent 目录 + git config**

```bash
cd /root/wiki
git config user.name "新 Agent 名"
git config user.email "newagent@openclaw.local"
# 写完即可 git add + commit + push
```

**步骤 5：边界**

新 agent 可写自己专属目录 + shared/，**不要**写其他 agent 的目录

- 财务 agent：`finance/`, `shared/`
- 写作 agent：`writing/`, `shared/`
- 不能写：`research/` `teaching/` `manager/`（除非老板授权）

---

### 路径 B：本地 Coding Agent 接入（Claude Code / Codex / Work Buddy）

老板本机（Mac/Win）常用的 coding agent：

**步骤 1：clone 仓库**

```bash
git clone git@github.com:zehonglin/obsidian-wiki.git ~/wiki-local
```

**步骤 2：让它读 SCHEMA.md**

在对话里说：

> 「这是我的私人 wiki，规则全在 `~/wiki-local/SCHEMA.md`。
> 你帮我在这个目录里创建 XX 主题页面。」

Coding agent 会读 SCHEMA → 填 frontmatter → 写 wikilinks → 自动 commit。

**步骤 3（可选）：装 llm-wiki skill**

```bash
# Claude Code
mkdir -p ~/.claude/skills/llm-wiki
cp ~/.openclaw/skills/llm-wiki/SKILL.md ~/.claude/skills/llm-wiki/

# Codex 类似路径：~/.codex/skills/llm-wiki/
```

**步骤 4（可选）：git hooks 自动 push**

```bash
cd ~/wiki-local
cat > .git/hooks/post-commit << 'EOF'
#!/bin/bash
git push origin main
EOF
chmod +x .git/hooks/post-commit
```

---

### 路径 C：Obsidian 直接看 + 手动编辑（只读）

最简单，但**不推荐自动写**：

1. Clone 同路径 B 步骤 1
2. Obsidian → **Open vault as folder** → 选 `~/wiki-local/`
3. `[[wikilinks]]` 自动渲染，Graph View 看知识图谱
4. 手动改 frontmatter / 加页 → 用 Obsidian 插件（**git plugin**）自动 commit

适合**浏览 + 简单修改**，不适合大批量 ingest。

---

### 🧪 接入验证（接入后必跑）

新 agent 第一次对话，做这 3 个动作确认接入成功：

```bash
# 1. 能读到 schema（应有 20 个 tag 字典）
cat /root/wiki/SCHEMA.md | grep -c "tag:"

# 2. 能读到 index（应有 ≥6 个 H2 区段）
grep -c "^## " /root/wiki/index.md

# 3. git 通
echo "test" > /root/wiki/_meta/test-agent-接入.md
cd /root/wiki && git add . && git commit -m "test: agent 接入验证" && git push
```

3 步都成功 → 接入完成 → 可以正式工作。

---

### 📞 接入失败排查

| 现象 | 原因 | 修复 |
|---|---|---|
| Agent 不知道 wiki 在哪 | WIKI_PATH 未设 | 加环境变量 |
| Agent 不填 frontmatter | 没读 SCHEMA | 让 agent `read /root/wiki/SCHEMA.md` |
| Git push 失败 | SSH key 没配 | `ssh-add` + GitHub Settings 加 key |
| Agent 写到其他 agent 的目录 | 没讲边界 | 在 SOUL.md 加 "你只能写 X/, Y/" |
| Tag 不在字典 | 字典是封闭的 | 加新 tag 前先改 SCHEMA.md，等老板批 |
| commit 频繁失败 | API rate limit | 让 agent 增量 commit（小批次），失败由父 agent 收尾 |

---

### ❌ 不需要装的 4 件事

| ❌ 别这样 | ✅ 应该这样 |
|---|---|
| 装"wiki server" | 不需要，本地 markdown 即可 |
| 装数据库 / 向量库 | wiki 就是文件，**RAG 替代** |
| 装同步软件 | **git = 同步**，push 即可 |
| 给所有 agent 共享一个 skill 目录 | 各 agent 自己的 `~/.openclaw/skills/` 即可 |

---

## 🔧 配套 Skill（llm-wiki v2.1.0）

本仓库依赖 [`llm-wiki`](https://github.com/NousResearch/hermes-agent/blob/main/skills/research/llm-wiki/SKILL.md) skill（v2.1.0）：

```
~/.openclaw/skills/llm-wiki/SKILL.md   # OpenClaw agent 默认路径
```

提供：
- **Ingest / Query / Lint** 三大操作流程
- **12 项 lint 健康检查**（孤儿页、断链、stale 内容、矛盾页...）
- **规模化阈值**（200 行/页、500 条日志、200 条索引）

⚠️ **skill 是增强，不是必须**。没有 skill 也能用——只要 agent 会读 SCHEMA.md。
但装了 skill 后 agent 会自动调用三大操作，质量更稳。

**多 agent 共享 skill**：每个 agent 自己的 `~/.openclaw/skills/llm-wiki/` 路径即可，互不影响。

---

## 📊 当前进度

**Last updated**: 2026-07-12

| 指标 | 值 |
|---|---|
| 总页数 | 62（核心内容页） |
| Raw 资料 | 27（论文笔记 + 选题文档） |
| 选题覆盖 | T008 (5) + T009 (7) + T010 (3) + T011 (7) + T012 (7) + T013 (7) + T014 (8) |
| 跨域实体 | 4（老板 / 教研室 / 学院 / 学校） |
| 经理概念 | 2（AI 工作坊哲学 / 学期总结） |
| 远端同步 | ✅ GitHub |

→ 详见 [`index.md`](./index.md) 和 [`log.md`](./log.md)。

## 🪜 Roadmap

- [ ] 科研助手继续 ingest：剩余 ~63 篇候选（3D Spatial / RL 余篇 / Manipulation 余篇 / Pre-training / Humanoid）
- [ ] 教学助手首批：建课程 + 学生体系（教研室文档库 / 试卷题库 / 教材）
- [ ] 老板本机 agent（Claude Code / Codex）配 git hooks 自动 push
- [ ] 第一次 lint 全量健康检查（62 页量级）
- [ ] README 接入手册翻译给新人 agent 试用验证

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
