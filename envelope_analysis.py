"""
There are two envelopes with sides (a, b) and (c, d) to determine whether one envelope can be put in another.
The program handles the input of floating-point numbers.
The program asks for envelope sizes one parameter at a time.
After each count, the program asks whether to continue.
If the answer is "y" or "yes" or "input" (case-insensitive), the program continues to work first,
otherwise it completes execution.
"""


def envelope_analysis(a, b, c, d):
    # Simple Envelope Analysis (without diagonals)
    if max(a, b) < max(c, b) and min(a, b) < min(c, d):
        print("It's possible to put: {}*{} --> {}*{}".format(a, b, c, d))
        return 1  # for unittest
    elif max(a, b) > max(c, d) and min(a, b) > min(c, d):
        print("It's possible to put: {}*{} <-- {}*{}".format(a, b, c, d))
        return 2  # for unittest
    else:
        print("It's NOT possible to put: {}*{} <--> {}*{}".format(a, b, c, d))
        return 0  # for unittest


def text_to_float(text):
    try:
        text = text.replace(',', '.').replace(' ', '')
        number = float(text)
    except ValueError:
        print('{} -- IS NOT NUMBER! Retype!'.format(text))
        return text  # It's important for loop in terminal function
    return number


def start_terminal():
    dimension = []
    instructions = [
        'WIDTH of the FIRST envelope: ',
        'HEIGHT of the FIRST envelope: ',
        'WIDTH of the SECOND envelope: ',
        'HEIGHT of the SECOND envelope: '
    ]

    while len(dimension) < 4:
        text = input(instructions[len(dimension)])
        text = text_to_float(text)
        if type(text) == float:
            dimension.append(text)

    a, b, c, d = dimension
    envelope_analysis(a, b, c, d)

    n = input("y/n to repeat :").lower()
    if n in ('yes', 'y'):
        return start_terminal()


if __name__ == "__main__":
    start_terminal()
