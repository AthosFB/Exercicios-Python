from collections.abc import Iterator


def arange(*args: float) -> Iterator[float]:
    """Generates a range of floating point values.

    :param args: stop or start[, stop[, step]]
    :return: The iterator of range values.
    """
    if not args:
        raise ValueError('Not enough arguments')
    if len(args) == 1:
        yield from arange(0, args[0])
    elif len(args) == 2:
        yield from arange(args[0], args[1], 1)
    else:
        start, stop, step = args

        while start < stop:
            yield start
            start += step


def linspace(start: float, stop: float, n: float) -> Iterator[float]:
    """Generates an iterator of values from start to stop with length of n.

    :param start: The start value.
    :param stop: The stop value.
    :param n: The number of values, defaults to 100.
    :return: The linspace of arguments.
    """
    return arange(start, stop, (stop - start) / n)


def series_sum(*args: int) -> int:
    """Calculates the series sum of the interval.

    :param args: stop or start[, stop[, n]]
    :return: the series sum.
    """
    if not args:
        raise ValueError('Not enough arguments')
    if len(args) == 1:
        return series_sum(0, args[0])
    elif len(args) == 2:
        return series_sum(args[0], args[1], abs(args[1] - args[0]) + 1)
    else:
        start, stop, n = args

        return (start + stop) * n // 2
