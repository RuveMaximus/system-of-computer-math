from .decorators import same_dimension_required
from math import acos


@same_dimension_required
def plus(v1: list[float], v2: list[float]) -> list[float]: 
    """Сумма векторов"""
    return [point + v2[i] for i, point in enumerate(v1)]

@same_dimension_required
def minus(v1: list[float], v2: list[float]) -> list[float]:
    """Разность векторов"""
    return plus(v1, list(map(lambda p: -p, v2)))

@same_dimension_required
def multi(v1: list[float], v2: list[float]) -> list[float]: 
    """Скалярное произведение векторов"""
    return list(map(lambda p1, p2: p1 * p2, v1, v2))

def multi_scalar(v1: list[float], k: float) -> list[float]:
    return list(map(lambda point: point*k, v1))

def dev_scalar(v1: list[float], k: float) -> list[float]:
    return list(map(lambda point: point/k, v1))

@same_dimension_required
def is_coliniar(v1: list[float], v2: list[float]) -> bool:
    k = v1[0]/v2[0]
    for i in range(len(v1)):
        if v1[i]/v2[i] != k:
            return False
    return True

@same_dimension_required
def is_codirected(v1: list[float], v2: list[float]) -> bool:
    return is_coliniar(v1, v2) and multi(v1, v2) > 0

@same_dimension_required
def is_not_codirected(v1: list[float], v2: list[float]) -> bool:
    return not is_codirected(v1, v2)

@same_dimension_required
def is_equal(v1: list[float], v2: list[float]) -> bool:
    return is_codirected(v1, v2) and length(v1) == length(v2)

@same_dimension_required
def is_orthogonal(v1: list[float], v2: list[float]) -> bool:
    return cos(v1, v2) == 0

@same_dimension_required
def cos(v1: list[float], v2: list[float]) -> float:
    return (multi(v1, v2))/(length(v1) * length(v2))

@same_dimension_required
def angle(v1: list[float], v2: list[float]) -> float:
    """Угол между векторами в радианах"""
    return acos(cos(v1, v2))

def ration(vector: list[float], _=None) -> list[float]:
    """Нормировка вектора"""
    return dev_scalar(vector, length(vector)) 

def reverse(vector: list[float], _=None) -> list[float]:
    """Изменение направления вектора на противоположный"""
    return multi_scalar(vector, -1.0)

def length(vector: list[float], _=None):
    """Длина вектора"""
    return sum([point**2 for point in vector])**(0.5)