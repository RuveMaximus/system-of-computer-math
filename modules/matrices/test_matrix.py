from . import matrix

def test_summ(): 
    assert matrix.summ(
        [[1, 2, 3], [2, 3 ,4], [3, 4, 5]], 
        [[2, 3, 4], [3, 4, 5],  [4, 5, 6]]
    ) == [[3, 5, 7], [5, 7, 9], [7, 9, 11]]

def test_dif(): 
    assert matrix.dif(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ) == [[0,0,0], [0,0,0], [0,0,0]]

def test_transposition():
    assert matrix.transposition([
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ]) == [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9] 
    ]

def test_multiply(): 
    assert matrix.multiply(
        [[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10]]
    ) == [[25, 28], [57, 64], [89, 100]]

def test_scalar_multiply():
    assert matrix.scalar_multiply(
        [[1, 2, 3], [4, 5, 6]], 2
    ) == [[2, 4, 6], [8, 10, 12]]

def test_scalar_dif():
    assert matrix.scalar_dif(
        [[2, 4, 6], [8, 10, 12]], 2
    ) == [[1, 2, 3], [4, 5, 6]]

def test_get_row():
    assert matrix.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [4, 5, 6]

def test_get_col(): 
    assert matrix.get_col([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [2, 5, 8]

def test_swap_rows():
    assert matrix.swap_rows([[1, 1], [2, 2], [3, 3]], [0, 2]) == [[3, 3], [2, 2], [1, 1]]

def test_multiply_row_by_scalar(): 
    assert matrix.multiply_row_by_scalar([[1, 2, 3], [4, 5, 6]], 0, 3) == [[3, 6, 9], [4, 5, 6]]

def test_dif_row_by_scalar(): 
    assert matrix.dif_row_by_scalar([[3, 6, 9], [4, 5, 6]], 0, 3) == [[1, 2, 3], [4, 5, 6]]

def test_sum_matrix_rows(): 
    assert matrix.sum_matrix_rows(
        [[3, 3, 3], [1, 2, 3], [1, 1, 1]], [0, 2], [1, -3]
    ) == [[0, 0, 0], [1, 2, 3], [1, 1, 1]]