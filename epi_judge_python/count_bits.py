from test_framework import generic_test


<<<<<<< HEAD
def count_bits(x):
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count
=======
def count_bits(x: int) -> int:
    # TODO - you fill in here.
    return 0
>>>>>>> f2c94dc79c9b7b162c48dff6b83a7c33f654d9aa


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
