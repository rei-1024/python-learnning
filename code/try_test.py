try:
  file = open("eeee","r+") 
#将错误信息存入变量e中
except Exception as e:
  print(e)
  response = input("Do you want to cteate new file?\nYes\nNo\n")
  if response == "Yes":
    file = open("eeee","w")
  else:
    pass
else:
  file.write("ssss")
file.close()