# 迴圈整數連加
a = eval(input())
b = eval(input())
total = 0
for i in range(a, b + 1):
  total += i
print(total)