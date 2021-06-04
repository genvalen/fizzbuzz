# this file makes the fizzbuzz package executable

import sys

from fizzbuzz.fizzbuzz import fizz_buzz
integer = int(sys.argv[1])
print(fizz_buzz(integer))
