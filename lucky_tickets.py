"""
Console application, counts the number of lucky tickets.
Ticket number is a six-digit number.
Algorithm indicators:
'Moscow' - if the sum of the first three digits is equal to the sum of the last three
'Piter' - if the sum of digits on even positions is equal to the sum of the digits at odd positions
'Dnipro' - if the sum of even digits is equal to the sum of odd digits
To select a counting algorithm, a text file is read.
The path to the text file is set in the console after the program is started.
"""


def lucky_check(number, key):
    if key.lower() == 'moskow':
        if sum(lst[:3]) == sum(lst[3:]):
            return 1
        return 0
    lst = [int(i) for i in str(number)][:6]
    if key.lower() == 'piter':
        if sum(lst[::2]) == sum(lst[::-2]):
            return 1
        return 0
    if key.lower() == 'dnipro':
        countable = sum([i for i in lst if i % 2 == 0])
        uncountable = sum([i for i in lst if i % 2 == 1])
        if countable == uncountable:
            return 1
        return 0


def lucky_counter(key, start=0, end=999999):
    count = 0
    for i in range(start, end):
        count += lucky_check(i, key)

def start_console():
