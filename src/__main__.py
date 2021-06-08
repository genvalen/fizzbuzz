# make fizzbuzz.py executable

import sys

from fizzbuzzer.fizzbuzz import fizz_buzz

args = sys.argv[1:]
args = map(int, args)

# print output of each argument on a new line
output = ""
for arg in args:
    output += '{}\n'.format(
        fizz_buzz(arg)
    )

print(output)