from unittest import TestCase
from linear_algebra.vector_calculations import add
from linear_algebra.vector_calculations import subtract


v = [5, 6, 7]
w = [1, 0, 1]

s = [2, 3, 4]
t = [1, 0, 1]

class TestAdd(TestCase):
    def test_add(self):

        x = add(v, w)

        assert  x == [6,6,8]


class TestSubtract(TestCase):
    def test_subtract(self):

        x = subtract(s, t)

        assert x == [1, 3, 3]