from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    rows = len(square_matrix)

    if rows == 0:
        return []

    cols = len(square_matrix[0])

    top_row, bottom_row, left_col, right_col, orientation = 0, rows - 1, 0, cols - 1, 0
    flat_arr = []

    while top_row <= bottom_row and left_col <= right_col:
        if orientation == 0:
            for i in range(left_col, right_col+1):
                flat_arr.append(square_matrix[top_row][i])
            orientation += 1
            top_row += 1
        elif orientation == 1:
            for i in range(top_row, bottom_row+1):
                flat_arr.append(square_matrix[i][right_col])
            orientation += 1
            right_col -= 1
        elif orientation == 2:
            for i in range(right_col, left_col-1, -1):
                flat_arr.append(square_matrix[bottom_row][i])
            orientation += 1
            bottom_row -= 1
        elif orientation == 3:
            for i in range(bottom_row, top_row-1, -1):
                flat_arr.append(square_matrix[i][left_col])
            orientation = 0
            left_col += 1

    return flat_arr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
