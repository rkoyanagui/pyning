def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def tr_factorial(n: int) -> int:
    def helper(m: int, acc: int) -> int:
        if m == 1:
            return acc
        else:
            return helper(m - 1, m * acc)

    if n <= 1:
        return 1
    else:
        return helper(n, 1)


def loop_factorial(n: int) -> int:
    def helper(m: int, acc: int) -> int:
        while True:
            if m <= 1:
                return acc
            else:
                acc = m * acc
                m = m - 1

    return helper(n, 1)
