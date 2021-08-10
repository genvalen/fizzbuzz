# FizzBuzzer

## What is this repository for?

FizzBuzzer allows you to implement ``fizz_buzz`` on the command line.

``fizz_buzz`` is a function that accepts an integer, x, as an argument and returns an output for x according to the following rules:
* If x is a positive integer (i.e., greater than 0) and:
    * divisible by 3, return the string 'Fizz'
    * divisible by 5, return the string 'Buzz'
    * divisible by both 3 and 5, return the string 'FizzBuzz'

If x doesn't satisfy any of the above conditions, simply return x.

## Requirements

* Python 3.7.4+

## How to Use
To begin using, clone the repository, open in the command line interface, and type `$ fizzbuzzer` followed by the integer(s) you want to convert. If you pass in more than one integer, each result is returned on a new line. Here are a few input examples:

```
$ fizzbuzzer 3   
Fizz

$ fizzbuzzer 1 2 3 5 15
1
2
Fizz
Buzz
FizzBuzz
```

The unit tests for ``fizz_buzz`` can be run on the command line interface:

```
$ python -m unittest
$ python -m unittest -v
```

As well as the doctests:

```
$ python -m doctest fizzbuzz.py 
$ python -m doctest fizzbuzz.py -v
```