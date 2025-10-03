import pytest
from calculator import add, divide
def test_add():
    """Tests the add function"""
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(0,0)==0

def test_divide():
    """Tests the divide function"""
    assert divide(6,3)==2
    assert divide(5,2)==2.5
    assert divide(1,0)=="Division by zero is not allowed"

