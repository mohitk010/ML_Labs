import pytest
import sys
sys.path.append('../src')
import calculator
# from src import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(5,0) == 5
    assert calculator.add (-1, 1) == 0
    assert calculator.add (-1, -1) == -2


def test_substract():
    assert calculator.substract(2, 3) == -1
    assert calculator.substract(5,0) == 5
    assert calculator.substract (-1, 1) == -2
    assert calculator.substract (-1, -1) == 0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(5,0) == 0
    assert calculator.multiply (-1, 1) == -1
    
    assert calculator.multiply (-1, -1) == 1

def add_3_nums():
    assert calculator.add_3_nums(2, 3, 5) == 10
    assert calculator.add_3_nums(5,0, -1) == 4
    assert calculator.add_3_nums (-1, -1, -1) == -3
    
    assert calculator.add_3_nums (-1, -1, 100) == 98
    