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

### [2026-07-12 12:27] ingest | Batch 3: VLA Safety & Robustness — 6 papers + 1 concept update | research
来源：`/root/.openclaw/agents/research-manager/workspace/literature/papers/` 中 T009（VLA 安全）方向的 6 篇代表性论文

**科研助手首次自取**（前两批由大总管代行）

主题：**VLA Safety & Robustness (T009)** — 从攻击、防御、运行时、评测四个维度构建 VLA 安全研究全景

新建 6 个 paper entity（research/entities/）：
- [[paper-2026-005-vla-fool]] — 多模态对抗攻击（文本+视觉+跨模态，失败率>93%）
- [[paper-2026-040-rovla]] — 多一致性约束鲁棒性训练（IC+EC+OC）
- [[paper-2026-046-pre-vla]] — 先发式运行时动作验证（+6.83pp）
- [[paper-2026-063-libero-safety]] — 物理+语义安全综合基准（ECCV 2026）
- [[paper-2026-080-foresight-safety-vla]] — 诊断级安全基准（13 类，过程级度量）
- [[paper-2026-096-oopsieverse]] — 物理损伤感知仿真基准（RSS 2026）

更新 1 个 concept（research/concepts/）：
- [[concept-t009-safety-robustness]] — 新增「安全研究三维框架」（攻击-防御-评测），6 篇论文 cross-reference

raw sources 同步：
- raw/papers/ 新增 6 份论文笔记

index.md 更新：research/entities +6，总页数 19→25

选题覆盖进展：
- T008（3D+VLA）：5 篇（不变）
- T009（VLA 安全）：1 篇 → **7 篇**（+6，含 2 个 ECCV/RSS 顶会基准）
- T010（数据效率）：3 篇（不变）

操作员：科研助手 (research-manager)

### [2026-07-12 12:54] ingest | Batch 4: Manipulation / Dexterous — 7 papers + 1 concept | research
来源：`/root/.openclaw/agents/research-manager/workspace/literature/papers/` 中 Manipulation/Dexterous 方向的 7 篇代表性论文

**科研助手第二次自取**（batch 3 后继续）

主题：**Manipulation / Dexterous (T011)** — 从灵巧控制、双臂协调、可供性、长时程操作、评测基准五个维度构建操作研究全景

新建 7 个 paper entity（research/entities/）：
- [[paper-2026-033-handitl]] — 人机协同灵巧修正（抖动↓99.8%）
- [[paper-2026-038-dexora]] — 36-DoF 双臂灵巧开源 VLA（ICRA 2026）
- [[paper-2026-053-bora]] — 灵巧 VLA 离线-在线 RL 后训练（成功率+33%）
- [[paper-2026-042-affordvla]] — 隐式可供性对齐增强操作（+20.5%）
- [[paper-2026-106-cortex]] — 长时程操作双向对齐框架（32 技能原语）
- [[paper-2026-110-furniturevla]] — 双臂家具组装 1550 步长时程
- [[paper-2026-122-dexverse]] — 100 任务灵巧操作模块化基准（3 臂 6 手）

新建 1 个 concept（research/concepts/）：
- [[concept-t011-manipulation]] — T011 选题总览：5 维度技术路线收敛

raw sources 同步：
- raw/papers/ 新增 7 份论文笔记

index.md 更新：research/entities +7、research/concepts +1，总页数 25→33

选题覆盖进展：
- T008（3D+VLA）：5 篇（不变）
- T009（VLA 安全）：7 篇（不变）
- T010（数据效率）：3 篇（不变）
- **T011（操作/灵巧）：0 篇 → 7 篇**（新建选题，含 1 ICRA 顶会 + 1 大规模基准）

研究空白识别：
1. 高 DoF + 长时程交叉（>500 步灵巧操作几乎空白）
2. 力反馈与 VLA 融合（本批论文均无触觉/力反馈）
3. Deformable 物体操作（柔性物体操作缺失）
4. 跨本体灵巧迁移（Dexora 验证可行性，DexVerse 揭示泛化仍困难）

操作员：科研助手 (research-manager)

### [2026-07-12 15:30] ingest | Batch 5: RL Training — 7 papers + 1 concept | research
来源：`/root/.openclaw/agents/research-manager/workspace/literature/papers/` 中 RL Training 方向的 7 篇代表性论文

**科研助手第三次自取**（batch 4 后继续）

主题：**RL Training (T012)** — 从策略优化、训练稳定化、架构特定目标、奖励建模、语义 RL、世界模型增强六个维度构建 VLA RL 训练全景

