# TODO
string = input()
total = 0
for i in range(len(string)):
    char = string[i]
    total = total + ord(char)
    print("ASCII code for '{}' is {}".format(char,ord(char)))
print(total)


"""
ASCII code for '_' is _
"""