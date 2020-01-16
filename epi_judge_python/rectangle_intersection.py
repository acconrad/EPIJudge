import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    invalidRect = Rectangle(0, 0, -1, -1)

    rx = max(R1[0], R2[0])
    r1xend = R1[0] + R1[2]
    r2xend = R2[0] + R2[2]
    rxend = min(r1xend, r2xend)
    rwidth = rxend - rx

    ry = max(R1[1], R2[1])
    r1yend = R1[1] + R1[3]
    r2yend = R2[1] + R2[3]
    ryend = min(r1yend, r2yend)
    rheight = ryend - ry

    if rwidth < 0 or rheight < 0:
         return invalidRect
    return Rectangle(rx, ry, rwidth, rheight)


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
