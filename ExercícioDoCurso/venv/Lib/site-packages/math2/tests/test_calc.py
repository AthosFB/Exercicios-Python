from math import cos, exp, log, sin
from unittest import main

from math2.calc import derivative, integrate, root
from math2.consts import EPS
from math2.tests import ExtendedTestCase


class CalcTestCase(ExtendedTestCase):
    def test_derivative(self) -> None:
        self.assertAlmostEqual(derivative(lambda x: x ** 3 - 2 * x ** 2, 3, EPS), 3 * 3 ** 2 - 4 * 3)
        self.assertAlmostEqual(derivative(lambda x: -3 * sin(2 * x), 5, EPS), -6 * cos(2 * 5))

    def test_root(self) -> None:
        self.assertAlmostEqual(root(lambda x: (x - 1) * (x + 5), 4, EPS), 1)
        self.assertAlmostEqual(root(lambda x: exp(2 * x) - 10, 0.1, EPS), log(10) / 2)

    def test_integrate(self) -> None:
        self.assertAlmostEqual(integrate(lambda x: x, 0, 1), 0.5, 2)
        self.assertAlmostEqual(integrate(lambda x: 2 * x ** 2, -1, 1), 4 / 3, 3)


if __name__ == '__main__':
    main()
