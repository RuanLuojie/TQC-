# TODO
row = eval(input())
col = eval(input())

for r in range(row):
    for c in range(col):
        print('{:4d}'.format(c-r),end = '')
    print()
