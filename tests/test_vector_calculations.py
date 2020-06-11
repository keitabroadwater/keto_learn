from unittest import TestCase

from linear_algebra.vector_calculations import add, subtract, vector_sum, scalar_multiply, vector_mean, dot, sum_of_squares, magnitude

v = [5, 6, 7]
w = [1, 0, 1]

s = [2, 3, 4]
t = [1, 0, 1]

u = [3, 4]

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