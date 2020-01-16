from test_framework import generic_test


def reverse_bits(x):
    r_bit = 0
    bits = 64
    while bits:
        r_bit += ((x >> (bits-1)) & 1) << (64 - bits)
        bits -= 1

    return r_bit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
