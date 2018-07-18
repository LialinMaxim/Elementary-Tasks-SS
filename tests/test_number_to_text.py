from unittest import TestCase, main
from sys import path

path.append('../')

from number_to_text import number_to_text


class Num2WordsRUTest(TestCase):

    def test_different_numbers(self):
        self.assertEqual(number_to_text(5), "пять")
        self.assertEqual(number_to_text(15), "пятнадцать")
        self.assertEqual(number_to_text(100), "сто")
        self.assertEqual(number_to_text(101), "сто один")
        self.assertEqual(number_to_text(110), "сто десять")
        self.assertEqual(number_to_text(115), "сто пятнадцать")
        self.assertEqual(number_to_text(123), "сто двадцать три")
        self.assertEqual(number_to_text(154), "сто пятьдесят четыре")
        self.assertEqual(number_to_text(1000), "одна тысяча")
        self.assertEqual(number_to_text(1001), "одна тысяча один")
        self.assertEqual(number_to_text(1135), "одна тысяча сто тридцать пять")
        self.assertEqual(number_to_text(2012), "две тысячи двенадцать")
        self.assertEqual(number_to_text(418531), "четыреста восемнадцать тысяч пятьсот тридцать один")
        self.assertEqual(number_to_text(1000139), "один миллион сто тридцать девять")

    def test_floating_point(self):
        self.assertEqual(number_to_text(5.2), "пять запятая два")
        self.assertEqual(number_to_text(561.42), "пятьсот шестьдесят один запятая сорок два")

    def test_negative_number(self):
        self.assertEqual(number_to_text(-5), "минус пять")
        self.assertEqual(number_to_text(-561.42), "минус пятьсот шестьдесят один запятая сорок два")

    def test_text(self):
        self.assertEqual(number_to_text('-5'), "минус пять")
        self.assertEqual(number_to_text("-561.42"), "минус пятьсот шестьдесят один запятая сорок два")


if __name__ == '__main__':
    main()
