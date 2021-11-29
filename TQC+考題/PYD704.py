# TODO
num = set()

while True:
    temp = eval(input())
    if temp == -9999:
        break
    else:
        num.add(temp)

print('Length: {}'.format(len(num)))
print('Max: {}'.format(max(num)))
print('Min: {}'.format(min(num)))
print('Sum: {}'.format(sum(num)))

"""
Length: _
Max: _
Min: _
Sum: _
"""
