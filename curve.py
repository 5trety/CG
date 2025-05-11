import numpy as np
import matplotlib.pyplot as plt

# 输入点的坐标
points = []
n = int(input("请输入点的数量："))
for i in range(n):
    x = float(input(f"请输入第{i+1}个点的x坐标："))
    y = float(input(f"请输入第{i+1}个点的y坐标："))
    points.append((x, y))

# 将点拆分为两个列表，分别存储x和y值
x_values = np.array([point[0] for point in points])
y_values = np.array([point[1] for point in points])

# 选择多项式拟合的阶数
degree = int(input("请输入拟合多项式的阶数："))

# 进行多项式拟合
coeffs = np.polyfit(x_values, y_values, degree)
polynomial = np.poly1d(coeffs)
print(f"拟合多项式系数为：{coeffs}")
print(f"拟合多项式为：\n{polynomial}")

# 生成拟合后的点坐标（用于绘图）
x_fit = np.linspace(min(x_values), max(x_values), 500)
y_fit = polynomial(x_fit)

# 绘制原始点和拟合曲线
plt.scatter(x_values, y_values, color='red', label='origin points')
plt.plot(x_fit, y_fit, color='blue', label=f'fitting curve (degree={degree})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('curve and points')
plt.legend()
plt.grid(True)
plt.show()