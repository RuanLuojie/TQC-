#TODO
data = {}
while True:
    #Key: (後方有一空白格)
    key = input("Key: ")
    if key == "end":
        break
    #Value: (後方有一空白格)
    value = input("Value: ")
    data[key]=value

sk = input("Search key: ")
print(sk in data)