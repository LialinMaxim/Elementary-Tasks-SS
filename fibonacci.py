"""
The program allows you to output all Fibonacci numbers that are in the specified range.
The range is specified by two arguments when calling a higher class.
The numbers are output comma-separated in ascending order.
"""


class Fibonacci:
    def __init__(self, last, first=0):
        self.first = first
        self.last = last
        self.list = self.fib(first, last)

    @staticmethod
    def validation(first, last):
        if (type(first) != int) or (type(last) != int):
            raise TypeError('One of the parameters is not an integer')
        if first < 0 or last < 0:
            raise ValueError('One of the parameters is less than zero')
        return True

    @staticmethod
    def fib(first, last):
        Fibonacci.validation(first, last)

        '''in case if first > last'''
        if last < first:
            last, first = first, last

        '''fibonacci generation'''
        fib_list = []
        a, b = 0, 1
        while a <= last:
            if first <= a <= last:
                fib_list.append(a)
            a, b = b, a + b
        return fib_list

    def __repr__(self):
        return ', '.join(map(str, self.list))

