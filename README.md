

#  曲线拟合程序（Fitting Curve）

本项目是一个基于 Python 的简单曲线拟合程序，用户可以输入多个二维点的坐标，程序将根据这些点进行多项式拟合，并绘制出拟合后的曲线图像。

## 功能特点

- 支持任意数量的数据点输入
- 可指定拟合多项式的阶数
- 输出拟合多项式的系数及表达式
- 使用 Matplotlib 绘图，直观展示原始点与拟合曲线

##  依赖库

请确保已安装以下 Python 库：

numpy
matplotlib

可以通过以下命令安装依赖：


pip install numpy matplotlib


## 运行方法

1. 克隆仓库（如使用 Git）：


   git clone https://gitee.com/capoobot/fitting-curve.git
   cd fitting-curve


2. 运行主程序：


   python curve.py


3. 按照提示依次输入：
   - 点的数量
   - 每个点的 x 和 y 坐标
   - 拟合多项式的阶数

4. 程序将输出多项式表达式，并弹出窗口显示图像。



## 注意事项

- 输入的点应尽量不共线或避免全部 x 相同，否则可能导致拟合不稳定。
- 多项式阶数不宜过高（建议不超过点的数量 - 1），以防止过拟合。
- 图像窗口关闭后程序结束，如需多次绘图请修改代码循环执行逻辑。

## 文件结构

.
├── curve.py          # 主程序
└── README.md         # 项目说明文档




