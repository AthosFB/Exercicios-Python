from unittest import main

from math2.ntheory import gcd, lcm
from math2.tests import ExtendedTestCase


class MiscTestCase(ExtendedTestCase):
    def test_gcd(self) -> None:
        self.assertEqual(gcd(10, 15), 5)
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(0, 0), 0)

    def test_lcm(self) -> None:
        self.assertEqual(lcm(10, 15), 30)
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(0, 1), 1)


if __name__ == '__main__':
    main()
