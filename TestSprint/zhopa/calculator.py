

class MadCalculator:

    def sum_string(self, first_num, second_num):
        if first_num < 0 or second_num < 0:
            raise ValueError('Я решительно отказываюсь работать!')
        return int(str(first_num) + str(second_num))

    def sum_args(self, *args):
        return sum(args)
