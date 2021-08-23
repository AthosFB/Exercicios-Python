from math2.linalg.tensors import Matrix, Vector


def solve(m: Matrix, y: Vector) -> Vector:
    """Solves Mx = y for x.

    :param m: The matrix M.
    :param y: The product y.
    :return: The factor x.
    """
    if not m:
        return Vector(())
    elif len(m) == 1:
        return Vector((y[0] / m[0][0],))
    elif len(m) == 2:
        x = [0.0, 0.0]
        x[1] = (m[1][0] * y[0] - m[0][0] * y[1]) / (m[0][1] * m[1][0] - m[0][0] * m[1][1])
        x[0] = (y[0] - m[0][1] * x[1]) / m[0][0]

        return Vector(x)
    else:
        raise NotImplementedError  # TODO: ACCEPT GENERAL MATRICES
