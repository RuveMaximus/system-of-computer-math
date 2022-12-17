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

def test_inverse_matrix(): 
    m = slae.attach_unit_matrix([[1, 2], [3, 4]])
    m = slae.inverse_matrix(m)
    assert [row[len(m)//2+1:] for row in m] == [[-2, 1], [1.5, -0.5]]

def test_solve():
    assert slae.solve([[2, 3], [4, 3]], [2, 7]) == [2.5, -1.0]
    assert slae.solve([[-1, 2, 6], [3, -6, 0], [1, 0, 6]], [15, -9, 5]) == [-7, -2, 2]

def test_solve_by_inverse_matrix(): 
    assert slae.solve_by_inverse_matrix([[1, 2], [3, 4]], [6, 8]) == [-4, 5]