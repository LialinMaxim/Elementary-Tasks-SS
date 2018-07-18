import unittest
from sys import path
path.append('../')

import envelope_analysis as env


class TestEnvelopeAnalysis(unittest.TestCase):
    def test_validation(self):
        data_test = (
            (1, 1.0, 1, 1, "It's NOT possible to put: 1*1.0 <--> 1*1"),
            (1, 1, 3, 3, "It's possible to put: 1*1 --> 3*3"),
            (3, 3, 1, 1, "It's possible to put: 3*3 <-- 1*1"),
        )
        for h, w, h2, w2, answer in data_test:
            self.assertEqual(env.envelope_analysis(h, w, h2, w2), answer)

    def test_text_to_float(self):
        data_test = (
            ('1', 1.0),
            ('1.', 1.0),
            ('a', 'a'),
        )
        for test, answer in data_test:
            self.assertEqual(env.text_to_float(test), answer)


if __name__ == '__main__':
    unittest.main()
