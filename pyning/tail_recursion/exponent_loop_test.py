import unittest

from pyning.tail_recursion.exponent import loop_exp
from pyning.utils.testutils import BaseTest


class ExponentLoopTest(BaseTest):

    def test_0_exp_3(self):
        self.check(f=loop_exp, xr=0, b=0, p=3)

    def test_1_exp_3(self):
        self.check(f=loop_exp, xr=1, b=1, p=3)

    def test_2_exp_0(self):
        self.check(f=loop_exp, xr=1, b=2, p=0)

    def test_2_exp_1(self):
        self.check(f=loop_exp, xr=2, b=2, p=1)

    def test_3_exp_3(self):
        self.check(f=loop_exp, xr=27, b=3, p=3)

    def test_3_exp_4(self):
        self.check(f=loop_exp, xr=81, b=3, p=4)

    def test_3_exp_6(self):
        self.check(f=loop_exp, xr=729, b=3, p=6)


if __name__ == '__main__':
    unittest.main()
