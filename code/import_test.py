#模块名太长时可以as来代替
import time as t
print(t.localtime())

#只想用指定功能时
from time import time,localtime
print(localtime())
print(time())

#所有功能
from time import *
