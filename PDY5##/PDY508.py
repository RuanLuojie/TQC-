def compute(x,y):
    if y == 0:
        print(x)
    else:
        compute(y,x%y)
x,y = eval(input())
compute(x,y)