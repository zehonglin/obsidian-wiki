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

---

## 2026-07-12 batch 7 — T014 World Models（8 篇 + 1 concept）

**选题**：T014（世界模型）—— 核心方法论选题，贯穿 VLA 所有维度

**论文**（8 篇）：
- [[paper-2024-001-3d-vla]] — 3D-VLA：3D 视觉-语言-动作生成式世界模型开山之作（2403.09631，T008/T014）
- [[paper-2026-057-rynnvla002-unified-vla-wm]] — RynnVLA-002：统一 VLA 与世界模型双向增强（LIBERO 97.4%，LeRobot +50%）
- [[paper-2026-071-icwm-in-context-world-model]] — ICWM：上下文世界建模，零微调跨环境适配
- [[paper-2026-077-regen-wam-continual-imitation]] — REGEN：WAM 生成式回放持续学习（遗忘↓50%）
- [[paper-2026-101-vt-wam-visual-tactile]] — VT-WAM：视觉-触觉世界动作模型（contact-rich 71.67%）
- [[paper-2026-108-rynnworld-4d]] — RynnWorld-4D：4D 具身世界模型（RGB+深度+光流，2.544 亿帧）
- [[paper-2026-056-gaussiandream-3d-vla]] — GaussianDream：前馈式 3D 高斯世界模型插件（LIBERO 98.4% SOTA）
- [[paper-2026-107-bridge-wa]] — Bridge-WA：世界模型知识蒸馏（位置+变化+语义三先验，OOD 泛化）

新建 1 个 concept（research/concepts/）：
- [[concept-t014-wm]] — T014 选题总览：世界模型四条技术路线（生成式→统一训练→蒸馏→新范式）

raw sources 同步：
- raw/papers/ 新增 8 份论文笔记

index.md 更新：research/entities +8、research/concepts +1，总页数 49→58

**四条技术路线**：
1. **生成式世界模型**：3D-VLA → GaussianDream → RynnWorld-4D（从点云到高斯到 4D）
2. **VLA × WM 统一训练**：RynnVLA-002（双向增强）↔ MotuBrain/MemoryWAM
3. **世界模型知识蒸馏**：World2VLM → Bridge-WA → GaussianDream（推理零开销）
4. **WM 驱动新范式**：REGEN（持续学习）、ICWM（跨环境适配）、VT-WAM（触觉 WAM）

**与已有 WAM 论文的知识图谱**：
- WAM Survey 为顶层地图，MotuBrain 为统一基线
- VT-WAM = MotuBrain + 触觉；MemoryWAM = MotuBrain + 记忆；REGEN = MotuBrain + 生成回放
- Bridge-WA = World2VLM 的 VLA 版本（空间蒸馏 → 变化蒸馏）
- GaussianDream 与 RynnWorld-4D 为 3D 世界模型两条路线（高斯 vs RGB-DF）

选题覆盖进展：
- T008（3D+VLA）：5 篇（不变，GaussianDream/RynnWorld-4D/3D-VLA 为 cross-link）
- T009（VLA 安全）：7 篇（不变）
- T010（数据效率）：3 篇（不变，多批 WM 论文挂 T010 cross-link）
- T011（操作/灵巧）：7 篇（不变，VT-WAM 为 cross-link）
- T012（RL Training）：7 篇（不变，WorldSample 为 cross-link）
- T013（Navigation）：7 篇（不变）
- **T014（World Models）：0 篇 → 8 篇 + 1 concept**（新建选题，含跨批次 16 篇 WM 相关）

研究空白识别：
1. 世界模型 × 导航（WM 集中在操作，导航场景空白）
2. 多本体世界模型（不同机器人共享一个 WM 未验证）
3. 长时程预测质量（REGEN 揭示 horizon 增加时退化）
4. 触觉/力/声音等多模态世界模型扩展
5. 世界模型 + RL 闭环的 sim-to-real gap

操作员：科研助手 (research-manager)

### [2026-07-12 15:54] ingest | Batch 8: VLA Survey/Review 横向收束 — 4 papers + 1 concept update | research
来源：老板指令"继续科研助手"

4 个 paper entity（research/entities/）：
- [[paper-2026-125-vla-survey-embodied-ai]] — VLA 学术综述：IEEE TNNLS，三研究路线分类法（T008-T014 全覆盖）
- [[paper-2026-126-vla-review-realworld]] — VLA 部署综述：IEEE Access，实际应用六维度
- [[paper-2026-127-vla-survey-manipulation]] — VLA 操作综述：中文，arXiv 2508.15201，五维度框架
- [[paper-2026-128-embodied-ai-sae]] — Embodied AI 行业白皮书：SAE World Congress 2026

更新 1 个 concept：
- [[concept-t008-3d-vla]] — 新增「相关综述」区段（4 篇综述交叉引用）

⚠️ 子 agent 在 commit 阶段因 API rate limit 失败，由大总管手动 commit 收尾。

操作员：科研助手（失败）→ 大总管代行 commit

### [2026-07-12 16:05] lint | 全量健康检查 — 5 类问题修复完毕 | main
来源：老板指令「跑一次 lint 全量健康检查」(7-12 16:00)

跑通 12 项检查（基于 llm-wiki skill v2.1.0 Lint 规范）：

**修复 5 类问题：**
1. **Orphans (2)** — manager/concepts/ 两个页面无 inbound
   → 重命名为 concept-* 前缀（与 SCHEMA 约定一致）
2. **Broken wikilinks (28 → 0)** — 4 个 typo + 10 个 forward ref + 14 个 template false positives
   → typo 修复、forward ref 转为 TODO、template 排除
