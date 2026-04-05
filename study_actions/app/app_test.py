from app import add

def test_add():
    assert add([2, 3]) == 5
    assert add([-1, 1]) == 0
    assert add([0, 0]) == 0
    assert add([2, 3, 1]) == 6
    assert add([-1, 1, 1]) == 1
    assert add([0, 0, 0]) == 0
    
    
test_add()