from decorators import same_dimension_required


@same_dimension_required
def plus(v1: list[float], v2: list[float]) -> list: 
    """
    :param v1: Список точек первого вектора
    :param v2: Список точек второго вектора

    :return: Список точек вектора, полученного при v1 + v2
    """
    return [point + v2[i] for i, point in enumerate(v1)]

@same_dimension_required
def minus(v1: list[float], v2: list[float]) -> list:
    """
    :param v1: Список точек первого вектора
    :param v2: Список точек второго вектора

    :return: Список точек вектора, полученного при v1 - v2
    """
    return plus(v1, list(map(lambda p: -p, v2)))

@same_dimension_required
def multi(v1: list[float], v2: list[float]) -> list: 
    """
    :param v1: Список точек первого вектора
    :param v2: Список точек второго вектора

    :return: Скалярное произведение v1 и v2
    """
    return list(map(lambda p1, p2: p1 * p2, v1, v2))

def multi_scalar(v1: list[float], k: float) -> list:
    return list(map(lambda point: point*k, v1))

def dev_scalar(v1: list[float], k: float) -> list:
    return list(map(lambda point: point/k, v1))

@same_dimension_required
def coliniar(v1: list[float], v2: list[float]) -> bool:
    k = v1[0]/v2[0]
    for i in range(len(v1)):
        if v1[i]/v2[i] != k:
            return False
    return True

def length(vector: list[float]): 
    return sum([point**2 for point in vector])**(0.5)