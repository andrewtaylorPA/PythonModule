def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

print(list_of_squares(10))


import pytest
from programs import list_of_squares

def test_list_of_squares():
    assert list_of_squares.list_of_squares(0) == 1

def test_list_of_squares():
    assert list_of_squares.list_of_squares(3) == {1: 1, 2: 4, 3: 9}