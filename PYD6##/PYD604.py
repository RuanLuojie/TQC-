# TODO
num = []
counter = []

for i in range(10):
    temp = eval(input())
    num.append(temp)
    counter.append(num.count(temp))

maxCount = max(counter)
maxCountIndex = counter.index(maxCount)

print(num[maxCountIndex])
print(maxCount)