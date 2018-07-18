"""
There are two envelopes with sides (a, b) and (c, d) to determine whether one envelope can be put in another.
The program handles the input of floating-point numbers.
The program asks for envelope sizes one parameter at a time.
After each count, the program asks whether to continue.
If the answer is "y" or "yes" or "input" (case-insensitive), the program continues to work first,
otherwise it completes execution.
"""

INSTRUCTIONS = (
    'HEIGHT of the FIRST envelope: ',
    'WIDTH of the FIRST envelope: ',
    'HEIGHT of the SECOND envelope: ',
    'WIDTH of the SECOND envelope: ',
)


def envelope_analysis(h, w, h2, w2):
    # Simple Envelope Analysis (without diagonals)
    # h - height, w - width of envelopes
    if max(h, w) < max(h2, w) and min(h, w) < min(h2, w2):
        return "It's possible to put: {}*{} --> {}*{}".format(h, w, h2, w2)
    elif max(h, w) > max(h2, w2) and min(h, w) > min(h2, w2):
        return "It's possible to put: {}*{} <-- {}*{}".format(h, w, h2, w2)
    else:
        return "It's NOT possible to put: {}*{} <--> {}*{}".format(h, w, h2, w2)


def text_to_float(text):
    try:
        text = text.replace(',', '.').replace(' ', '')
        number = float(text)
    except ValueError:
        print('{} -- IS NOT NUMBER! Retype!'.format(text))
        return text  # It's important for loop in terminal function
    return number


def start_terminal():
    print('====== ENVELOPE ANALYTICS ======')
    dimension = []

    while len(dimension) < 4:
        text = input(INSTRUCTIONS[len(dimension)])
        text = text_to_float(text)
        if type(text) == float:
            dimension.append(text)

    h, w, h2, w2 = dimension
    print(envelope_analysis(h, w, h2, w2))

    n = input("[Y / N] :").lower().strip()
    if n in ('yes', 'y'):
        start_terminal()


if __name__ == "__main__":
    start_terminal()
