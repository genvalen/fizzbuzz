import unittest

from fizzbuzz.fizzbuzz import fizz_buzz

class FizzBuzzTest(unittest.TestCase):

# The following parameterized tests examine the output when x is 1 - 15.
# Testing numbers 1 - 15 is enough to ENSURE COVERAGE of all multiples of 3, 5, or both 3 AND 5.
    def test_that_an_input_x_divisble_by_neither_3_or_5_returns_x(self):
        test_cases = [
            (1, 1),
            (2, 2),
            (4, 4),
            (7, 7),
            (8, 8),
            (11, 11),
            (13, 13),
            (14, 14)
        ]
        for number, expected_output in test_cases:
            with self.subTest(f'{number} -> {expected_output}'):
                self.assertEqual(fizz_buzz(number), expected_output)

    def test_that_an_input_divisble_by_3_only_returns_fizz(self):
        test_cases = [
            (3, 'Fizz'),
            (6, 'Fizz'),
            (9, 'Fizz'),
            (12, 'Fizz')
        ]
        for number, expected_output in test_cases:
            with self.subTest(f'{number} -> {expected_output}'):
                self.assertEqual(fizz_buzz(number), expected_output)

    def test_that_an_input_divisble_by_5_only_returns_buzz(self):
        test_cases = [
            (5, 'Buzz'),
            (10, 'Buzz')
        ]
        for number, expected_output in test_cases:
            with self.subTest(f'{number} -> {expected_output}'):
                self.assertEqual(fizz_buzz(number), expected_output)

    def test_that_an_input_divisble_by_both_3_and_5_returns_fizzbuzz(self):
        self.assertEqual('FizzBuzz', fizz_buzz(15))

# Testing numbers beyond 15
#####################################

# Test when x is a multiple of 3 in the range of 3 through 100 
    def test_multiples_of_3_in_range_3_to_100(self):
        test_cases = [
            (num, 'Fizz') 
            for num in range(3, 101, 3) 
            if num % 5 != 0 # ignore multiples of 5
        ]
        for number, expected_output in test_cases:
            with self.subTest(f'{number} -> {expected_output}'):
                self.assertEqual(fizz_buzz(number), expected_output)

# Test multiples of 5 in the range of 5 through 100
    def test_multiples_of_5_in_range_5_to_100(self):
        test_cases = [
            (num, 'Buzz') 
            for num in range(5, 101, 5) 
            if num % 3 != 0 # ignore multiples of 3
        ]
        for number, expected_output in test_cases:
            with self.subTest(f'{number} -> {expected_output}'):
                self.assertEqual(fizz_buzz(number), expected_output)

# Test multiples of 5 that are also multiples of 3 in the range of 5 through 100
    def test_multiples_of_5_that_are_also_multiples_of_3_in_range_5_to_100(self):
        test_cases = [
            (num, 'FizzBuzz') 
            for num in range(5, 101, 5) 
            if num % 3 == 0 
        ]
        for number, expected_output in test_cases:
            with self.subTest(f'{number} -> {expected_output}'):
                self.assertEqual(fizz_buzz(number), expected_output)

# Test output within a list comprehension for various ranges
    def test_outputs_when_x_is_in_the_range_of_1_through_15(self):
        self.assertListEqual(
            [fizz_buzz(x) for x in range(1, 16)],
            [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        )
    def test_outputs_when_x_is_in_the_range_of_16_through_30(self):
        self.assertListEqual(
            [fizz_buzz(x) for x in range(16, 31)],
            [16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz'] 
        )

# Testing Errors
#####################################

# Test that program raises TypeErrors
    def test_that_passing_string_as_argument_raises_error(self):
        with self.assertRaises(TypeError):
            fizz_buzz('42')
    
    def test_that_passing_a_float_as_argument_raises_error(self):
        with self.assertRaises(TypeError):
            fizz_buzz(3.1415926)

    def test_that_passing_a_boolean_as_argument_raises_error(self):
       with self.assertRaises(TypeError):
           fizz_buzz(True)

    def test_that_passing_more_than_one_argument_raises_error(self):
        with self.assertRaises(TypeError):
            fizz_buzz(12, 30)

# Test that program raises ValueErrors
    def test_that_passing_zero_as_argument_raises_error(self):
        with self.assertRaises(ValueError):
            fizz_buzz(0)

    def test_that_passing_a_negative_number_as_argument_raises_error(self):
        with self.assertRaises(ValueError):
            fizz_buzz(-42)


if __name__ == '__main__':
    unittest.main()
