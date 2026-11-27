import numpy as np

#根据索引找到值
a = np.arange(3,15).reshape((3,4))
print(a[1][1])
#冒号代表所有数
print(a[1][:])

#for循环默认迭代行 axis=0
#想遍历列 先转置再遍历行
for column in a.T:
  print(column)

#一维迭代器 迭代每一个元素
for item in a.flat:
  print(item)