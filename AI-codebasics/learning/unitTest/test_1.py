def add(x,y):
    return x+y

def test_add():
    assert add(2,3) == 5
    assert add(-1, -3) == -4
    
def test_add_big_number():
    assert add(200000,300000) == 500000