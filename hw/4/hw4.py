#Abhishek Yadav
#I pledge my honor to abide by the Stevens Honor Code
#9/28/19

def pascal_row(n):
    '''
        assume n >= 0
        returns the nth row of pascals triangle
    '''
    def sums(L):
        if len(L) == 1:
            return []
        return [L[0] + L[1]] + sums(L[1:])
    
    if n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    return [1] + sums(pascal_row(n-1)) + [1]


def pascal_triangle(n):
    '''
        assume n >= 0
        Returns nth index rows of pascals triangle in a list
    '''
    if n == 0:
        return [pascal_row(0)]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]


def test_pascal_row():
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]


def test_pascal_triangle():
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
