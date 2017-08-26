import matplotlib.pyplot as plt
import numpy as np

#普通图：plot
#离散图：scatter
#柱状图：bar
#等高线：contour
#灰度图：imshow
#饼状图：pie
#量场图：quiver

# plt.figure(1.csv)
# plt.subplot(211)
# plt.plot([1.csv,2,3,4],[2,9,3,6] ,'r-')
# plt.ylabel('some numbers')
# ###默认轴区间
# plt.axis([0, 6, 0, 20])
# # plt.show()
#
# plt.subplot(212)
# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'rs', t, t**2, 'b-', t, t**3, 'g^')
# plt.show()



plt.figure(1) # 第一个图形
plt.subplot(221) # 第一个图形的第一个子图
plt.plot([1, 2, 3])
plt.subplot(222) # 第一个图形的第二个子图
plt.plot([4, 5, 6])
plt.figure(2) # 第二个图形
plt.plot([4, 5, 6]) # 默认创建 subplot(111)
plt.figure(1) # 当前是图形 1.csv，subplot(212)
plt.subplot(221) # 将第一个图形的 subplot(211) 设为当前
plt.title('Easy as 1.csv, 2, 3') # 子图 211 的标题
plt.show()

plt.hist
