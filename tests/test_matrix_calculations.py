from unittest import TestCase

from linear_algebra.matrix_calculations import *


A = [[1, 2, 3], [4, 5, 6]]

B = [[2, 2, 2], [2, 2, 2]]

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



def vector_to_matrix():
    pass

def matrix_to_vector():
    pass

def dot_product():
    pass

