from copy import deepcopy


def copy_need(func: callable):
    def wrapper(*args, **kwargs):
        args = list(map(deepcopy, args))
        return func(*args, **kwargs)
    return wrapper