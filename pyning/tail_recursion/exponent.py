def odd(n):
    return n % 2 == 1


def exp(b: int, p: int):
    """
    Performs exponentiation using the definition.
    We ignore case in which exponent is negative for simplicity.
    """
    n = b
    for _ in range(1, p):
        n = n * b

    return n


def rpe_exp(x, n):
    if n < 0:
        return rpe_exp(1 / x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif odd(n):
        return x * rpe_exp(x * x, (n - 1) / 2)
    else:
        return rpe_exp(x * x, n / 2)


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
