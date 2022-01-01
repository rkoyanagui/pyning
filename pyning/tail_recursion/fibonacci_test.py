import unittest

from pyning.tail_recursion.fibonacci import fib
from pyning.utils.testutils import BaseTest


class FibonacciTest(BaseTest):

    def test_zero(self):
        self.check(f=fib, xr=0, n=0)

    def test_one(self):
        self.check(f=fib, xr=1, n=1)

    def test_two(self):
        self.check(f=fib, xr=1, n=2)

    def test_three(self):
        self.check(f=fib, xr=2, n=3)

    def test_four(self):
        self.check(f=fib, xr=3, n=4)

    def test_five(self):
        self.check(f=fib, xr=5, n=5)

    def test_six(self):
        self.check(f=fib, xr=8, n=6)


if __name__ == '__main__':
    unittest.main()
