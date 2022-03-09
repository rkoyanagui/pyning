from typing import Tuple


def naive_fib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return naive_fib(n - 1) + naive_fib(n - 2)


def tr_fib(n: int) -> int:
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


def loop_fib(n: int) -> int:
    def helper(x: int, s: Tuple) -> int:
        while x < n:
            s = (s[1], s[0] + s[1])
            x = x + 1
        return s[1]

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return helper(1, (0, 1))
