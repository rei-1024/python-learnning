import numpy as np

a = np.arange(2,14).reshape((3,4))
#求矩阵最小值索引
print(np.argmin(a))
#求矩阵最大值索引
print(np.argmax(a))

#求矩阵平均值
print(np.mean(a))
print(a.mean())
print(np.average(a))

#求矩阵中位数
print(np.median(a))

#累加矩阵元素
print(np.cumsum(a))

#每两个数之间的差
print(np.diff(a))

#打印出元素行列array
print(np.nonzero(a))

#排序
print(np.sort(a))

#矩阵转置 行变列 列变行
print(np.transpose(a))
print(a.T)

#在3,7之间的数保持不变，小于3的数变成三，大于7的数变成7
print(np.clip(a,3,7))