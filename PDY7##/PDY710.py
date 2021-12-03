data = {}
while True:
    key = input("key: ")
    if key == "end" :
        break
    value = input("Value: ")
    data[key]=value

sk = input("Search key: ")
print(sk in data)