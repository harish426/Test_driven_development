import pytest
from sparse_recommender import SparseMatrix

def test_set_get():
    matrix = SparseMatrix(3, 3)
    #setting values
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    matrix.set(2, 2, 3)
    #getting values
    assert matrix.get(1, 0) == 0  
    assert matrix.get(0, 0) == 1
    assert matrix.get(1, 1) == 2
    assert matrix.get(2, 2) == 3
    
#testing recommend method
def test_recommend():
    matrix = SparseMatrix(3, 3)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    matrix.set(2, 2, 3)
    vector = [1, 0, 0]
    result = matrix.recommend(vector)
    assert result == [1, 0, 0]
    vector2 = [0, 1, 0]
    #Testing recommend with a different vector
    result2 = matrix.recommend(vector2)
    assert result2 == [0, 2, 0]

# Test adding two matrices
def test_add_Movie():
    matrix1 = SparseMatrix(3, 3)
    matrix1.set(1, 0, 1)
    matrix1.set(1, 1, 2)
    matrix1.set(2, 2, 3)
    matrix2 = SparseMatrix(3, 3)
    matrix2.set(0, 0, 2)
    matrix2.set(1, 1, 3)
    matrix2.set(2, 2, 4)
    result = matrix1.add_Movie(matrix2)
    assert result.get(0, 1) == 0 
    assert result.get(1, 0) == 1
    assert result.get(1, 1) == 5
    assert result.get(2, 2) == 7

# Testing converting to a dense matrix
def test_to_dense():
    matrix = SparseMatrix(2, 2)
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(1, 1, 3)
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[1, 2], [0, 3]]

# Test setting and getting with invalid indices
def test_invalid():
    matrix = SparseMatrix(3, 3)
    with pytest.raises(ValueError):
        matrix.set(4, 0, 1)
    with pytest.raises(ValueError):
        matrix.get(0, 4)
    with pytest.raises(ValueError):
        matrix.recommend([1, 0, 0, 1])
