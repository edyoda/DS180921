# RUNNING THE TEST CASES USING STRING MATCHING APPROACH
import pytest
def func(x):
    if x%2 == 0:
        return x+5
    else:
        return x-5
        
def test_pavan():
    assert func(3) == 8

def test_rajitha():
    assert func(4) == 10

def test_rajitha_1():
    assert func(8) == 13
    
def test_aditya():
    assert func(10) == 15