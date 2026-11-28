import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4])
p = pd.Series([1,2,3])

#index是行的名字 columns是列的名字
df = pd.DataFrame(np.arange(12).reshape((3,4)),index=p,columns=s)
#字典形式最常见 key为列号 value为值,自定义index写在功能里面
data = {"name":["Jack","Lily"],
        "age":[12,23],
        "sex":["male","female"]}
df2 = pd.DataFrame(data,index=["class1", "class2"])
#打印每一列的数据类型
df.dtypes
#打印行标签
df.index
#打印列标签
df.columns
#打印所有值
df.values
#计算每一列的平均值，方差等数据
#count有多少条数据 mean平均值 std标准差 min最小值 25%第一四分位数 50%中位数 75%第三四分位数
df.describe()

#矩阵转置
df.T

#将index排序 ascending=True为正序 ascending=False为倒序
df2.sort_index(axis=0,ascending=False)
#将values排序
df2.sort_values(by="sex")

#select by lable:loc
#选择要的行数据
df2[0:1]
df2["class1":"class2"]
#选择要的列数据
df2.name
#更具体的方法
df2.loc["class1","age"]

#select by position:iloc
df2.iloc[1,1]
df2.iloc[0:2,0:3]

#boolean indexing
df2[df2.sex == "male"]

#修改值
df2.iloc[0,0] = "Max"
df2.loc["class1","name"] = "Max"
#增加新的column
df2["height"] = [187,165]
#增加新的index需要loc
df2.loc["class3"] = ["Tom",18,"male",178]
#先定义值
df2["weight"] = pd.Series([65,50,76],index=["class1","class2","class3"])
print(df2)

#处理异常数据
#how="any"只要有nan就删除 how="all"所有都是nan才删除
df2.dropna(axis=0,how="any")
#填充nan数据
df2.fillna(value=0)
#检查有没有缺失数据 返回boolean值
print(df2.isnull())
#当数据太多无法确定时
np.any(df2.isnull()) == True