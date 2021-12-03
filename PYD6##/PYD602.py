# TODO
total=[]
for i in range(5):
    temp = input()
    if temp == 'A':
        total.append(1)
    elif temp == 'J':
        total.append(11)
    elif temp == 'Q':
        total.append(12)
    elif temp == 'K':
        total.append(13)
    else:
        total.append(eval(temp))
print(sum(total))