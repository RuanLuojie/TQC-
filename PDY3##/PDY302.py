num1 = eval(input("請輸入數字: "))
num2 = eval(input("請輸入數字: "))
stop = (input("停止鍵: "))
total = 0
for i in range(num1, num2 + 1):
    if i % 2 == 0:
       total = total + i
print(total)