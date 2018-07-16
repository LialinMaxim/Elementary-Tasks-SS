"""
The console program draws out the triangles in descending order of their area.
After adding each new triangle, the program asks if you need to add one more.
If the answer is "y" or "yes" (not case sensitive), the program will ask you to enter data for another triangle,
otherwise - print the result to the console.
"""


class Triangle:
    def __init__(self, name, sides, area):
        self.name = name
        self.sides = sides
        self.area = area

    def __str__(self):
        return "[{}]: {} cm²".format(self.name, self.area)

    @staticmethod
    def triangle_area(sides):
        # Gerone formula
        a, b, c = sides
        p = (a + b + c) / 2
        if p <= a or p <= b or p <= c:
            return None
        area = ((p - a) * (p - b) * (p - c)) ** 0.5
        return round(area, 4)

    @staticmethod
    def create():
        name = input("NAME: ")
        valid_sides = None
        while not valid_sides:
            sides = input("SIDES by comma: ").replace(' ', '').split(',')
            try:
                a, b, c = sides
                sides = (abs(float(a)), abs(float(b)), abs(float(c)))
            except ValueError:
                print('ValueError, please specify the dimensions again:', sides)
            except TypeError:
                print('TypeError, please specify the dimensions again:', sides)
            if len(sides) == 3:
                area = Triangle.triangle_area(sides)
                if area:
                    return Triangle(name, sides, area)
                    valid_sides = True
                else:
                    print('ValueError:', sides)
                    print('It is impossible to create a triangle with such sides!')
            else:
                print("The number of sides is not exactly three")


def start_terminal():
    """Launches a console program"""
    new_triangles = []
    repeat = True  # for break condition
    while repeat:
        print('--- NEW TRIANGLE ---')
        new_triangles.append(Triangle.create())
        question = input("[Y/N] to continue: ").lower()
        if question not in ('yes', 'y'):  # or just press ENTER
            repeat = None

    # output and sort triangles
    print('\n============= Triangles list: ===============')
    i = 1
    for self in sorted(new_triangles, key=lambda x: x.area):
        print('{}. [Triangle {}]: {} сm²'.format(i, self.name, self.area))
        i += 1


if __name__ == "__main__":
    start_terminal()
