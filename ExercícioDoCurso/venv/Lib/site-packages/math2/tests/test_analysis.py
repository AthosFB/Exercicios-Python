from unittest import main

from math2.analysis import interpolate
from math2.tests import ExtendedTestCase


class AnalysisTestCase(ExtendedTestCase):
    def test_interpolate(self) -> None:
        self.assertAlmostEqual(interpolate(1, (0, 2), (0, 3)), 1.5)
        self.assertAlmostEqual(interpolate(1, (0, 1), (0, 3)), 3)
        self.assertAlmostEqual(interpolate(2, (0, 1), (0, 6)), 12)


if __name__ == '__main__':
    main()
