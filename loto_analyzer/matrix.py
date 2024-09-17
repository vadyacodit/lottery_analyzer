import numpy as np

from typing import *
from loto_analyzer.utils.data_parser import get_data



class Matrix:
    def __init__(self, data: Dict) -> None:
        self.data = data
        self.lucky_numbers = self.get_lucky_numbers()
        self.matrix = self.get_matrix()
        self.transposed_matrix = self.get_transposed_matrix()

# Возвращает матрицу, состоящую из удачных чисел за этот день
    def get_lucky_numbers(self) -> List[List]:
        self.lucky_numbers = []
        for val in self.data.values():
            self.lucky_numbers.append(val)

        return self.lucky_numbers

# Возвращает готовую для анализа матрицу
    def get_matrix(self):
        self.matrix = []
        period = len(self.data)
        for index in range(period):
            zeroes_list = [0] * 49
            for num in self.lucky_numbers[index]:
                for j in range(len(zeroes_list)):
                    if (j + 1) == num:
                        zeroes_list[j] += 1
            self.matrix.append(zeroes_list)

        return self.matrix

# Возвращает готовую для анализа матрицу, сортировка по числам
    def get_transposed_matrix(self):
        self.transposed_matrix = []
        period = len(self.lucky_numbers)
        for number in range(49):
            zeroes_list = [0] * period
            for day in range(period):
                if (number + 1) in self.lucky_numbers[day]:
                    zeroes_list[day] = 1
            self.transposed_matrix.append(zeroes_list)

        return self.transposed_matrix

#Для каждого числа считает, сколько дней прошло с момента последнего выпадения
    def count_days_until_hit(self):
        days_off = []
        for number in self.transposed_matrix:
            count = 0
            found = False
            while count < len(number):
                if number[count] == 1:
                    found = True
                    break
                count += 1

            if not found:
                days_off.append(len(number))
            else:
                days_off.append(count)

        return days_off

# Считает частоту выпадения числа
    def count_frequency(self):
        freq_list = []
        for days in self.transposed_matrix:
            freq = len(days) / sum(days)
            freq_list.append(freq)
        return freq_list


# Печатает матрицу построчно с нумерацией
    @staticmethod
    def show_data(matrix_data: List[List] | Dict) -> None:
        if isinstance(matrix_data, List):
            n = 1
            for row in matrix_data:
                if n < 10:
                    print(f' {n} -> {row}')
                else:
                    print(f'{n} -> {row}')
                n += 1
        else:
            for date, numbers in matrix_data.items():
                print(f'{date} -> {numbers}')

