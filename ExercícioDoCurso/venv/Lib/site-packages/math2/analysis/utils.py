from collections.abc import Sequence


def interpolate(x: float, x_values: Sequence[float], y_values: Sequence[float]) -> float:  # TODO: MAKE GENERIC
    """Interpolates the point between two given points.

    :param x: The point to interpolate.
    :param x_values: The x coordinates.
    :param y_values: The x coordinates.
    :return: The interpolated value.
    """
    return (x - x_values[0]) / (x_values[-1] - x_values[0]) * (y_values[-1] - y_values[0]) + y_values[0]
