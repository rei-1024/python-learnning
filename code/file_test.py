#打印文件会生成在哪里
import os
print(os.getcwd())

text = "first test\nsecond test\nlast test"

#创建文件 第一个参数是名字 第二个参数是打开形式 w=write r=read a=append加内容
my_file = open("file_test.txt","w")
#写文件
my_file.write(text)
#一定要关上
my_file.close()


file = open("file_test.txt","r")
#将file里的内容读取到content
content = file.read()

#逐行读取 将内容存放于list
content = file.readline()

#输出所有行
content = file.readlines()
print(content)
