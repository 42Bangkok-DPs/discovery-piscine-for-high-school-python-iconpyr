#!/usr/bin/env python3
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

result = x*y
# print(result)
print(f'{x} X {y} = {result}' )

if result > 0:
    print('The result is positive')
elif result < 0:
    print('The result is negative')
else:
    print('The result is positive and negative')
