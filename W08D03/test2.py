def func(x):
    if x == 'Rajitha':
        return True
        
def test_method():
    assert func('Pavan') == True

def test_method_1():
    assert func('Rajitha') == False
    
def test_method_2():
    assert func('Rajitha') == True

    