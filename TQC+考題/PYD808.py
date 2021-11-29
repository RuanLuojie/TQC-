# TODO
string = input()

if string[0:3].isdigit() and string[3]=="-" and string[4:6].isdigit() and string[6]=="-" and string[7:].isdigit():
    print('Valid SSN')
else:
    print('Invalid SSN')



"""
Valid SSN
Invalid SSN
"""