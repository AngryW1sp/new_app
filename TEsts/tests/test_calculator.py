import unittest

from calc_code.calculator import MadCalculator


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = MadCalculator()
        print(self.calc)

    def test_sum_string(self):

        act = self.calc.sum_string(1, 100500)
        self.assertEqual(
            act, 1100500, 'Метод sum_string работает не правильно.')

    def test_sum_string_negative_value(self):

        with self.assertRaises(ValueError):
            self.calc.sum_string(1, -100500)

    def test_sum_args(self):

        act = self.calc.sum_args(3, -3, 5)
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно')
