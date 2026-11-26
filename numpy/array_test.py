import numpy as np

#数据类型 位数越小，占用空间越小
a = np.array( [[1,2,3],
              [2,3,4],
              [3,4,5]],dtype=int)
print(a)
print(a.dtype)

#全部为0的矩阵
b = np.zeros((3,3))
print(b)

c = np.ones((3,3),dtype = int)
print(c)
print(c.dtype)

#有序矩阵 x到y-1，步长
#reshape可改变行列数
d = np.arange(1,12,2).reshape((2,3))
print(d)

#生成线段，x到y，几段
e = np.linspace(1,10,4).reshape((1,4))
print(e)