# RelAfford6D: Relational 6D Affordance Graphs for Constraint-Driven Robotic Manipulation

- **arXiv**: 2606.27036
- **Authors**: Guodong Zhang et al.
- **Date**: 2026-06-25
- **Topics**: T008 (3D视觉+VLA)
- **Relevance**: 0.85

## 核心贡献

提出RelAfford6D，一个基于关系6D可供性图（Relational 6D Affordance Graph）的训练无关框架：
1. **语义拓扑推断**：从自由格式指令推断主要交互部件及其物理锚点的语义拓扑
2. **SE(3)位姿估计**：利用视觉基础模型将拓扑节点提升为精确的度量位姿
3. **运动学约束**：将下游执行建模为运动学约束满足问题
4. **闭环重规划**：动态环境中对抗干扰的鲁棒跟踪

## 方法亮点

- **Training-free**：无需训练，利用预训练视觉基础模型
- **物理流形约束**：旋转关节/滑动关节的轨迹在严格定义的物理流形上
- **跨类别泛化**：零样本跨类别成功率高
- 自由格式指令→语义拓扑→SE(3)位姿→运动学约束→轨迹合成

## 实验结果

- 仿真和真实环境均验证
- 零样本成功率和跨类别泛化优于数据驱动基线
- 对铰接物体（articulated objects）操作效果突出

## 与T008的关联

- 6D空间感知与VLA操作直接相关
- SE(3)位姿估计 + 运动学约束为VLA提供物理先验
- 训练无关特性使其可作为VLA的即插即用增强模块
- 与T008"3D视觉感知融入VLA增强空间理解能力"的方向一致
