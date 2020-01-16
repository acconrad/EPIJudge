import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


<<<<<<< HEAD
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
=======
def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # TODO - you fill in here.
    return Rect(0, 0, 0, 0)
>>>>>>> f2c94dc79c9b7b162c48dff6b83a7c33f654d9aa


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
