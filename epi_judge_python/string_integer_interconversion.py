from test_framework import generic_test
from test_framework.test_failure import TestFailure


<<<<<<< HEAD
def int_to_string(x):
    if x == 0:
        return '0'
    negate = x < 0
    return_str = ''
    tmp = abs(x)
    digit = 1
    while tmp > 0:
        digit_n = tmp - (tmp // 10 ** digit * 10 ** digit)
        tmp -= digit_n
        return_str = '{0}'.format(digit_n // (10 ** (digit - 1))) + return_str
        digit += 1
    return '-' + return_str if negate else return_str


def string_to_int(s):
    if s == '0':
        return 0
    negate = s[0] == '-'
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    inp = s[1::] if negate else s
    n = 0
    length = len(inp)
    for digit in range(length, 0, -1):
        n += DIGITS[inp[digit - 1]] * 10 ** (length - digit)
    return n * -1 if negate else n
=======
def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    return '0'


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    return 0
>>>>>>> f2c94dc79c9b7b162c48dff6b83a7c33f654d9aa


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
