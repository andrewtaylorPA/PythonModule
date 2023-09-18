import pytest
from programs import factorial

def test_fact():
    assert factorial.fact(0) == 1

def test_fact():
    assert factorial.fact(3) == 6