# 乘法表
n = eval(input())
for i in range(1, n + 1):
  for j in range(1, n + 1):
    print('{:<2d}* {:<2d}= {:<4d}'.format(j, i, j * i), end ='') 
    #要特別注意*和=左邊都沒空隔
  print()