# TODO
t1 = ()
t2 = ()
print("Create tuple1:")
# TODO
while True:
    temp = eval(input())
    if temp == -9999:
        break
    else:
        t1 = t1 + (temp,)
print("Create tuple2:")
# TODO
while True:
    temp = eval(input())
    if temp == -9999:
        break
    else:
        t2 = t2 + (temp,)

print('Combined tuple before sorting: {}'.format(t1+t2))
print('Combined list after sorting: {}'.format(sorted(t1+t2)))

"""
Combined tuple before sorting: _
Combined list after sorting: _
"""
