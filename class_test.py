#规范类名首字母要大写
class Calculator:
  name = "good calculator" #属性
  price = "20"#属性

  #初始化__init__
  def __init__(self,name,price,height):
    #self.xxx 属于这个实例自己的属性
    self.n = name
    self.p = price
    self.h = height


  def add(self,x,y): #功能
    print(self.n)
    result = x + y
    print(result)

  def minus(self,x,y):
    result = x - y
    print(result)

#使用代码
#创建对象的时候，括号里传参数，传给__init__
cal = Calculator("gg",21,175)
cal.add(1,24)
print(cal.p)