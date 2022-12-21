from modules.slae import slae
from copy import deepcopy
from math import prod


def split_matrix_with_replace(matrix):
    matrix = deepcopy(matrix)
    result_column = []
    for i in range(len(matrix)):
        result_column += [matrix[i][-1]]
        matrix[i][-1] = 1
    return matrix, result_column


def get_line_equation(matrix):
    matrix, result_column = split_matrix_with_replace(matrix)
    return slae.solve_by_inverse_matrix(matrix, result_column)


def linear_interpolation(matrix):
    line_equation = get_line_equation(matrix)
    x = min(matrix[1][0], matrix[0][0]) + (max(matrix[1][0], matrix[0][0]) - min(matrix[1][0], matrix[0][0])) / 2
    return [x, x * line_equation[0] + line_equation[-1]]


def linear_extrapolate(matrix, indent=3):
    line_equation = get_line_equation(matrix)
    x = min(matrix[1][0], matrix[0][0]) - indent
    return [x, x * line_equation[0] + line_equation[-1]]


def interpolate_piece_line(matrix, indent=3):
    matrix_xy = [linear_extrapolate(matrix[:2], indent=indent)]
    for i in range(len(matrix) - 1):
        matrix_xy += [linear_interpolation(matrix[i:i+2])]
    matrix_xy += [linear_extrapolate(matrix[-2:], indent=-indent)]

    return matrix_xy


def lagrange_interpolation_polynomial(matrix, x):
    return sum([row[1] * get_basic_polynomials(matrix, x, index) for index, row in enumerate(matrix)])


def get_basic_polynomials(matrix, x, i):
    looking_for = ((x - row[0]) / (matrix[i][0] - row[0]) for index, row in enumerate(matrix) if index != i)

    return prod(looking_for)