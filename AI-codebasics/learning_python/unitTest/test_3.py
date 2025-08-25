import pytest

def multiply(a,b):
    return a**b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

def test_multiply():
    assert multiply(3,2) == 6
    assert multiply(0,5) == 0
    assert multiply(-1,5) == -5
    
def test_divide():
    assert divide(10,2) == 5
    
    with pytest.raises(ValueError):
        divide(10,0)
    
    
    # error Output

    """(venv) mohitrajnayak@Mohits-MacBook-Pro unitTest % pytest -v test_3.py      
================================================================================== test session starts ==================================================================================
platform darwin -- Python 3.11.9, pytest-8.4.1, pluggy-1.6.0 -- /Users/mohitrajnayak/Data Sci Work/Data Sci REPO/Machine-Learning/venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/mohitrajnayak/Data Sci Work/Data Sci REPO/Machine-Learning/AI-codebasics/unitTest
plugins: anyio-4.10.0
collected 2 items                                                                                                                                                                       

test_3.py::test_multiply FAILED                                                                                                                                                   [ 50%]
test_3.py::test_divide PASSED                                                                                                                                                     [100%]

======================================================================================= FAILURES ========================================================================================
_____________________________________________________________________________________ test_multiply _____________________________________________________________________________________

    def test_multiply():
>       assert multiply(3,2) == 6
E       assert 9 == 6
E        +  where 9 = multiply(3, 2)

test_3.py:12: AssertionError
================================================================================ short test summary info ================================================================================
FAILED test_3.py::test_multiply - assert 9 == 6
============================================================================== 1 failed, 1 passed in 0.02s ==============================================================================
    """