3. **Missing from index (2)** — 新创建 stub 概念页
   → 补入 index.md
4. **Contradictions (1 false positive)** — SCHEMA.md frontmatter 示例
   → lint 脚本排除 schema 文档
5. **Low confidence (12 → 0 排除 stub)** — 业务上合理（level 1 摘要级笔记）

**新增文件：**
- `_meta/lint-check.py` — 12 项健康检查脚本（可复用）
- `research/concepts/concept-vla-model.md` — VLA 总览 stub
- `research/concepts/concept-world-model-for-robotics.md` — WM in Robotics stub

**最终结果：🎉 12 项检查全部通过**

| 指标 | 修复前 | 修复后 |
|---|---|---|
| Pages | 67 | 69 |
| Wikilinks | 530 | 537 |
| Orphans | 2 | 0 |
| Broken links | 28 | 0 |
| Missing from index | 2 | 0 |
| Frontmatter issues | 0 | 0 |
| Stale (>90d) | 0 | 0 |
| Contradictions | 1 | 0 |
| Low confidence | 12 | 0 (排除 stub) |
| Oversize pages | 2 (README/log) | 0 (排除允许长文档) |
| Unknown tags | 0 | 0 |

未来 lint 触发方式：
- 老板手动：`bash /root/.openclaw/workspace/wiki-lint.sh`
- 或在 cron 中每月自动跑一次
- 或新 batch 完成后自动跑（建议加 git hook）

### [2026-07-12 17:44] ingest | Batch 9: 闭环 forward refs — 6 papers + TODO recovery | research
来源：lint 检查发现的 10 个 forward ref TODO，本批全部闭环

新建 6 个 paper entity：
- [[paper-2026-079-abc-scalable-behavior-cloning]] — ABC 全开源 BC 工具栈（ABC-130K，3500h，195 任务，T010）
- [[paper-2026-104-qwen-robotmanip-alignment]] — Qwen-RobotManip 三维对齐+38K小时预训练（跨15平台 SOTA，T008/T010）
- [[paper-2026-083-relafford6d]] — RelAfford6D 关系6D可供性图（训练无关，T008/T011）
- [[paper-2026-094-bpp-behavior-prompting]] — BPP 单次演示 behavior prompting（任务多样性>数据量，T010）
- [[paper-2026-050-qwen-vla]] — Qwen-VLA 统一操作+导航 VLA 基础模型（LIBERO 97.9%，T008/T009/T010）
- [[paper-2026-115-internvla-a15]] — InternVLA-A1.5 潜在前瞻+统一专家（6基准最佳，T008/T010/T014）

闭环动作：5 个引用页面的 TODO → wikilink 还原（共 +11 wikilinks）
- paper-2026-126: +1 wikilink（abc → [[paper-2026-079-abc-scalable-behavior-cloning]]）✅ 闭环 +1
- paper-2026-127: +4 wikilinks（qwen-vla, internvla-a15, abc, qwen-robotmanip）✅ 闭环 +4
- paper-2026-128: +2 wikilinks（abc, qwen-robotmanip）✅ 闭环 +2
- paper-2026-042: +1 wikilink（relafford6d → [[paper-2026-083-relafford6d]]）✅ 闭环 +1
- paper-2026-100: +1 wikilink（bpp → [[paper-2026-094-bpp-behavior-prompting]]）✅ 闭环 +1
- paper-2026-014: 1 处「未来待 ingest」为表格注释，非 forward ref，保留

增量 commit 策略（3 步抗中断）：
1. commit 1/3: papers 079, 104, 083 — SHA 2a6eeb0
2. commit 2/3: papers 094, 050, 115 — SHA 3d5d40a
3. commit 3/3: TODO 还原 + index/log 更新

操作员：科研助手（research-manager subagent）

### [2026-07-12 18:00] ingest | Batch 10: T008 主线补强 — 7 papers + concept 路线分类表 | research
来源：老板指令「继续科研助手下一批」——T008 主线补强（3D/Spatial Perception）

新建 7 个 paper entity（T008 主线）：
- [[paper-2025-001-graphcot-vla]] — 3D Pose-Object 图 + CoT 处理模糊指令（2025 早期代表，arXiv 2508.07650）
- [[paper-2026-002-gst-vla]] — 高斯空间 Token + DA-CoT 显式空间推理（LIBERO 96.4%，arXiv 2603.09079）
- [[paper-2026-017-rag-vlm-spatial]] — RAG 增强 VLM 空间感知（Science Robotics，DOI 10.1126/scirobotics.aea2092）
- [[paper-2026-030-multiview-vla]] — 多视角扩散先验 + 动作流形学习（arXiv 2605.11832）
- [[paper-2026-034-evo-depth]] — 0.9B 轻量隐式深度增强 VLA（arXiv 2605.14950）
- [[paper-2026-039-esi-bench]] — 具身空间智能评测基准（Li Fei-Fei 团队，arXiv 2605.18746）
- [[paper-2026-055-stereopolicy-3d-vla]] — 立体视觉 3D 操作策略（arXiv 2605.09989）

更新 1 个 concept：
- [[concept-t008-3d-vla]] — 新增「T008 论文技术路线分类」表格（8+ 路线，路线间关系图，关键洞察），从 3 路线 → 8+ 路线覆盖

增量 commit 策略（3 步抗中断）：
1. commit 1/3: papers 2025-001, 2026-002, 2026-017 + raw — 前三篇三星
2. commit 2/3: papers 2026-030, 2026-034, 2026-039, 2026-055 + raw — 后四篇两星
3. commit 3/3: concept-t008 + index + log — 元数据更新

操作员：科研助手（research-manager subagent）
