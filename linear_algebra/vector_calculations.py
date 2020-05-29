"""
Basic Vector Calculations:


"""


from typing import List


Vector = List(float)

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