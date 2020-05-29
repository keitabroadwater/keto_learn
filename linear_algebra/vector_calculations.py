"""
Basic Vector Calculations:

The basis for these calculation is the python list. So, this is only for insight and education, not performance.
"""


from typing import List


Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:

    """Adds vectors element-wise"""

    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:

    """Subtracts vectors element-wise"""

    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v,w)]


def vector_sum(vectors: List[Vector]) -> Vector:

    """ Sum all corresponding elements"""

    # Check that vectors is not empty

    assert vectors, "No vectors given"

    # Check that vectors are the same size

    number_of_elements = len(vectors[0])
    assert all(number_of_elements == len(v) for v in vectors), "vectors are not the same size"

    # the i-th element of the result is the sum of every vector[i]

    return [sum(vector[i] for vector in vectors)   \
            for i in range(number_of_elements)]

def scalar_multiply(c: float, v:Vector) -> Vector:

    """ Multiplies every element by c"""

    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:

    """Computes the element-wise average"""

    return sum[]


def dot(v: Vector, w: Vector) -> float:

    """computes v_1 * w_1 + v_2 * w_2 + ... v_n * w_n"""



def sum_of_squares(v: Vector) -> float:

    """Returns v_1 * v_1 + v_2 * v_2 + .... v_n * v_n"""

def magnitude(v: Vector) -> float:

    """Returns the magnitude (or length) of v"""


def squared_distance(v: Vector, w: Vector) -> float:

    """Computes (v_1 - w_1) ** 2 + ... + (v_n -w_n) ** 2"""

def euclidean_distance(v: Vector, w: Vector) -> float:

    """Computes the euclidean distance between v and w"""

