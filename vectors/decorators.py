def same_dimension_required(func: callable):
    def check_vectors(v1, v2):
        if len(v1) != len(v2):
            raise ValueError("Размерности векторов не совпадают!")
        return func(v1, v2)
    return check_vectors