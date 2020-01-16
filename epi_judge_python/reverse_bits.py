from test_framework import generic_test


<<<<<<< HEAD
def reverse_bits(x):
    r_bit = 0
    bits = 64
    while bits:
        r_bit += ((x >> (bits-1)) & 1) << (64 - bits)
        bits -= 1

    return r_bit
=======
def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    return 0
>>>>>>> f2c94dc79c9b7b162c48dff6b83a7c33f654d9aa


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
