from modules.vectors import vector


def summ(m1, m2):
    return [vector.plus(m1[i], m2[i]) for i in range(len(m1))]

def dif(m1, m2): 
    return [vector.minus(m1[i], m2[i]) for i in range(len(m1))]

def transposition(m):
    return [[m[cell][row] for cell in range(len(m))] for row in range(len(m[0]))]

def multiply(m1, m2): 
    m2 = transposition(m2)
    return [[sum(vector.multi(m1_row, m2_row)) for m2_row in m2] for m1_row in m1]

def scalar_multiply(matrix, scalar): 
    return [vector.multi_scalar(row, scalar) for row in matrix]

def get_row(matrix, index: int): 
    return matrix[index]

def get_col(matrix, index: int): 
    return get_row(transposition(matrix), index)

def swap_rows(m, indexes: list):
    a = [None]*len(m)

    a[indexes[1]] = m[indexes[0]]
    a[indexes[0]] = m[indexes[1]]
    
    for index, row in enumerate(a): 
        if row is None:
            a[index] = m[index] 
    return a

def multiply_row_by_scalar(matrix, index: int, scalar: float): 
    matrix[index] = vector.multi_scalar(get_row(matrix, index), scalar)
    return matrix

def sum_matrix_rows(m, row_idxs: list, scalars: list): 
    m[row_idxs[0]] = vector.plus(
        vector.multi_scalar(m[row_idxs[0]], scalars[0]),
        vector.multi_scalar(m[row_idxs[1]], scalars[1])
    )
    return m