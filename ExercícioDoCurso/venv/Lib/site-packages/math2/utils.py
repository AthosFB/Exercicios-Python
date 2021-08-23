from collections.abc import Collection, Hashable, Iterable, Iterator, Sequence
from functools import reduce
from itertools import chain
from operator import mul
from typing import Any, Optional, cast

from math2.typing import SupportsLessThan, _SLT, _SM, _T


def windowed(it: Iterable[_T], width: int, step: int = 1, partial: bool = False) -> Iterator[Iterator[_T]]:
    """Returns the sliding window views of the supplied iterable.

    :param it: The values to generate the window views on.
    :param width: The sliding window width.
    :param step: The step of the window views.
    :param partial: Allow partial view.
    :return: The window views.
    """
    if isinstance(it, Sequence):
        return (iter(it[i:i + width]) for i in range(0, len(it) if partial else len(it) - width + 1, step))
    else:
        return windowed(tuple(it), width, step, partial)


def chunked(it: Iterable[_T], width: int) -> Iterator[Iterator[_T]]:
    """Chunks the iterable by the given width.

    :param it: The iterable to chunk.
    :param width: The width of the chunks.
    :return: The chunks.
    """
    return windowed(it, width, width, True)


def trimmed(it: Iterable[_T], percentage: float) -> Iterator[_T]:
    """Trims the iterable by the percentage.

    :param it: The values to trim.
    :param percentage: The trimmed percentage.
    :return: The trimmed sequence.
    """
    if isinstance(it, Sequence):
        n = int(len(it) * percentage)

        return iter(it[n:len(it) - n])
    else:
        return trimmed(tuple(it), percentage)


def rotated(it: Iterable[_T], index: int) -> Iterator[_T]:
    """Rotates the iterable by the given index.

    :param it: The values to rotate.
    :param index: The index of rotation.
    :return: The rotated iterator.
    """
    return chain(it[index:], it[:index]) if isinstance(it, Sequence) else rotated(tuple(it), index)


def after(it: Iterable[_T], v: _T, loop: bool = False) -> _T:
    """Gets the next the value inside the iterable.

    :param it: The iterator to get from.
    :param v: The previous value.
    :param loop: True to allow loop-around, else False.
    :return: The next value.
    """
    if isinstance(it, Sequence):
        try:
            i = (it.index(v) + 1)

            if loop:
                i %= len(it)

            return cast(_T, it[i])
        except IndexError:
            raise ValueError('Last element')
    else:
        return after(tuple(it), v, loop)


def iter_equal(it1: Iterable[Any], it2: Iterable[Any]) -> bool:
    """Checks if all elements in both iterables are equal to the elements in the other iterable at the same position.

    :param it1: The first iterable.
    :param it2: The second iterable.
    :return: True if the equality check passes, else False.
    """
    if isinstance(it1, Collection) and isinstance(it2, Collection):
        return len(it1) == len(it2) and all(x == y for x, y in zip(it1, it2))
    elif isinstance(it1, Collection):
        return iter_equal(it1, tuple(it2))
    elif isinstance(it2, Collection):
        return iter_equal(tuple(it1), it2)
    else:
        return iter_equal(tuple(it1), tuple(it2))


def const(it: Iterable[Any]) -> bool:
    """Checks if all elements inside the iterable are equal to each other.

       If the iterable is empty, True is returned.

    :param it: The iterable.
    :return: True if all elements are equal, else False.
    """
    it = iter(it)

    try:
        x = next(it)
    except StopIteration:
        return True
    else:
        return all(x == y for y in it)


def unique(it: Iterable[Any]) -> bool:
    """Checks if all elements inside the iterable are unique to each other.

       If the iterable is empty, True is returned.

    :param it: The iterable.
    :return: True if all elements are unique, else False.
    """
    if isinstance(it, Sequence):
        if not it:
            return True
        elif isinstance(it[0], Hashable):
            return len(it) == len(set(it))
        elif isinstance(it[0], SupportsLessThan):
            return all(x != y for x, y in windowed(it, 2))
        else:
            return all(all(it[i] != it[j] for j in range(len(it)) if i != j) for i in range(len(it)))
    else:
        return unique(tuple(it))


def empty(it: Iterable[Any]) -> bool:
    """Checks if the iterable is empty.

    :param it: The iterable to check.
    :return: True if the iterable is empty, else False.
    """
    try:
        next(iter(it))

        return False
    except StopIteration:
        return True


def bind(value: _SLT, lower: _SLT, upper: _SLT) -> _SLT:
    """Binds the value by the given interval.

    :param value: The value to be bound.
    :param lower: The lower limit.
    :param upper: The upper limit.
    :return: The bound value.
    """
    if upper < lower:
        raise ValueError('Lower bound is greater than the upper bound')
    elif value < lower:
        return lower
    elif upper < value:
        return upper
    else:
        return value


def product(values: Iterable[_SM], start: Optional[_SM] = None) -> _SM:
    """Calculates the product of the elements in the iterable.

    :param values: The values to be multiplied.
    :param start: The optional start value.
    :return: The product of the values.
    """
    try:
        return reduce(mul, values if start is None else chain((start,), values))
    except TypeError:
        raise ValueError('Invalid iterable')


def next_or_none(it: Iterator[_T]) -> Optional[_T]:
    """Tries to get the next element of the iterator.

    :param it: The iterator to consume.
    :return: None if there is no next element, else the next element.
    """
    try:
        return next(it)
    except StopIteration:
        return None


def default(optional: Optional[_T], default_: _T) -> _T:
    """Checks if the value is not None and returns it or the default value.

    :param optional: The optional value.
    :param default_: The default value.
    :return: The default value if the value to check is None, else the checked value.
    """
    return default_ if optional is None else optional


def get(optional: Optional[_T]) -> _T:
    """Checks if the optional value is not none and returns it.

    :param optional: The optional value.
    :return: The checked value.
    """
    if optional is None:
        raise ValueError('The checked value is None')
    else:
        return optional
