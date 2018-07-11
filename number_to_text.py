from num2words import num2words  #https://pypi.org/project/num2words/


def number_to_text(number):
    '''
    Converts a number to text in Russian
    :param number: int
    :return: str, None if case of invalid data
    '''

    try:
        return num2words(number, lang='ru')
    except ValueError:
        print('invalid data:', number)
        return None


if __name__ == "__main__":
    for n in (14, -587, 'a', 78987877, 1.1):
        print(n, '-->', number_to_text(n))