from . import slae

def test_refresh_matrix(): 
    assert slae.refresh_matrix(
        [[0, 1, 4], [1, 2, 3], [0, 0, 5]]
    ) == [[1, 2, 3], [0, 1, 4], [0, 0, 5]]

def test_add_column():
    assert slae.add_column(
        [[2, 3], [4, 3]], [2, 7]
    ) == [[2, 3, 2], [4, 3, 7]]

def test_is_solution():
    assert slae.is_solution([[1, 0, 2.5], [0, 1, -1]])
    assert not slae.is_solution([[1, 2, 2.5], [0, 1, -1]])

def test_solve():
    assert slae.solve([[2, 3], [4, 3]], [2, 7]) == [2.5, -1.0]