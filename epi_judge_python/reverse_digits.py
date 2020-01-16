from test_framework import generic_test


<<<<<<< HEAD
def reverse(x):
    # lead = 1
    # if x < 0:
    #     lead = -1
    #     x = abs(x)
    # return int(''.join(reversed(str(x)))) * lead
    result, xtrack = 0, abs(x)
    while xtrack:
        result = result * 10 + xtrack % 10
        xtrack //= 10
    return result if x > 0 else result * -1
=======
def reverse(x: int) -> int:
    # TODO - you fill in here.
    return 0
>>>>>>> f2c94dc79c9b7b162c48dff6b83a7c33f654d9aa


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
