import unittest

import lucky_tickets as ticket


class TestLuckyTickets(unittest.TestCase):
    def test_lucky_check(self):
        # 1 - lucky ticket, 0 - not lucky
        parameters = [
            [[9, 9, 9, 9, 9, 9], 'moscow', 1],
            [[1, 1, 1, 9, 9, 9], 'Moscow', 0],
            [[0, 0, 0, 0, 0, 1], 'Moscow', 0],
            [[9, 2, 9, 2, 9, 2], 'peter', 0],
            [[1, 1, 2, 2, 3, 3], 'Peter', 1],
            [[1, 0, 0, 0, 0, 1], 'Peter', 1],
            [[1, 1, 1, 1, 4, 0], 'dnipro', 1],
            [[1, 1, 1, 1, 4, 0], 'Dnipro', 1],
            [[9, 9, 9, 9, 9, 9], 'Dnipro', 0],
        ]
        for lst, key, outcome in parameters:
            self.assertEqual(ticket.lucky_check(lst, key), outcome)

    def test_lucky_counter(self):
        # parameters: name of count method, first and second number of tickets, amount of lucky tickets
        parameters = [
            ['Moscow', 1, 999_999, 55_251],
            ['Peter', 1, 999_999, 55_251],
            ['Dnipro', 1, 999_999, 25080],
        ]
        for key, start, end, outcome in parameters:
            self.assertEqual(ticket.lucky_counter(key, start, end), outcome)


if __name__ == '__name__':
    unittest.main()
