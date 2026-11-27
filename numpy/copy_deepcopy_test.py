import numpy as np

a = np.arange(4)

b = a
c = a
d = b
a[0] = 10
#第一项到第二项
d[1:3] = [20,30]

#deep copy 两个array完全独立，互不影响
b = a.copy()