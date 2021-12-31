import logging.config
import time
import unittest

from pyning.tail_recursion import exponent

log = logging.getLogger(__name__)


class ExponentTest(unittest.TestCase):

    def check(self, f, b, p, xr):
        r = f(b, p)
        self.assertEqual(
            r,
            xr,
            "Expected {} to yield {} but was {} !".format(f.__name__, xr, r))

    def test_exp(self):
        self.check(exponent.exp, 3, 3, 27)
        self.check(exponent.exp, 3, 4, 81)
        self.check(exponent.exp, 3, 6, 729)

    def test_rpe_exp(self):
        self.check(exponent.rpe_exp, 3, 3, 27)
        self.check(exponent.rpe_exp, 3, 4, 81)
        self.check(exponent.rpe_exp, 3, 6, 729)

    def test_fast_rpe_exp(self):
        self.check(exponent.fast_rpe_exp, 3, 3, 27)
        self.check(exponent.fast_rpe_exp, 3, 4, 81)
        self.check(exponent.fast_rpe_exp, 3, 6, 729)

    def test_speed(self):
        b = 3
        p = 240000
        # Compare speeds
        t0 = time.time_ns()
        exponent.exp(b, p)
        t1 = time.time_ns()
        exp_duration = t1 - t0
        log.debug(f"exp took\t\t\t{exp_duration:>12} nanoseconds to calculate"
                  f" {b} ^ {p}")

        # Compare speeds
        t0 = time.time_ns()
        exponent.rpe_exp(b, p)
        t1 = time.time_ns()
        rpe_exp_duration = t1 - t0
        log.debug(f"rpe_exp took\t\t{rpe_exp_duration:>12} nanoseconds to "
                  f"calculate {b} ^ {p}")

        # Compare speeds
        t0 = time.time_ns()
        exponent.fast_rpe_exp(b, p)
        t1 = time.time_ns()
        fast_rpe_exp_duration = t1 - t0
        log.debug(f"fast_rpe_exp took\t{fast_rpe_exp_duration:>12} nanoseconds"
                  f" to calculate {b} ^ {p}")

        self.assertLess(rpe_exp_duration, exp_duration)
        self.assertLess(fast_rpe_exp_duration, exp_duration)


if __name__ == '__main__':
    unittest.main()
