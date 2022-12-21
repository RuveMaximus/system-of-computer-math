from modules.matrices import matrix
from modules.decorators import args_copy_need

def count_row_position(row: list):
    pos = 0
    while row[pos] == 0: pos+=1
    return pos 


def refresh_matrix(m: list):
    _matrix = [None]*len(m)
    for row in m:
        pos = count_row_position(row)
        if _matrix[pos] is not None: 
            pos = _matrix.index(None, pos)

        _matrix[pos] = row
    return _matrix


def is_solution(m: list) -> bool:
    for i in range(len(m)):
        if m[i][i] != 1 or m[i].count(0) + 2 < len(m[i]): 
            return False
    return True


def add_column(m: list, col_to_add: list):
    if len(m) != len(col_to_add):
        raise ValueError('The length of matrix must be equal to the length of column to add')
    for i in range(len(m)): 
        m[i].append(col_to_add[i])
    return m


def left_complete(m):
    for i in range(len(m)):
        for j in range(i):
            if m[i][j] != 0:
                return False
    return True


def right_complete(m):
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            if m[i][j] != 0:
                return False
    return True
    

def attach_unit_matrix(m):
    for i in range(len(m)):
        row = []
        for j in range(i): row.append(0)
        row.append(1)
        for j in range(len(m)-i-1): row.append(0)
        m = add_column(m, row)
    
    return m


def inverse_matrix(m):
    while not left_complete(m):
        for i in range(len(m)):
            if m[i][i] == 0: m = refresh_matrix(m)
            m = matrix.dif_row_by_scalar(m, i, m[i][i])
            for j in range(i):
                m = matrix.sum_matrix_rows(m, [i, j], [-1, m[i][j]])

    while not right_complete(m):
        for i in range(len(m)):
            if m[i][i] == 0: m = refresh_matrix(m)
            m = matrix.dif_row_by_scalar(m, i, m[i][i])
            for j in range(i+1, len(m)):
                m = matrix.sum_matrix_rows(m, [i, j], [1, -m[i][j]])

    return m


@args_copy_need
def solve(m: list, result_column: list):
    m = add_column(m, result_column)
    m = inverse_matrix(m)

    return [round(row[-1], 2) for row in m]

@args_copy_need
def solve_by_inverse_matrix(m: list, result_column: list):
    m = attach_unit_matrix(m)
    m = inverse_matrix(m)

    m = [row[len(result_column):] for row in m]
    result_column = [[row]*len(result_column) for row in result_column]
    m = matrix.multiply(m, result_column)
    
    return [row[0] for row in m]
