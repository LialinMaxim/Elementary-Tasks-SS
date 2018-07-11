import unittest

from row_numbers import RowNumbers


class TestRowNumbers(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(RowNumbers.validation(1), 1)
        self.assertEqual(RowNumbers.validation(1.0), 1)
        self.assertEqual(RowNumbers.validation(-1), 1)

        self.assertRaises(TypeError, RowNumbers.validation, '1', 0)

    def test_sequence(self):
        self.assertEqual(RowNumbers.sequence(1), [0, 1])
        self.assertEqual(RowNumbers.sequence(4), [0, 1, 2])
        self.assertEqual(RowNumbers.sequence(30), [0, 1, 2, 3, 4, 5])
        self.assertEqual(RowNumbers.sequence(81), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(RowNumbers.sequence(100), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(RowNumbers.sequence(121), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])


if __name__ == '__main__':
    unittest.main()
