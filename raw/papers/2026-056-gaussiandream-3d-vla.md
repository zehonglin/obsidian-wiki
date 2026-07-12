# GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation
- 作者：Haibao Yu 等
- 来源：arXiv (cs.RO)
- 日期：2026-05-20 (v2)
- arxivId：2605.20752
- URL：https://arxiv.org/abs/2605.20752
- 相关选题：T008
- 相关度：0.90

## 研究背景
VLA策略通过从预训练VLM迁移语义先验来生成动作，但标准动作模仿学习缺乏对显式3D空间信息、密集几何监督和未来环境演化的建模，这些都是精确机器人交互的关键要素。

## 核心方法
GaussianDream提出前馈式3D高斯世界模型插件：
1. **GaussianDream Queries**：在编码器中引入可学习的前缀查询，捕获当前帧3D空间结构和短期未来演化
2. **双头训练**：静态重建头（当前3D高斯场景状态）+ 未来预测头（未来高斯演化状态），分别用RGB渲染+深度和未来RGB+深度+伪3D场景流监督
3. **推理时轻量**：丢弃所有辅助头，仅保留学习到的前缀来条件化动作生成，无需测试时高斯重建或未来预测

## 实验结果
- LIBERO: 98.4% (SOTA)
- RoboCasa Human-50: 54.8%
- 真实机器人: 50.0%
- 相比其他3D增强VLA方法：精度强+推理效率高于视频世界模型方法

## 局限性
- 训练时需要深度信息辅助监督
- 短期未来预测范围有限
- 3D高斯表示在大规模场景的内存开销

## 与选题关联
- **T008（3D视觉+VLA）**：GaussianDream是3D信息融入VLA的代表性工作。其"前缀查询"设计无需推理时额外计算，是高效3D增强方案。LIBERO 98.4%的SOTA成绩证明了3D空间建模对操作性能的关键作用。
- 核心创新：将3D高斯表示作为VLA的内部中间表示，而非外部输入模态，这种设计哲学值得借鉴。

## 关键引用
- 3D Gaussian Splatting
- World Models for robotics
- LIBERO benchmark
