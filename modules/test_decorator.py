from modules.decorators import args_copy_need


@args_copy_need
def foo(l: list):
    l[0] = [0, 0, 0]

def test_decorator():
    data = [1, 2, 3]
    foo(data)
    assert data == [1, 2, 3]