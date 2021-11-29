#TODO
dict1 = {}
dict2 = {}
for i in range(1,3):
    print('Create dict{}:'.format(i))
    while True:
        #Key: (後方有一空白格)
        key = input("Key: ")
        if key =='end':
            break
        #Value: (後方有一空白格)
        value = input("Value: ")
        if i == 1:
            dict1[key]=value
        else:
            dict2[key]=value

dict3 = dict1.copy()
dict3.update(dict2)
dict4 = sorted(dict3)

for i in dict4:
    print('{}: {}'.format(i, dict3[i]))