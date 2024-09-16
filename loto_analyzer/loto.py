import numpy as np

from typing import *
from loto_analyzer.utils.data_parser import get_data



class Loto:
    def __init__(self, url: str, init_date: str, final_date: str) -> None:
        self.url = url
        self.init_date = init_date
        self.final_date = final_date

        self.data = get_data(self.url, self.init_date, self.final_date)
        self.lucky_numbers = self.get_lucky_numbers()
        self.matrix = self.get_matrix()

# Возвращает матрицу, состоящую из удачных чисел за этот день
    def get_lucky_numbers(self) -> List[List]:
        self.lucky_numbers = []
        for val in self.data.values():
            self.lucky_numbers.append(val)

        return self.lucky_numbers

#Возвращает готовую для анализа матрицу
    def get_matrix(self):
        self.matrix = []
        period = len(self.data)
        for index in range(period):
            zeroes_list = [0] * 49
            for num in self.lucky_numbers[index]:
                for j in range(len(zeroes_list)):
                    if (j+1) == num:
                        zeroes_list[j] += 1
            self.matrix.append(zeroes_list)
        return self.matrix

    def days_until_next_hit(self):
        self.matrix = np.array(self.matrix).T
        print(self.show_data())


# Печатает матрицу построчно с нумерацией
    @staticmethod
    def show_data(matrix_data: List[List] | Dict) -> None:
        if isinstance(matrix_data, List):
            n = 1
            for row in matrix_data:
                if n < 10:
                    print(f' {n} {row}')
                else:
                    print(f'{n} {row}')
                n += 1
        else:
            for date, numbers in matrix_data.items():
                print(f'{date} -> {numbers}')

