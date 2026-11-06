#break直接跳出大循环
while True:
  b = input("type something:")
  if b == "1":
    break
  
print("end")

#continue跳过下一步重新开始循环
while True:
  b = input("type something:")
  if b == "1":
    continue
  else:
    break

print("end")