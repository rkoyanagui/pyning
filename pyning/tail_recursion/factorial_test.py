import unittest

from pyning.tail_recursion.factorial import factorial
from pyning.utils.testutils import BaseTest


class FactorialTest(BaseTest):

    def test_minus_one(self):
        self.check(f=factorial, xr=1, n=-1)

    def test_0(self):
        self.check(f=factorial, xr=1, n=0)

    def test_1(self):
        self.check(f=factorial, xr=1, n=1)

    def test_2(self):
        self.check(f=factorial, xr=2, n=2)

    def test_3(self):
        self.check(f=factorial, xr=6, n=3)

    def test_4(self):
        self.check(f=factorial, xr=24, n=4)

    def test_5(self):
        self.check(f=factorial, xr=120, n=5)

    def test_6(self):
        self.check(f=factorial, xr=720, n=6)


if __name__ == '__main__':
    unittest.main()
