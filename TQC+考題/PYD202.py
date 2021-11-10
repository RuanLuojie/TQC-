# TODO
num = eval(input())

if num % 3 == 0 and num % 5 == 0:
    print('{}  is a multiple of 3 and 5.'.format(num))
elif num % 3 == 0:
    print('{}  is a multiple of 3.'.format(num))
elif num % 5 == 0:
    print('{} is a multiple of 5.'.format(num))
else:
    print('{} is not a multiple of 3 or 5.'.format(num))

"""
_ is a multiple of 3 and 5.
_ is a multiple of 3.
_ is a multiple of 5.
_ is not a multiple of 3 or 5.
"""