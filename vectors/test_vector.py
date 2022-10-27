from random import randint, random
from math import pi
from vectors import vector

def get_vector(*args, rand_func: callable, size=None):
    """генерация вектора"""
    return [rand_func(*args) for i in range(size if size else 4)]


def test_vector():
    v1 = get_vector(-100, 100, rand_func=randint)
    v2 = get_vector(-10, 10, rand_func=randint)

    scalar = randint(1, 100)

    print(f'{v1=}\n{v2=}')
    
    assert vector.plus(v1, v2) == [ v1[i] + v2[i] for i in range(len(v1)) ]
    assert vector.minus(v1, v2) == [ v1[i] - v2[i] for i in range(len(v1)) ]
    assert vector.multi(v1, v2) == [ v1[i] * v2[i] for i in range(len(v1)) ]
    assert vector.angle([2, 2], [2, -2]) == pi / 2
    assert vector.cos([0, 1], [1, 0]) == 0

    assert vector.multi_scalar(v1, scalar) == [ point * scalar for point in v1 ]
    assert vector.dev_scalar(v1, scalar) == [point / scalar for point in v1]

    assert vector.is_equal([1, 2], [1, 2])
    assert vector.is_coliniar([1, 2], [1, 2])
    assert vector.is_codirected([1, 2], [2, 4])
    assert vector.is_not_codirected([1, 2], [3, 4])
    assert vector.is_orthogonal([0, 2], [2, 0])

    assert vector.reverse(v1) == [-point for point in v1]
    assert vector.ration([0, 10]) == [0, 1]
    assert vector.length([3, 4]) == 5