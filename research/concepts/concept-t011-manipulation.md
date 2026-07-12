---
title: "T011 选题：操作与灵巧操作 (Manipulation / Dexterous)"
created: 2026-07-12
updated: 2026-07-12
type: concept
agent: research
domain: ai-research
visibility: shared
tags: [manipulation, vla, survey]
sources:
  - raw/papers/2026-033-HandITL-dexterous-VLA.md
  - raw/papers/2026-038-Dexora-bimanual-dexterous-VLA.md
  - raw/papers/2026-053-bora-vla-dex-rl.md
  - raw/papers/2026-042-AffordVLA-affordance-feature-alignment.md
  - raw/papers/2026-106-cortex-long-horizon-vla.md
  - raw/papers/2026-110-furniturevla.md
  - raw/papers/2026-122-dexverse-benchmark.md
confidence: high
---

# T011：操作与灵巧操作

> VLA 模型在机器人操作领域的纵深方向：从抓取到灵巧控制，从短时程到长时程，从单一本体到跨本体迁移。

## 选题定位

T011 聚焦 VLA 在**物理操作**层面的核心挑战，区别于 T008（3D 感知）、T009（安全鲁棒）、T010（数据效率），本选题关注操作能力的**广度与深度**：

| 维度 | 子方向 | 代表论文 |
|---|---|---|
| **灵巧操作** | 高 DoF 手部控制、gesture jump 修正 | [[paper-2026-033-handitl]], [[paper-2026-053-bora]] |
| **双臂协调** | 双臂协同、双手系统 | [[paper-2026-038-dexora]], [[paper-2026-110-furniturevla]] |
| **可供性与抓取** | 功能区域定位、隐式对齐 | [[paper-2026-042-affordvla]] |
| **长时程操作** | 多步骤任务、技能原语、进度估计 | [[paper-2026-106-cortex]], [[paper-2026-110-furniturevla]] |
| **评测基准** | 多任务多本体测试 | [[paper-2026-122-dexverse]] |

## 技术路线收敛

### 路线 1：灵巧控制 → 从数据到部署

```
数据采集（遥操作/仿真）
  → 质量感知训练（Dexora）
  → 人机协同修正（HandITL）
  → RL 后训练（BORA）
  → 部署
```

三篇论文形成完整的灵巧操作流水线：Dexora 解决数据规模与质量，HandITL 解决在线修正，BORA 解决 RL 后训练可靠性。

### 路线 2：长时程操作 → 分层 vs 进度

两种范式并存：
- **技能原语分层**（Cortex）：32 个标准技能 + VLM 规划 + VLA 执行
- **进度自动切换**（FurnitureVLA）：进度估计模块驱动子任务切换

两种方案各有优劣：技能原语更灵活但需预定义；进度估计更自动但依赖训练数据。

### 路线 3：可供性感知 → 空间智能互补

AffordVLA 的隐式对齐让 VLA "知道看哪里"，与 [[concept-t008-3d-vla]] 的 3D 几何感知互补——一个提供"功能认知"，一个提供"几何认知"。

## 与其他选题的关系

- **T008（3D+VLA）**：AffordVLA 的可供性 + 3D-Mix 的几何 = 完整空间感知
- **T009（安全）**：BORA 的冻结基座 + 残差适配是一种安全策略；HandITL 的干预修正与 Pre-VLA 的运行时验证呼应
- **T010（数据效率）**：Dexora 的质量感知训练、Cortex 的 4k+ 小时自动标注、DexVerse 的 3,180 条多本体数据，都直接服务数据效率

## 研究空白

1. **高 DoF + 长时程交叉**：现有灵巧操作论文（HandITL, BORA）任务时程较短，长时程灵巧操作（>500 步）几乎空白
2. **力反馈与 VLA 融合**：本批论文均无触觉/力反馈集成，接触丰富操作可能需要
3. **Deformable 物体操作**：柔性物体（布料、绳索）操作在本批论文中缺失
4. **跨本体灵巧迁移**：Dexora 验证跨本体可行性，但 DexVerse 揭示泛化仍困难

## 本批论文总览（7 篇）

| ID | 论文 | 核心贡献 | 交叉选题 |
|---|---|---|---|
| 033 | [[paper-2026-033-handitl]] | 人机协同灵巧修正（抖动 ↓99.8%） | T009 |
| 038 | [[paper-2026-038-dexora]] | 36-DoF 双臂开源 VLA（ICRA 2026） | T010 |
| 053 | [[paper-2026-053-bora]] | 灵巧 RL 后训练（成功率 +33%） | T009, T010 |
| 042 | [[paper-2026-042-affordvla]] | 隐式可供性对齐（+20.5%） | T008 |
| 106 | [[paper-2026-106-cortex]] | 长时程双向对齐（32 技能原语） | T010 |
| 110 | [[paper-2026-110-furniturevla]] | 双臂家具组装（1550 步） | — |
| 122 | [[paper-2026-122-dexverse]] | 100 任务灵巧基准（3 臂 6 手） | T010 |
