from test_framework import generic_test


<<<<<<< HEAD
def parity(x):
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count % 2
=======
def parity(x: int) -> int:
    # TODO - you fill in here.
    return 0
>>>>>>> f2c94dc79c9b7b162c48dff6b83a7c33f654d9aa


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
