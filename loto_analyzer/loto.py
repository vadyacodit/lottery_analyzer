from loto_analyzer.matrix import Matrix
from typing import *
from loto_analyzer.utils.data_parser import get_data

class Loto:
    def __init__(self, url: str, init_date: str, final_date: str):
        self.url = url
        self.init_date = init_date
        self.final_date = final_date

        self.data = get_data(self.url, self.init_date, self.final_date)
        self.matrix = Matrix(self.data)

# Возвращает матрицу, состоящую из удачных чисел за этот день
    def get_lucky_numbers(self):
        print(self.matrix.lucky_numbers_matrix)

# Возвращает готовую для анализа матрицу
    def get_matrix(self):
        return self.matrix.matrix

# Печатает матрицу построчно с нумерацией
    def prettify_matrix(self):
        self.matrix.show_data()







