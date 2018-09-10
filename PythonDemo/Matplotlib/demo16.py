# -*- coding: utf-8 -*-
"""
figure绘制多图 方法2
"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 定义figure
plt.figure()
# 提前分隔figure
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, 0:2])
ax3 = plt.subplot(gs[1, 2])
ax4 = plt.subplot(gs[2, :])

# 绘制图像
ax1.plot([0, 1], [0, 1])
ax1.set_title('Test2')

ax2.plot([0, 1], [0, 1])
ax2.set_title('try1')

ax3.plot([0, 1], [0, 1])
ax3.set_title('try2')

ax4.plot([0, 1], [0, 1])

plt.show()
