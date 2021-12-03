# TODO

num = []

for i in range(9):
    temp = eval(input())
    num.append(temp)
    
maxNumber = max(num)
minNumber = min(num)
maxNumberIndex = num.index(maxNumber)
minNumberIndex = num.index(minNumber)

print('Index of the largest number {} is: ({}, {})'.format(maxNumber,maxNumberIndex//3,maxNumberIndex%3))
print('Index of the smallest number {} is: ({}, {})'.format(minNumber,minNumberIndex//3,minNumberIndex%3))

"""
Index of the largest number _ is: (_, _)
Index of the smallest number _ is: (_, _)
"""
