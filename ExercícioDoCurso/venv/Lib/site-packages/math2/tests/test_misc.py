from unittest import main

from math2.misc import arange, linspace, series_sum
from math2.tests import ExtendedTestCase


class MiscTestCase(ExtendedTestCase):
    def test_frange(self) -> None:
        self.assertIterableAlmostEqual(arange(5), (0, 1, 2, 3, 4))
        self.assertIterableAlmostEqual(arange(1, 5), (1, 2, 3, 4))
        self.assertIterableAlmostEqual(arange(1, 5, 0.5), (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5))

    def test_linspace(self) -> None:
        self.assertIterableAlmostEqual(linspace(0, 5, 100), arange(0, 5, 0.05))
        self.assertIterableAlmostEqual(linspace(0, 5, 5), range(5))

    def test_series_sum(self) -> None:
        self.assertEqual(series_sum(-5), -15)
        self.assertEqual(series_sum(-5, 0), -15)
        self.assertEqual(series_sum(0, -5), -15)
        self.assertEqual(series_sum(5), 15)
        self.assertEqual(series_sum(0, 5), 15)
        self.assertEqual(series_sum(0, 5, 6), 15)
        self.assertEqual(series_sum(0, 5, 2), 5)
        self.assertEqual(series_sum(1, 1, 1), 1)


if __name__ == '__main__':
    main()
