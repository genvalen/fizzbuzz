from typing import List, Any
    
def is_divisible_by_3(x: int) -> bool:
    '''Determine if x is divisible by 3'''
    return x % 3 == 0

def is_divisible_by_5(x: int) -> bool:
    '''Determine if x is divisible by 5'''
    return x % 5 == 0

def fizz_buzz(x: int) -> Any:
    '''Return an output for x according to the following rules:

    If x is a positive integer (i.e., greater than 0) and:
        divisible by 3, return the string 'Fizz';
        divisible by 5, return the string 'Buzz';
        divisible by both 3 and 5, return the string 'FizzBuzz';
        and if divisible by neither 3 nor 5, simply return x.
    
    >>> [fizz_buzz(num) for num in range(1,16)]
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
    >>> fizz_buzz(15)
    'FizzBuzz'

    The fizz_buzz method will only accept a positive integer as an argument, anything else will raise an error.
    >>> fizz_buzz('42')
    Traceback (most recent call last):
        ...
    TypeError: 42 is not an integer.
    >>> fizz_buzz(True)
    Traceback (most recent call last):
        ...
    TypeError: True is not an integer.

    # >>> fizz_buzz(3.1415926)
    # Traceback (most recent call last):
    #     ...
    # TypeError: 3.1415926 is not an integer.  
    '''
    # If x is NOT an integer, or if IT IS a boolean, this check will raise a TypeError
    if isinstance(x, bool) or not isinstance(x, int):
        raise TypeError(f'{x} is not an integer.')

    # If x has a value that is NOT positive, this check will raise a ValueError       
    if x <= 0:
        raise ValueError(f'{x} is not a positive number.')

    # The logic to return appropriate output starts here
    if is_divisible_by_3(x) and is_divisible_by_5(x): 
        return 'FizzBuzz'

    if is_divisible_by_3(x): 
        return 'Fizz'

    if is_divisible_by_5(x): 
        return 'Buzz'

    return x


if __name__ == '__main__':
        import doctest
        doctest.testmod()