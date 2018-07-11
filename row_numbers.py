"""
The program displays a series of natural numbers separated by a comma,
the square of which is less than the given number n.
The program is launched via the main class call with parameters.
"""


class RowNumbers:
    def __init__(self, number):
        self.number = self.validation(number)
        self.list = self.sequence(number)

    @staticmethod
    def validation(number):
        if type(number) != int and type(number) != float:
            raise TypeError('Parameters is not an number')
        return abs(round(number))

    @staticmethod
    def sequence(number):
        """ Outputs a series of natural numbers, the square of which is less than the specified number.
        :param number: integer or float
        :return: list
        """
        n = RowNumbers.validation(number)
        return [i for i in range(round(n ** 0.5) + 1) if i <= number]

    def __repr__(self):
        return ', '.join(map(str, self.list))
