import unittest
from sys import path
path.append('../')

import envelope_analysis as env


class TestEnvelopeAnalysis(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(env.envelope_analysis(1, 1.0, 1, 1), 0)
        self.assertEqual(env.envelope_analysis(2.1, 2, 2.2, 2.1), 1)
        self.assertEqual(env.envelope_analysis(1, 1, 3, 3), 1)
        self.assertEqual(env.envelope_analysis(3, 3, 1, 1), 2)

    def test_text_to_float(self):
        self.assertEqual(env.text_to_float('1'), 1.0)
        self.assertEqual(env.text_to_float('1.'), 1.0)
        self.assertEqual(env.text_to_float('a'), 'a')


if __name__ == '__main__':
    unittest.main()
