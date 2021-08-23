from collections.abc import Iterable, MutableSequence


class Vector(MutableSequence[float]):
    def __init__(self, it: Iterable[float]):
        self.__values = list(it)

    def __getitem__(self, i):
        return self.__values[i] if isinstance(i, int) else Vector(self.__values[i])

    def __setitem__(self, i, o):
        self.__values[i] = o

    def __delitem__(self, i):
        del self.__values[i]

    def __len__(self):
        return len(self.__values)

    def __pos__(self):
        return Vector(self)

    def __neg__(self):
        return Vector(-x for x in self)

    def __add__(self, other):
        try:
            if len(other := tuple(other)) != len(self):
                raise ValueError('Unequal lengths between operands')

            return Vector(x + y for x, y in zip(self, other))
        except TypeError:
            return NotImplemented

    def __sub__(self, other):
        try:
            if len(other := tuple(other)) != len(self):
                raise ValueError('Unequal lengths between operands')

            return Vector(x - y for x, y in zip(self, other))
        except TypeError:
            return NotImplemented

    def __mul__(self, other):
        try:
            return Vector(x * other for x in self)
        except TypeError:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        try:
            return Vector(x / other for x in self)
        except TypeError:
            return NotImplemented

    def __matmul__(self, other):
        try:
            if len(other := tuple(other)) != len(self):
                raise ValueError('Unequal lengths between operands')

            return sum(x * y for x, y in zip(self, other))
        except TypeError:
            return NotImplemented

    def __iadd__(self, other):
        self.__values = (self + other).__values

        return self

    def insert(self, index, value):
        self.__values.insert(index, value)


class Matrix(MutableSequence[Vector]):
    def __init__(self, it: Iterable[Iterable[float]]):
        self.__values = list(map(Vector, it))

    def __getitem__(self, i):
        return self.__values[i] if isinstance(i, int) else Matrix(self.__values[i])

    def __setitem__(self, i, o):
        self.__values[i] = Vector(o) if isinstance(i, int) else map(Vector, o)

    def __delitem__(self, i):
        del self.__values[i]

    def __len__(self):
        return len(self.__values)

    def __pos__(self):
        return Matrix(self)

    def __neg__(self):
        return Matrix(-x for x in self)

    def __add__(self, other):
        try:
            if len(other := tuple(other)) != len(self):
                raise ValueError('Unequal lengths between operands')

            return Matrix(x + y for x, y in zip(self, other))
        except TypeError:
            return NotImplemented

    def __sub__(self, other):
        try:
            if len(other := tuple(other)) != len(self):
                raise ValueError('Unequal lengths between operands')

            return Matrix(x - y for x, y in zip(self, other))
        except TypeError:
            return NotImplemented

    def __mul__(self, other):
        try:
            if isinstance(other, Matrix):
                if not len(self) or len(self[0]) != len(other):
                    raise ValueError('Unequal lengths between operands')

                other = transposed(other)

                return Matrix((row @ col for col in other) for row in self)
            elif isinstance(other, Iterable):
                other = Vector(other)

                if not len(self) or len(self[0]) != len(other):
                    raise ValueError('Unequal lengths between operands')

                return Matrix((row @ other) for row in self)
            else:
                return Matrix(x * other for x in self)
        except TypeError:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        try:
            return Matrix(x / other for x in self)
        except TypeError:
            return NotImplemented

    def __matmul__(self, other):
        try:
            if len(other := tuple(other)) != len(self):
                raise ValueError('Unequal lengths between operands')

            return sum(x @ y for x, y in zip(self, other))
        except TypeError:
            return NotImplemented

    def __iadd__(self, other):
        self.__values = (self + other).__values

        return self

    def insert(self, index, value):
        self.__values.insert(index, Vector(value))


def full(size: int, value):
    """Constructs a vector of size filled with the given value.

    :param size: The size of the vector.
    :param value: The fill value.
    :return: The constructed vector.
    """
    return Vector(value for _ in range(size))


def zeros(size: int):
    """Constructs a vector of size filled with zeros.

    :param size: The size of the vector.
    :return: The constructed vector.
    """
    return full(size, 0)


def ones(size: int):
    """Constructs a vector of size filled with ones.

    :param size: The size of the vector.
    :return: The constructed vector.
    """
    return full(size, 1)


def deleted(vec, index):
    """Returns the copied version of the supplied vector that has a value deleted.

    :param vec: The vector to delete.
    :param index: The index of deletion.
    :return: The deleted vector.
    """
    vec = Vector(vec)
    del vec[index]

    return vec


def inserted(vec, index, value):
    """Returns the copied version of the supplied vector that has a value inserted.

    :param vec: The vector to insert.
    :param index: The index of insertion.
    :param value: The value to insert with.
    :return: The inserted vector.
    """
    vec = Vector(vec)
    vec.insert(index, value)

    return vec


def replaced(vec, index, value):
    """Returns the copied version of the supplied vector that has a value replaced.

    :param vec: The vector to replace.
    :param index: The index of replacement.
    :param value: The value to replace with.
    :return: The replaced vector.
    """
    vec = Vector(vec)
    vec[index] = value

    return vec


def transposed(mat):
    """Transposes the supplied matrix.

    :param mat: The matrix to transpose.
    :return: The transposed matrix.
    """
    return Matrix((mat[j][i] for j in range(len(mat[i]))) for i in range(len(mat)))
