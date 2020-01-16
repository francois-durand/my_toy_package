import pytest
from my_toy_package import MyClass1


def test():
    with pytest.raises(ValueError):
        my_object = MyClass1(a=-1, b=42)
    my_object = MyClass1(a=2, b=3)
    assert repr(my_object) == 'MyClass1(a=2, b=3)'
    assert str(my_object) == '(a, b) = 2, 3'
    assert my_object.a_square == 4
