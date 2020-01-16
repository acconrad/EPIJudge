from test_framework import generic_test


<<<<<<< HEAD
def power(x, y):
    result = 1.0
    pwr = y
    if y < 0:
        pwr = -pwr
        x = 1.0/x
    while pwr:
        if pwr & 1:
            result *= x
        x = x*x
        pwr >>= 1

    return result
=======
def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    return 0.0
>>>>>>> f2c94dc79c9b7b162c48dff6b83a7c33f654d9aa


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
