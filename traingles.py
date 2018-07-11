class Traingles:
    def __init__(self, name, a, b, c):
        self.name = name
        p = (a + b + c) / 2
        if p >= a and p >= b and p >= c:
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            self.area = round(area, 2)
        else:
            self.area = None

    def __str__(self):
        return "[{}]: {} cm**2".format(self.name, self.area)


def start_terminal():
    '''Launches a console program for creating and sorting triangles'''
    my_traingles = []

    repeat = 1  # for break condition
    while repeat:
        print('-' * 3, 'NEW TRAIGLE', '-' * 3)
        name = input("NAME: ")
        try:
            sides = input("SIDES a,b,c by comma: ")
            a, b, c = sides.replace(' ', '').split(',')
            a, b, c = float(a), float(b), float(c)
            my_traingles.append(Traingles(name, a, b, c))
        except ValueError:
            print('ValueError, can not be processed:', sides)

        question = input("'Y' or 'YES' to continue:").lower()
        if question not in ('yes', 'y', ''):  # or just press ENTER
            repeat = 0

    # output and sort created triangles
    print('\n' * 2, '=' * 5 + ' Traingles list: ' + '=' * 5)
    i = 1
    for t in sorted(my_traingles, key=lambda x: x.area):
        print(str(i) + ".", t)
        i += 1


if __name__ == "__main__":
    start_terminal()
