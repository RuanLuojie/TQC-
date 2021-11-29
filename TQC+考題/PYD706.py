# TODO
count = eval(input())
for i in range(count):
    string = input()
    string = set(string.lower().replace(" ", ''))
    print(len(string)==26)
