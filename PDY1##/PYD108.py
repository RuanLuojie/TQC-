# TODO
x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())

x = (x1 - x2) * (x1 - x2)
y = (y1 - y2) * (y1 - y2)
distance = (x + y)**0.5

print("(", x1 ,"," , y1 ,")")
print("(",x2,",",y2,")")
print('Distance= {:.4f}'.format(distance))

"""
Distance = _
"""