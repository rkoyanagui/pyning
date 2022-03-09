import logging
import time
import unittest

from pyning.tail_recursion.exponent import naive_exp, rpe_exp, fast_rpe_exp, loop_exp
from pyning.utils.testutils import BaseTest

log = logging.getLogger(__name__)


class ExponentSpeedTest(BaseTest):

    def test_rpe_exp_speed(self):
        b = 3
        p = 240000
        t0 = time.time_ns()
        naive_exp(b, p)
        t1 = time.time_ns()
        exp_duration = t1 - t0
        log.debug(f"exp took\t\t\t{exp_duration:>12} nanoseconds to calculate"
                  f" {b} ^ {p}")

        t0 = time.time_ns()
        rpe_exp(b, p)
        t1 = time.time_ns()
        rpe_exp_duration = t1 - t0
        log.debug(f"rpe_exp took\t\t{rpe_exp_duration:>12} nanoseconds to "
                  f"calculate {b} ^ {p}")

        self.assertLess(rpe_exp_duration, exp_duration)

    def test_fast_rpe_exp_speed(self):
        b = 3
        p = 240000
        t0 = time.time_ns()
        rpe_exp(b, p)
        t1 = time.time_ns()
        rpe_exp_duration = t1 - t0
        log.debug(f"rpe_exp took\t\t{rpe_exp_duration:>12} nanoseconds to "
                  f"calculate {b} ^ {p}")

        t0 = time.time_ns()
        fast_rpe_exp(b, p)
        t1 = time.time_ns()
        fast_rpe_exp_duration = t1 - t0
        log.debug(f"fast_rpe_exp took\t{fast_rpe_exp_duration:>12} nanoseconds"
                  f" to calculate {b} ^ {p}")

        self.assertLess(fast_rpe_exp_duration, rpe_exp_duration)


if __name__ == '__main__':
    unittest.main()
