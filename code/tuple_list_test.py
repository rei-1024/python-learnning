#元组
a_tuple = (1,2,3,4,5)
b_tuple = 6,7,8,9,10
#列表
a_list = [1,2,3,4,5]

for element in a_list:
  print(element)

#index为参数 len()代表长度  遍历list
for index in range(len(a_list)):
  print("index:",index,"\nnumber in list:",a_list[index])

#在list加一个值append
a_list.append(6)
#在list中在哪个位置添加什么值insert（a，b）
a_list.insert(6,7)
#从第一次出现的数字开始remove
a_list.remove(1)

#与其他语言相同打印元素,索引为-1时从最后一位开始算
print(a_list[0])
print(a_list[-1])
a_list.insert(0,1)
#从第0位到第3位
print(a_list[0:3])

#打印元素的索引
print(a_list.index(1))
#打印元素出现的次数
print(a_list.count(1))
#将元素按照从小到大排序
a_list.sort()
print(a_list)
#从大到小排序
a_list.sort(reverse = True)
print(a_list)

#多维列表
multi_dim_a = [[1,2,3],
               [2,3,4],
               [5,6,7]]

print(multi_dim_a[0][1])