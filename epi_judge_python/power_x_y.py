from test_framework import generic_test


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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
