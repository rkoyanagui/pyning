from typing import Tuple


def fib(n: int) -> int:
    """
    Calculates the nth Fibonacci value, using tail recursion, and the minimum
    amount of memory (stores only the last two values needed to get
    f(n) = f(n-1) + f(n-2)).

    :param n: index of the Fibonacci sequence
    :return: the nth Fibonacci value
    """

    def helper(x: int, s: Tuple) -> int:
        if x < n:
            s1 = (s[1], s[0] + s[1])
            return helper(x + 1, s1)
        else:
            return s[1]

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return helper(1, (0, 1))
