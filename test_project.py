from project import *

def test_multiplication():
    a=[[1,2],[3,4]]
    b=[[4,5],[6,7]]
    assert multiplication(a,b)==[[16,19],[36,43]]
    c=[[1,2],[3,4]]
    d=[[5],[6]]
    assert multiplication(c,d)==[[17],[39]]

def test_determinant():
    a=[[1,2],[3,4]]
    assert determinant(a)==-2


def test_deepcopy():
    a=[[1,9],[3,4]]
    assert (a is deepcopy(a))==False

def test_cofactor():
    a=[[1,2,3],[4,5,6],[7,8,9]]
    assert cofactor(a,0,0)==[[5,6],[8,9]]

def test_adjoint():
    a=[[1,2,3],[4,5,6],[7,8,9]]
    assert adjoint(a)==[[-3,6,-3],[6,-12,6],[-3,6,-3]]

def test_transpose():
    a=[[-3,6,-3],[6,-12,6],[-3,6,-3]]
    assert transpose(a)==a

