"""
Console application, counts the number of lucky tickets.
Ticket number is a six-digit number.

Algorithm indicators:
'Moscow' - if the sum of the first three digits is equal to the sum of the last three
'Peter' - if the sum of digits on even positions is equal to the sum of the digits at odd positions
'Dnipro' - if the sum of even digits is equal to the sum of odd digits

To select a counting algorithm, a text file is read.
The path to the text file is set in the console after the program is started.
"""
from os import path


def lucky_check(lst, key):
    # TODO check lst and key
    key = key.lower()
    if key == 'moscow':
        if sum(lst[:3]) == sum(lst[3:]):
            return 1
        return 0
    if key == 'peter':
        if sum(lst[::2]) == sum(lst[::-2]):
            return 1
        return 0
    if key == 'dnipro':
        countable = sum([i for i in lst if i % 2 == 0])
        uncountable = sum([i for i in lst if i % 2 == 1])
        if countable == uncountable:
            return 1
        return 0


def lucky_counter(key, start=1, end=999_999):
    # TODO check start, end
    count = 0
    blank = [0, 0, 0, 0, 0, 0]
    for number in range(start, end + 1):
        new = [int(i) for i in str(number)]
        lst = blank[:(6 - len(new))] + new
        count += lucky_check(lst, key)
    return count


def start_console():
    # TODO open file, terminal
    # print(path.abspath('.'))
    # input(Specify the path to the file:)
    pass


# def terminal():
#     print('TYPE BY COMA: file path, string, replacement')
#     print('two parameters - counts the number of occurrences')
#     print('three parameters - makes a line replacement')
#     repeat = True
#     while repeat:
#         data = input(': ').split(',')