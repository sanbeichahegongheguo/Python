# -*- coding: utf-8 -*-
"""
figure的使用
学习如何设置图像所在框的大小，以及设置图像线条性质
"""
import matplotlib.pyplot as plt
import numpy as np
# 设置x的取值，取50个点
x = np.linspace(-1, 1, 50)


# figure 1
y1 = 2 * x + 1
plt.figure()
plt.plot(x, y1)


# figure 2
y2 = x**2
plt.figure()
plt.plot(x, y2)


# figure 3，指定figure的编号并指定figure的大小,
y2 = x**2
plt.figure(num=5, figsize=(4, 4))
# 在一个坐标轴上画两个图形
plt.plot(x, y1)
# 指定线的颜色参数3, 宽度参数4和类型参数5
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
plt.show()
