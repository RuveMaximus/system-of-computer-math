import sys
sys.path.append("..")

from vectors import vector

def summ(m1, m2):
    return [vector.plus(m1[i], m2[i]) for i in range(len(m1))]

def dif(m1, m2): 
    return [vector.minus(m1[i], m2[i]) for i in range(len(m1))]

def transposition(m):
    return [[m[cell][row] for cell in range(len(m))] for row in range(len(m[0]))]

def multiply(m1, m2): 
    m2 = transposition(m2)
    return [[sum(vector.multi(m1_row, m2_row)) for m2_row in m2] for m1_row in m1]

def scalar_multiply(m, scalar): 
    return [vector.multi_scalar(row, scalar) for row in m]

def get_row(m, index): 
    return m[index]

def get_col(m, index): 
    return get_row(transposition(m), index)

def swap_rows(m, indexes: list):
    a = [[None]*len(m)][0]

    a[indexes[1]] = m[indexes[0]]
    a[indexes[0]] = m[indexes[1]]
    
    for index, row in enumerate(a): 
        if row is None:
            a[index] = m[index] 
    return a

def multiply_row_by_scalar(m, index, scalar): 
    m[index] = vector.multi_scalar(get_row(m, index), scalar)
    return m

def sum_matrix_rows(m, row1, row2, scalar1, scalar2): 
    pass
