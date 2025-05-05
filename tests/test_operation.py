## Importing both math operations from src folder 

from src.math_operations import add, sub

def test_add():    ##Function contaning test cases 
    assert add(2,3)== 5  ##Test case to check whether it is working
    assert add(-1,1)==0
     

def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0