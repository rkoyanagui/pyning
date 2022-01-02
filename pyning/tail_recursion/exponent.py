def odd(n):
    return n % 2 == 1


def exp(b: int, p: int):
    """
    Performs exponentiation using the definition.
    We ignore case in which exponent is negative for simplicity.
    """
    if b == 0:
        return 0
    elif b == 1:
        return 1
    elif p == 0:
        return 1
    else:
        n = b
        for _ in range(1, p):
            n = n * b

    return n


def rpe_exp(b, p):
    if p < 0:
        return rpe_exp(1 / b, -p)
    elif p == 0:
        return 1
    elif p == 1:
        return b
    elif odd(p):
        return b * rpe_exp(b * b, (p - 1) / 2)
    else:
        return rpe_exp(b * b, p / 2)


def fast_rpe_exp(b: int, p: int):
    """
    Calculates exponential using the RPE (Russian Peasant Exponentiation)
    algorithm , but using tail recursion.
    """

    def helper(x, n, acc):
        """
        @args:
            - x: base
            - m: power
            - acc: accumulator variable
        """
        if x == 0:
            return 0
        elif n == 0:
            return acc
        elif n == 1:
            return x * acc
        else:
            if odd(n):
                # Accumulate the result in acc instead of keeping in the heap
                return helper(x * x, (n - 1) / 2, x * acc)
            else:
                # Halve the power, and accumulate
                return helper(x * x, n / 2, acc)

    return helper(b, p, 1)


def loop_exp(b: int, p: int) -> int:
    def helper(b1: int, p1: int, acc: int) -> int:
        while True:
            if b1 == 0:
                return 0
            elif p1 == 0:
                return acc
            elif p1 == 1:
                return b1 * acc
            else:
                if odd(p1):
                    acc = b1 * acc
                    p1 = (p1 - 1) // 2
                    b1 = b1 * b1
                else:
                    p1 = p1 // 2
                    b1 = b1 * b1

    return helper(b, p, 1)
