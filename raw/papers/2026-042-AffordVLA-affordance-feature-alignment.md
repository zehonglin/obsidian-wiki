# AffordVLA: Injecting Affordance Representations into Vision-Language-Action Models via Implicit Feature Alignment
- 作者：Weijie Kong, Zhian Su, Wei Yu, Huixu Dong (浙江大学 Grasp Lab)
- 来源：arXiv
- 日期：2026-05-23
- arxivId：2605.17517
- URL：https://arxiv.org/abs/2605.17517
- 相关选题：T008（3D视觉+VLA）、T009（VLA安全性）
- 相关度：0.93

## 研究背景
现有VLA模型的视觉表征被全局物体外观主导，难以聚焦任务相关的功能交互区域，在非结构化环境中鲁棒性不足。现有可供性方法依赖显式mask注入或外部感知模块，需要额外标注且引入级联感知误差。

## 核心方法
AffordVLA通过隐式表征对齐将操作可供性感知内化到VLA视觉表征中：
1. **零样本可供性教师**：从RGB观察和语言指令提取任务条件的可供性视觉表征
2. **隐式表征对齐**：训练时将VLA中间视觉表征与教师提取的可供性表征对齐
3. **推理零开销**：推理时移除教师模块，不增加额外推理开销

关键创新：仅使用现有机器人演示数据训练，无需额外可供性标注。

## 实验结果
- RoboTwin基准：Easy设置超越最佳基线20.5%，Hard设置超越12.8%
- 真实世界实验验证在非结构化场景中的精确操作能力
- 消融分析表明AffordVLA有效重塑VLA视觉表征
- 训练效率提升，数据效率更高

## 局限性
- 零样本教师的可供性表征质量受限于教师模型能力
- 仅在RoboTwin和有限真实场景验证
- 隐式对齐可能损失部分语义表征能力

## 与选题关联
- **T008（3D视觉+VLA）**：可供性感知与3D空间理解互补，可结合深度信息增强功能区域定位
- **T009（VLA安全性）**：聚焦功能交互区域可减少非结构化环境中的误操作

## 关键引用
- OpenVLA, π0 - VLA基线
- Affordance learning经典工作
- RoboTwin benchmark
