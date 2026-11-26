a = [1,2,3]
b = [4,5,6]
zip(a,b)
#zip可视化
print(list(zip(a,b)))

for i,j in zip(a,b):
  print(i/2,j*2)

list(zip(a,a,b))

#等于 def fun1(x,y):
        #return(x+y)
fun2 = lambda x,y:x+y
print(fun2(1,3))

#zip:配对->组成多个序列，不修改值
#map:批量应用函数->转换每个元素的值