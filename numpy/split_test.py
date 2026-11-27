import numpy as np

a = np.arange(12).reshape((4,3))
#对列进行分割 分成两块
print(np.split(a,4,axis=0))

#不等量分割
print(np.array_split(a,2,axis=1))

#hsplit横向分割 vsplit竖向分割
print(np.hsplit(a,3))
print(np.vsplit(a,2))