from copy import deepcopy


def args_copy_need(func: callable):
    def wrapper(*args, **kwargs):
        args = deepcopy(args)
        kwargs = deepcopy(kwargs)

        return func(*args, **kwargs)
    return wrapper