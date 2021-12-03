# 數字反轉
s = input()
n = eval(s)
for i in range(len(s)):  
  print('{}'.format(n % 10), end ='')
  n //= 10