新建 7 个 paper entity（research/entities/）：
- [[paper-2026-097-z1]] — 基于 π₀.₅ 的 GRPO RL 后训练（RoboCasa 80.6%，+13.2pp）
- [[paper-2026-072-force]] — VLA RL 微调三阶段框架（+79%，防灾难性遗忘）
- [[paper-2026-067-dvla-rl]] — 离散扩散 VLA 的轨迹级 RL（LIBERO 99.7%）
- [[paper-2026-087-warp-rm]] — 自监督时间扭曲进度奖励模型（数据差时维持 19/20）
- [[paper-2026-100-sarl]] — 语义空间 RL（优化语言提示而非动作）
- [[paper-2026-103-worldsample]] — 世界模型增强真实机器人 RL（+28%，步数-59%）
- [[paper-2026-088-ppo-eal]] — 精确增广拉格朗日 PPO 安全控制（T009×T012 交叉）

新建 1 个 concept（research/concepts/）：
- [[concept-t012-rl-training]] — T012 选题总览：6 条技术路线收敛

raw sources 同步：
- raw/papers/ 新增 7 份论文笔记

index.md 更新：research/entities +7、research/concepts +1，总页数 33→41

选题覆盖进展：
- T008（3D+VLA）：5 篇（不变）
- T009（VLA 安全）：7 篇（不变，PPO-EAL 为 T009×T012 交叉）
- T010（数据效率）：3 篇（不变，多批 RL 论文挂 T010 cross-link）
- T011（操作/灵巧）：7 篇（不变）
- **T012（RL Training）：0 篇 → 7 篇**（新建选题，含 LIBERO 99.7% SOTA）

研究空白识别：
1. 真实世界 RL 迁移（大部分仅仿真验证）
2. 长时程任务信用分配（>500 步 RL 未验证）
3. RL + 多本体迁移（空白）
4. 奖励鲁棒性（adversarial 场景未测）

操作员：科研助手 (research-manager)

---

## 2026-07-12 batch 6 — T013 Navigation / Locomotion（7 篇 + 1 concept）

**选题**：T013（导航与运动）—— 首次建立，聚焦机器人空间移动能力

**论文**（7 篇）：
- [[paper-2026-006-metanav]] — MetaNav：元认知推理导航（GOAT-Bench/HM3D-OVON/A-EQA SOTA，-20.7% VLM 查询）
- [[paper-2026-052-uni-lavira]] — Uni-LaViRA：零训练三层 Agent 跨 4 类机器人（HM3D 77.7% SR）
- [[paper-2026-073-moe-rl-fault-tolerant]] — MoE-RL：故障容忍腿足运动（MoE 路由 + RL）
- [[paper-2026-090-cwi-humanoid-locomanipulation]] — CWI：人形全身解耦模仿（MoCap 上身 + AMP 下身）
- [[paper-2026-091-booster-lab]] — Booster Lab：data-centric 人形运动 pipeline（T1/K1 验证）
- [[paper-2026-093-vlk]] — VLK：3DGS 合成 48K 轨迹学 loco-manipulation（Unitree G1）
- [[paper-2026-095-human-as-humanoid]] — Human-as-Humanoid：人类视频→IK→60-DoF 人形（4.8-7.2× 遥操作）

新建 1 个 concept（research/concepts/）：
- [[concept-t013-navigation]] — T013 选题总览：3 条技术路线（零训练→合成数据→RL+模块化）

raw sources 同步：
- raw/papers/ 新增 7 份论文笔记

index.md 更新：research/entities +7、research/concepts +1，总页数 41→49

选题覆盖进展：
- T008（3D+VLA）：5 篇（不变）
- T009（VLA 安全）：7 篇（不变）
- T010（数据效率）：3 篇（不变，Booster Lab/Human-as-Humanoid/VLK 为 cross-link）
- T011（操作/灵巧）：7 篇（不变，CWI/Human-as-Humanoid 为 cross-link）
- T012（RL Training）：7 篇（不变，MoE-RL 为 cross-link）
- **T013（Navigation / Locomotion）：0 篇 → 7 篇**（新建选题）

三条技术路线：
1. **零训练导航**：MetaNav（元认知）+ Uni-LaViRA（架构解耦）—— 导航动作在 MLLM 流形内
2. **合成/转换数据**：VLK（3DGS 合成）+ Human-as-Humanoid（人类视频转换）—— 绕过遥操作瓶颈
3. **RL + 模块化**：MoE-RL（故障路由）+ CWI（解耦策略）+ Booster Lab（data-centric RL）

研究空白识别：
1. 导航 × 操作深度耦合（行进中操作未解决）
2. 室内→户外跨域迁移验证空白
3. 多机器人协作导航未涉及
4. 长期导航（>1h）安全退化未研究

操作员：科研助手 (research-manager)
