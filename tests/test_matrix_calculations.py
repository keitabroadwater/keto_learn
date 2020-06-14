from unittest import TestCase
import pytest

from linear_algebra.matrix_calculations import *


A = [[1, 2, 3], [4, 5, 6]]

B = [[2, 2, 2], [2, 2, 2]]



C = [[5, 6, 7]]

D = [[1,2], [1,2], [1,2]]

E = [[1, 2], [3, 4]]

F = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

v = [5, 6, 7]

i = 1
a = 2
b = 2


def entry_function(i, j):
    if i == 0:
        return 2
    else:
        return 0


class TestShape(TestCase):
    def test_shape(self):

        x = shape(A)

        assert x == (2, 3)


class TestGetRow(TestCase):
    def test_get_row(self):

        x = get_row(A, i)

        assert x == [4,5,6]


class TestGetColumn(TestCase):
    def test_get_column(self):

        x = get_column(A, i)

        assert x == [2, 5]


class TestMakeMatrix(TestCase):
    def test_make_matrix(self):

        x = make_matrix(a, b, entry_function)

        assert x == [[2, 2], [0, 0]]


class TestIdentityMatrix(TestCase):
    def test_identity_matrix(self):

        x = identity_matrix(a)

        assert x == [[1, 0], [0, 1]]


class TestMatrixZeros(TestCase):
    def test_zeros(self):

        x = zeros(a, a)

        assert x == [[0, 0], [0, 0]]


class TestMatrixOnes(TestCase):
    def test_ones(self):

        x = ones(a, a)

        assert x == [[1, 1], [1, 1]]


class TestMatrixAdd(TestCase):
    def test_matrix_add(self):

        x = matrix_add(A, B)

        assert x == [[3, 4, 5], [6, 7, 8]]


class TestMatrixSubtract(TestCase):
    def test_matrix_subtract(self):

        x = matrix_subtract(A, B)

        assert x == [[-1, 0, 1], [2, 3, 4]]


class TestMatrixMultHadamard(TestCase):
    def test_matrix_mult_hadamard(self):
        x = matrix_mult_hadamard(A, B)

        assert x == [[2, 4, 6], [8, 10, 12]]


class TestMatrixVectortoMatrix(TestCase):
    def test_vector_to_matrix(self):
        x = vector_to_matrix(v)

        assert x == [[5, 6, 7]]


class TestMatrixMatrixtoVector(TestCase):
    def test_matrix_to_vector(self):
        x = matrix_to_vector(C)

        assert x == [5, 6, 7]

class TestMatrixDotProduct(TestCase):
    def test_dot_product(self):
        x = dot_product(A, D, 'matrix')

        y = dot_product(A, v, 'vector')

        z = dot_product(A, a, 'scalar')

        assert x == [[6, 12], [15, 30]]
        assert y == [38, 92]
        assert z == [[2, 4, 6], [8, 10, 12]]


class TestTranspose(TestCase):
    def test_transpose(self):
        x = transpose(A)

        assert x == [[1, 4], [2, 5], [3, 6]]


class TestSquare(TestCase):
    def test_square(self):
        x = square(A)
        y = square(E)

        assert x == False
        assert y == True

class TestDeterminant(TestCase):
    def test_determinant_square_matrix(self):
        x = determinant(E)
        y = determinant(F)

        assert x == -2
        assert y == pytest.approx(-9.51619735392994e-16)

    def test_determinant_nonsquare_matrix(self):

        with pytest.raises(Exception):
            x = determinant(A)


class TestAdjoint(TestCase):
    def test_adjoint(self):
        x = adjoint(E)

        assert x == [[4, -2], [-3, 1]]


class TestMatrixDivision(TestCase):
    def test_matrix_division(self):

        x = matrix_division(B, B, 'matrix')
        y = matrix_division(B, -b, 'scalar')

        assert x == [[1, 1, 1], [1, 1, 1]]
        assert y == [[-1.0, -1.0, -1.0], [-1.0, -1.0, -1.0]]



class TestInverse(TestCase):
    def test_inverse(self):
        x = inverse(E)

        assert x == [ [-2, 1 ] , [3/2,  -1/2]]