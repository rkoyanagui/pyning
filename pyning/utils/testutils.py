import unittest


class BaseTest(unittest.TestCase):

    def check(self, f, xr, **kwargs):
        """
        Asserts that a function 'f', when given the arguments '**kwargs',
        returns a value equal to 'xr'.

        :param f: function under evaluation
        :param xr: expected result
        :param kwargs: arguments for the function, as a dictionary
        """
        r = f(**kwargs)
        self.assertEqual(
            xr,
            r,
            "Expected {}{} = {} but was {}".format(
                f.__name__,
                kwargs,
                xr,
                r))


if __name__ == '__main__':
    unittest.main()
