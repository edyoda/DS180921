import pytest
def func(x):
    if x%2 == 0:
        return x+5
    else:
        return x-5

@pytest.mark.pavan        
def test_1():
    assert func(3) == 8
    
@pytest.mark.rajitha
def test_2():
    assert func(4) == 10
@pytest.mark.rajitha
def test_3():
    assert func(8) == 13

@pytest.mark.aditya
def test_4():
    assert func(10) == 15
    