from unittest import TestCase
from linear_algebra.vector_calculations import subtract

v = [2, 3, 4]
w = [1, 0, 1]

class TestSubtract(TestCase):
    def test_subtract(self):

        x = subtract(v, w)

        assert x == [1, 3, 3]