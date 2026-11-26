import numpy as np

#将列表转换为矩阵
array = np.array([[1,2,3],
                  [2,3,4],
                  [3,4,5]])
print(array)

#几维数组
print("number of dim:",array.ndim)
#几行几列
print("shape:",array.shape)
#共多少个元素
print("size:",array.size)