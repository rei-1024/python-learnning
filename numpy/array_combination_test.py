import numpy as np

a = np.array([1,1,1])[:,np.newaxis]#新增维度
b = np.array([2,2,2])[:,np.newaxis]

#vertical stack上下合并
c = np.vstack((a,b))
print(c)
#horizontal stack
d = np.hstack((a,b))
print(d)

#axis=1横向合并 axis=0纵向合并
e = np.concatenate((a,a,b,b),axis = 1)
print(e)