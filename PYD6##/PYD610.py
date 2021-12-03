#TODO

temp = []
for w in range(1, 5):
    print('Week {}:'.format(w))
    for d in range(1, 4):
        print('Day {}: '.format(d), end = '')
        temp.append(eval(input()))

print('Average: {:.2f}'.format(sum(temp)/len(temp)))
print('Highest: {}'.format(max(temp)))
print('Lowest: {}'.format(min(temp)))



"""
Week _:
Day _: 
Average: _
Highest: _
Lowest: _
"""