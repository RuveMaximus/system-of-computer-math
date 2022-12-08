from modules.matrices import matrix

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


def solve(m: list, result_column: list):
    m = add_column(m, result_column)

    print(m)


    return [row[-1] for row in m]
