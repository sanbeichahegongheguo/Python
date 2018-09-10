# -*- coding: utf-8 -*-
"""
subplot绘制平均分配的多图
"""
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

# 绘制第一个图
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])
# 绘制第二个图
x = np.linspace(-1, 1, 66)
y = x**2 + 1
plt.subplot(2, 2, 2)
plt.plot(x, y, color='red', linewidth=1.0, linestyle='--')
# 绘制第三个图
x = np.linspace(-1, 1, 66)
y = x**3 + 1
plt.subplot(2, 2, 3)
plt.plot(x, y)
# 绘制第四个图
x = np.linspace(-1, 1, 66)
y = x**4 + 1
plt.subplot(2, 2, 4)
plt.plot(x, y, color='blue')
plt.show()
