import unittest

from fibonacci import Fibonacci as Fib


class TestFibonacci(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(Fib.validation(1, 1), True)

        self.assertRaises(TypeError, Fib.validation, '1', 0)
        self.assertRaises(TypeError, Fib.validation, 1.0, 0)
        self.assertRaises(ValueError, Fib.validation, -1, 0)

    def test_fib(self):
        self.assertEqual(Fib.fib(0, 0), [0])
        self.assertEqual(Fib.fib(0, 1), [0, 1, 1])
        self.assertEqual(Fib.fib(0, 6), [0, 1, 1, 2, 3, 5])
        self.assertEqual(Fib.fib(0, 144), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
        self.assertEqual(Fib.fib(144, 0), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])


if __name__ == '__main__':
    unittest.main()
