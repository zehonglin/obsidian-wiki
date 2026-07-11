# Wiki Log

> 时间线，append-only。所有 wiki 动作的审计记录。
> 格式：`## [YYYY-MM-DD HH:MM] action | subject | agent`
> actions: create, ingest, update, query, lint, archive, delete, config
> agent: manager, research, teaching, shared, local
> 当文件超过 500 条时按年轮转：`log-YYYY.md`

---

## [2026-07-11 23:08] create | Wiki initialized | shared

- Domain: manager + research + teaching（三 agent 协作）
- 注册 skill: llm-wiki v2.1.0（来自 NousResearch/hermes-agent）
- 落点：`/root/.openclaw/skills/llm-wiki/SKILL.md`
- 建目录：`shared/{entities,concepts,comparisons,queries}`、`manager/*`、`research/*`、`teaching/*`、`raw/*`、`_meta/`
- 写 SCHEMA.md（含 agent 边界表 + 20 个 tag 字典 + frontmatter 规范）
- 写 index.md（按 agent 分区）
- 写 log.md（本条）
- 操作员：大总管（main）

### [2026-07-11 23:08] config | agent boundaries defined | shared
- 大总管 → manager/, shared/
- 科研助手 → research/, shared/
- 教学助手 → teaching/, shared/
- 写入 shared/ 必须 [proposed-by]

### [2026-07-11 23:08] config | tag dictionary v1 | shared
- 20 个核心 tag（模型/多模态/学习/评测/实体/元数据）
- 新 tag 流程：先登记到 SCHEMA.md，再用

### [2026-07-11 23:08] pending | git push to GitHub | main
- 远端：https://github.com/zehonglin/obsidian-wiki.git
- 状态：等老板提供 GitHub PAT 或 SSH key
- 已完成本地：`git init` + `git add` + `git commit`

### [2026-07-11 23:08] planned | first batch ingest | research
- 数据源：`/root/.openclaw/agents/research-manager/workspace/literature/papers/*.md`（126 篇）
- 试点：选 5-10 篇代表性论文作为样板
- 计划写入位置：research/concepts/（方法）、research/entities/（论文/模型）、research/comparisons/
- 等老板确认推送凭证后执行

### [2026-07-11 23:21] config | git push succeeded | main
- 远端：https://github.com/zehonglin/obsidian-wiki
- 提交 SHA: e8b98bc
- 4 文件：.gitignore, SCHEMA.md, index.md, log.md
- 凭证：老板提供了 GitHub PAT，token 已使用并清掉本地痕迹
- 网络：云端到 github.com 不稳定（前面 2 次 push 超时失败，第 3 次才通）
