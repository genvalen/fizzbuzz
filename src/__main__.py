# make fizzbuzz.py executable

import sys

from fizzbuzzer.fizzbuzz import fizz_buzz

args = sys.argv[1:]
# for arg in args:
#     print(type(arg), arg)

if args:
    for arg in args:
        print(fizz_buzz(arg))
else:
    print('Whoops! You forgot to pass in a number (or two) to convert with FizzBuzzer')