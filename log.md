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

### [2026-07-11 23:30] ingest | First batch: 5 papers on T008 (3D+VLA) | research
来源：`/root/.openclaw/agents/research-manager/workspace/literature/papers/` 中 5 篇代表性论文
- 2026-001-3D-Mix（VGGT 融合 + 即插即用）
- 2025-002-OG-VLA（正交视图 + 视角不变性）
- 2026-013-World2VLM（世界模型蒸馏 VLM）
- 2026-018-STARRY（时空扩散 + GASAM）
- 2026-019-RISE（组合世界模型 + 想象空间自改进）

新建 wiki 页（7 个）：
- research/entities/paper-2026-001-3d-mix.md
- research/entities/paper-2025-002-og-vla.md
- research/entities/paper-2026-013-world2vlm.md
- research/entities/paper-2026-018-starry.md
- research/entities/paper-2026-019-rise.md
- research/concepts/concept-t008-3d-vla.md（选题总览）
- research/concepts/concept-world-model-distillation.md（跨论文概念）

复制 raw 文件：
- raw/papers/2026-001-3D-Mix.md, 2025-002-OG-VLA.md, 2026-013-World2VLM.md, 2026-018-STARRY.md, 2026-019-RISE.md

更新：index.md（research 分区填入 7 条）

大总管代行（老板指令）。下次科研 ingest 应转交科研助手。

### [2026-07-11 23:30] update | SCHEMA.md: note first batch exception | shared

### [2026-07-11 23:39] update | README.md created | main
- 添加仓库顶层 README.md（仓库介绍、目录、agent 边界、接入方式）
- 远端推送（SSH 走顺，14KB）

### [2026-07-12 11:35] ingest | First priority: 5 cross-domain entity/concept pages | manager
来源：老板指令"按优先级，先做第一个"
- 大总管盘点三个 agent 历史内容后报告，老板挑了高价值低风险的第一批

新建 5 个 wiki 页：

**shared/entities/**（跨域通用，标 `[proposed-by:main]`）：
- [[prof-lin-zehong]] — 老板本人
- [[ai-research-teaching-section]] — 人工智能教研室
- [[electronics-info-college]] — 电子信息学院
- [[lishui-vocational-tech-college]] — 丽水职业技术学院

**manager/concepts/**（大总管主理）：
- [[concept-ai-innovation-workshop-philosophy]] — Neural Bloom 设计哲学
- [[concept-semester-summary-2025-2026-2]] — 2025-2026-2 学期工作小结

更新：index.md（manager/concepts 和 shared/entities 各新增条目）

总页数从 7 增至 12。

**[proposed-by:main]** 因为包含教研室和学校这种跨域实体，按 SCHEMA 规范标 proposed。

### [2026-07-12 12:25] ingest | Second batch: 5 papers + 2 concept pages | research
来源：老板指令"开始第二个"——高价值低风险组的第二优先：126 篇论文中首批 5 篇 + 配套 2 个概念页

**[proposed-by:main]**（科研助手暂未自取，先按 SCHEMA 标 proposed，等科研助手接手后续批）

**5 个 paper entity**（research/entities/）：
- [[paper-2026-014-llm-safety-robot-care]] — LLM 在机器人护理场景安全评测（T009）
- [[paper-2026-020-world-env]] — World-Env 用世界模型做 VLA RL 后训练（T010，5 demo）
- [[paper-2026-021-motubrain]] — MotuBrain 统一世界动作模型（T008/T009/T010）
- [[paper-2026-022-wam-survey]] — WAM 综述 200+ 论文统分六大支柱
- [[paper-2026-060-memorywam]] — MemoryWAM 带持久记忆的高效 WAM（T008/T010）

**2 个 concept**（research/concepts/）：
- [[concept-t009-safety-robustness]] — VLA 安全与鲁棒性选题
- [[concept-t010-data-efficiency]] — VLA 数据效率与少样本适配选题

**raw sources 同步**：
- raw/papers/ 新增 5 份论文笔记
- raw/files-from-research-workspace/literature/directions/vla/ 新增 2 份选题文档

**index.md 更新**：research/entities +5、research/concepts +2，总页数 12→19

**选题覆盖进展**：
- T008（3D+VLA）：5 篇 → 还是 5 篇（之前首批）
- T009（VLA 安全）：0 篇 → 1 篇 + 1 concept
- T010（数据效率）：0 篇 → 3 篇（World-Env, MotuBrain, MemoryWAM）+ 1 concept

**待续**：剩下 109 篇论文分布：
- 3D/Spatial：13 篇剩余
- World Models：13 篇剩余
- RL Training：12 篇剩余
- Safety & Benchmarks：7 篇剩余
- Manipulation/Dexterous：8 篇
- ...

按 wiki roadmap 应转交科研助手自取，但老板直接指令可走"大总管代行"模式。
