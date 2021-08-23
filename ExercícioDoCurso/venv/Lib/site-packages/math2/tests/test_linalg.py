from operator import add, matmul, sub
from unittest import main

from math2.linalg import Matrix, Vector, full, ones, replaced, solve, zeros
from math2.tests import ExtendedTestCase


class VectorTestCase(ExtendedTestCase):
    def test_init(self):
        self.assertIterableAlmostEqual(Vector(range(10)), range(10))

        self.assertIterableAlmostEqual(zeros(10), (0,) * 10)
        self.assertIterableAlmostEqual(ones(10), (1,) * 10)
        self.assertIterableAlmostEqual(full(10, 1 / 3), (1 / 3,) * 10)
        self.assertIterableAlmostEqual(replaced(ones(10), 5, 0), (1,) * 5 + (0,) + (1,) * 4)

    def test_ops(self):
        a, b = Vector(range(10)), Vector(range(10))

        self.assertIterableAlmostEqual(+a, a)
        self.assertIterableAlmostEqual(-a, (-x for x in range(10)))

        self.assertIterableAlmostEqual(a + b, (x + x for x in range(10)))
        self.assertIterableAlmostEqual(a - b, zeros(10))
        self.assertIterableAlmostEqual(a * 3, (x * 3 for x in range(10)))
        self.assertIterableAlmostEqual(3 * a, (3 * x for x in range(10)))
        self.assertIterableAlmostEqual(a / 3, (x / 3 for x in range(10)))
        self.assertAlmostEqual(a @ b, sum(x * x for x in range(10)))

        a += b
        self.assertIterableAlmostEqual(a, (x + x for x in range(10)))
        a -= b
        self.assertIterableAlmostEqual(a, b)
        a *= 3
        self.assertIterableAlmostEqual(a, (x * 3 for x in range(10)))
        a /= 3
        self.assertIterableAlmostEqual(a, range(10))

        self.assertRaises(ValueError, add, a, range(5))
        self.assertRaises(ValueError, sub, a, range(5))
        self.assertRaises(ValueError, matmul, a, range(5))


class UtilsTestCase(ExtendedTestCase):
    def test_solve(self):
        self.assertIterableAlmostEqual(solve(Matrix(((1, 2), (3, 4))), Vector((1, 0))), (-2, 1.5))
        self.assertIterableAlmostEqual(solve(Matrix(((127, 102.2), (90, 102.2))), Vector((102, 77))),
                                       (0.6756756756756757, 0.15840693922885704))


if __name__ == '__main__':
    main()
