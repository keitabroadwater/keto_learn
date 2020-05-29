from unittest import TestCase
from linear_algebra.vector_calculations import add

v = [5, 6, 7]
w = [1, 0, 1]

class TestAdd(TestCase):
    def test_add(self):

        x = add(v, w)

        assert  x == [6,6,8]