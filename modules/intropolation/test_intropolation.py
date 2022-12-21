from . import intropolation

def test_split_matrix():
    assert intropolation.split_matrix_with_replace([[2, 5], [6, 9]]) == ([[2, 1], [6, 1]], [5, 9])

def test_get_line_equation():
    assert intropolation.get_line_equation([[2, 5], [6, 9]]) == [1, 3]

def test_linear_intropolation():
    assert intropolation.linear_interpolation([[2, 5], [6, 9]]) == [4, 7]

def test_linear_extrapolate():
    assert intropolation.linear_extrapolate([[2, 5], [6, 9]], 1) == [1, 4]

def test_interpolate_piece_line():
    data = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    assert intropolation.interpolate_piece_line(data) == [[-2, -1], [2, 3], [3.25, 3.500000000000007], [4.75, 5.000000000000001], [6.5, 7.800000000000001]]

def test_get_basic_polynomials():
    data = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    intropolation.get_basic_polynomials(data, data[0][0], 0) == 1

def test_lagrange_interpolation_polynomial():
    data = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    for i in range(len(data)):
        assert intropolation.lagrange_interpolation_polynomial(data, data[i][0]) == data[i][1]
