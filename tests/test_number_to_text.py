from unittest import TestCase

from number_to_text import number_to_text as num2words


class Num2WordsRUTest(TestCase):

    def test_cardinal(self):
        self.assertEqual(num2words(100), "сто")
        self.assertEqual(num2words(101), "сто один")
        self.assertEqual(num2words(110), "сто десять")
        self.assertEqual(num2words(115), "сто пятнадцать")
        self.assertEqual(num2words(123), "сто двадцать три")
        self.assertEqual(num2words(1000), "одна тысяча")
        self.assertEqual(num2words(1001), "одна тысяча один")
        self.assertEqual(num2words(2012), "две тысячи двенадцать")

        self.assertEqual(
            num2words,
            "один миллиард двести тридцать четыре миллиона пятьсот "
            "шестьдесят семь тысяч восемьсот девяносто")
        self.assertEqual(
            num2words(2154614078920390021571),
            "двести пятнадцать нониллионов четыреста шестьдесят один "
            "октиллион четыреста семь септиллионов восемьсот девяносто "
            "два секстиллиона тридцать девять квинтиллионов два квадриллиона "
            "сто пятьдесят семь триллионов сто восемьдесят девять миллиардов "
            "восемьсот восемьдесят три миллиона девятьсот одна тысяча "
            "шестьсот семьдесят шесть")
        self.assertEqual(
            num2words(719094234693663034822824384220291),
            "семьсот девятнадцать нониллионов девяносто четыре октиллиона "
            "двести тридцать четыре септиллиона шестьсот девяносто три "
            "секстиллиона шестьсот шестьдесят три квинтиллиона тридцать "
            "четыре квадриллиона восемьсот двадцать два триллиона восемьсот "
            "двадцать четыре миллиарда триста восемьдесят четыре миллиона "
            "двести двадцать тысяч двести девяносто один")
        self.assertEqual(num2words(5), "пять")
        self.assertEqual(num2words(15), "пятнадцать")
        self.assertEqual(num2words(154), "сто пятьдесят четыре")
        self.assertEqual(
            num2words(1135), "одна тысяча сто тридцать пять"
        )
        self.assertEqual(
            num2words(418531),
            "четыреста восемнадцать тысяч пятьсот тридцать один"
        )
        self.assertEqual(
            num2words(1000139), "один миллион сто тридцать девять"
        )

    def test_floating_point(self):
        self.assertEqual(num2words(5.2), "пять запятая два")
        self.assertEqual(
            num2words(561.42),
            "пятьсот шестьдесят один запятая сорок два"
        )