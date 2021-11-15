#pytest -> Third party open source module

def func(x):
    if x%2 == 0:
        return x+5
    else:
        return x-5
        
def test_method():
    assert func(3) == 8

def test_method_1():
    assert func(4) == 7
    
def test_method_2():
    assert func(4) == 9