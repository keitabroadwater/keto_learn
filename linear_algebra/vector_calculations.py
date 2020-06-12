"""
Basic Vector Calculations:

The basis for these calculation is the python list. So, this is only for insight and education, not performance.
"""

from typing import List
from math import sqrt
from numpy import inf

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:

    """Adds vectors element-wise"""

    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:

    """Subtracts vectors element-wise"""

    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:

    """ Sum all corresponding elements"""

    # Check that vectors is not empty

    assert vectors, "No vectors given"

    # Check that vectors are the same size

    number_of_elements = len(vectors[0])
    assert all(number_of_elements == len(v) for v in vectors), "vectors are not the same size"

    # the i-th element of the result is the sum of every vector[i]

    return [sum(vector[i] for vector in vectors)
            for i in range(number_of_elements)]


def scalar_multiply(c: float, v:Vector) -> Vector:

    """ Multiplies every element by c"""

    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:

    """Computes the element-wise average"""

    # Ensure lists are same length

    length_vector = len(vectors[0])
    number_of_vectors = len(vectors)
    assert all([len(vectors[i]) == length_vector for i in range(len(vectors))]), "vectors are not the same size"

    # For every index, get the element of each vector

    averages = []
    for idx in range(length_vector):
        temp_mean = []
        for vect in vectors:
            temp_mean.append(vect[idx])

        temp_mean = sum(temp_mean)/number_of_vectors*1.0
        averages.append(temp_mean)

    return averages


def dot(v: Vector, w: Vector) -> float:

    """computes v_1 * w_1 + v_2 * w_2 + ... v_n * w_n"""

    return sum([v_i * w_i for v_i, w_i in zip(v, w)])


def sum_of_squares(v: Vector) -> float:

    """Returns v_1 * v_1  +  v_2 * v_2  +  ....  v_n * v_n"""

    return dot(v,v)


def magnitude(v: Vector) -> float:

    """Returns the magnitude (or length) of v; which is the square root of the sum of squares"""

    return sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:

    """Computes (v_1 - w_1) ** 2 + ... + (v_n -w_n) ** 2"""

    return sum_of_squares(subtract(v, w))


def vector_multiply(v: Vector, w: Vector) -> Vector:

    """Element-wise multiplication of vectors"""

    return [v_i * w_i for v_i, w_i in zip(v, w)]


def vector_division(v: Vector, w: Vector) -> Vector:

    """Element-wise division of vectors"""

    # check for zero divisors

    assert (0 in w) == False, "zero in divisor vector!"

    return [v_i / w_i for v_i, w_i in zip(v, w)]


def norm(v: Vector, norm_type: float) -> float:

    """Computes the norm of a vector, given a the desired type:
        L1 or manhattan Norm = 1
        L2 or euclidean Norm = 2
        Linf or max Norm = inf"""

    if norm_type == 1:

        return sum([abs(x) for x in v])

    if norm_type == 2:

        return sqrt(sum([x**2 for x in v]))

    if norm_type == inf:

        return max([abs(x) for x in v])


