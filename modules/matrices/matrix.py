from modules.vectors import vector
from modules.decorators import args_copy_need

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

def scalar_dif(matrix, scalar): 
    return [vector.dev_scalar(row, scalar) for row in matrix]

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

def multiply_row_by_scalar(matrix: list, index: int, scalar: float): 
    matrix[index] = vector.multi_scalar(get_row(matrix, index), scalar)
    return matrix

def dif_row_by_scalar(matrix: list, index: int, scalar: float):
    matrix[index] = vector.dev_scalar(get_row(matrix, index), scalar)
    return matrix

def sum_matrix_rows(m, row_idxs: list, scalars: list): 
    """
    :param row_idxs: Список индексов строк для сложения
    :param scalars: Список чисел, на каторые будут домножены строки (первый элемент соответствует первому элементу из row_idxs)
    """
    m[row_idxs[0]] = vector.plus(
        vector.multi_scalar(m[row_idxs[0]], scalars[0]),
        vector.multi_scalar(m[row_idxs[1]], scalars[1])
    )
    return m

def get_unit_matrix(size: int):
    m = []
    for i in range(size): 
        row = []
        for j in range(i): row.append(0)
        row.append(1)
        for j in range(size-i-1): row.append(0)
        m.append(row)
    return m


@args_copy_need
def attach_matrix(base_matrix: list, matrix_to_add: list):
    for i in range(len(base_matrix)):
        base_matrix[i].extend(matrix_to_add[i])

    return base_matrix