#key:value
d = {"apple":1,"pear":{1:3,"boy":4},"orange":3}
d2 = {1:"a",2:"b"}
print(d["apple"])
print(d2[1])

#delete删除元素
del d["orange"]
#加元素
d["watermelon"] = 4
print(d["pear"]["boy"])