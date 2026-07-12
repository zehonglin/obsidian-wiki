# Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model
- 作者：Tao Lin, Yuxin Du, Jiting Liu, Nuobei Zhu et al.
- 来源：arXiv
- 日期：2026-05-14
- arxivId：2605.14950
- URL：https://arxiv.org/abs/2605.14950
- 相关选题：T008
- 相关度：1.00

## 研究背景
当前VLA模型主要依赖2D视觉表示，缺乏深度信息和详细空间关系。现有3D增强方法要么增加系统复杂度和传感器需求，要么依赖大型几何基础模型导致高训练部署成本。

## 核心方法
- Implicit Depth Encoding Module：从多视角RGB图像提取紧凑深度特征（无需额外传感器）
- Spatial Enhancement Module：通过深度感知调制将深度特征融入视觉语言表示
- Progressive Alignment Training：渐进式对齐训练策略，对齐深度增强表示与下游动作学习
- 仅0.9B参数的轻量级框架

## 实验结果
- 四个仿真基准上取得优越性能
- 实际实验中最高平均成功率
- 最小模型尺寸、最低GPU显存占用、最高推理频率
- 相比使用显式3D输入的方法更高效

## 局限性
- 隐式深度估计的精度可能受限于RGB输入质量
- 多视角输入的要求可能限制某些单目场景

## 与选题关联
高度相关T008（融合3D视觉的VLA空间感知增强）：Evo-Depth直接解决了T008的核心研究空白——如何高效地将3D信息注入VLA视觉编码器。其隐式深度编码方法无需额外传感器/大型几何模型，代表了T008研究的一个重要技术路线。

## 关键引用
- 3D-aware VLA方法对比
- 深度估计基础模型
