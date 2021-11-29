# TODO
count = eval(input())
for i in range(count):
    string = input()
    num = string.split(' ')
    for j in range(len(num)):
        num[j]= eval(num[j])
    print('{:.2f}'.format(max(num)-min(num)))
