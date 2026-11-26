import numpy as np

#运算时元素数量要相等
a = np.array([1,2,3,4])
b = np.arange(4)

#sin,cos,tan,cot要调用np
c = 10*np.sin(a)
#平方
d = b ** 2
print(c)
print(d)

#返回true,false
print(b < 3)
print(b == 3)

e = np.array([[1,2],
              [3,4]])
f = np.arange(4).reshape(2,2)
#数组相乘
g = e * f
#矩阵相乘
g_dot = np.dot(e,f)
g_dot2 = e.dot(f)
print(g_dot)
print(g_dot2)

#0到1随机数字，括号里参数是shape
h = np.random.random((2,4))
#axis=0在列数做运算 axis=1在行数做运算
print(np.sum(h),axis=1)
print(np.max(h))
print(np.min(h))