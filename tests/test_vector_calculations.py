from unittest import TestCase

from linear_algebra.vector_calculations import *
from numpy import inf


v = [5, 6, 7]
w = [1, 0, 1]

s = [2, 3, 4]
t = [1, 0, 1]

u = [3, 4]
vv = [1, 3, 1]

c = 5

class TestAdd(TestCase):
    def test_add(self):

        x = add(v, w)

        assert  x == [6,6,8]


class TestSubtract(TestCase):
    def test_subtract(self):

        x = subtract(s, t)

        assert x == [1, 3, 3]


class TestVectorsSum(TestCase):
    def test_sum(self):

        x = vector_sum([v, w, s, t])

        assert x == [9, 9, 13]


class TestScalarMultiply(TestCase):
    def test_scalar_mult(self):

        x = scalar_multiply(c, v)

        assert x == [25, 30, 35]

class TestVectorMean(TestCase):
    def test_vector_mean(self):

        x = vector_mean([v, w, s, t])

        assert x == [2.25, 2.25, 3.25]


class TestDotProduct(TestCase):
    def test_dot_product(self):

        x = dot(v, w)

        assert x == 12

class TestSumofSquares(TestCase):
    def test_sum_of_squares(self):

        x = sum_of_squares(v)

        assert x == 110

class TestMagnitude(TestCase):
    def test_magnitude(self):

        x = magnitude(u)

        assert x == 5

class TestSquaredDistance(TestCase):
    def test_squared_distance(self):

        x = squared_distance(s, t)

        assert x == 19

class TestVectorMultiply(TestCase):
    def test_vector_multiply(self):

        x = vector_multiply(v, w)

        assert x == [5, 0, 7]


class TestVectorDivision(TestCase):
    def test_vector_division(self):

        x = vector_division(v, vv)

        assert x == [5, 2, 7]

class TestVectorNorms(TestCase):
    def test_manhattan_norm(self):

        x = norm(v, 1)

        assert x == 18

    def test_euclidean_norm(self):

        x = norm(u, 2)

        assert x == 5

    def test_max_norm(self):

        x = norm(u, inf)

        assert x == 4

