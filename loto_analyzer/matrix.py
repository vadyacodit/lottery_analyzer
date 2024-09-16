from typing import *



class Matrix:
    def __init__(self, data: Dict) -> None:
        self.data = data
        self.lucky_numbers_matrix = self.get_lucky_numbers(self.data)
        self.matrix = self.get_matrix(self.lucky_numbers_matrix)

# Возвращает матрицу, состоящую из удачных чисел за этот день
    def get_lucky_numbers(self, data: Dict) -> List[List]:
        self.lucky_numbers_matrix = []
        for val in data.values():
            self.lucky_numbers_matrix.append(val)

        return self.lucky_numbers_matrix

#Возвращает готовую для анализа матрицу
    def get_matrix(self, lucky_numbers_matrix: List[List]):
        self.matrix = []
        period = len(self.data)
        for index in range(period):
            zeroes_list = [0] * 49
            for num in self.lucky_numbers_matrix[index]:
                for j in range(len(zeroes_list)):
                    if (j+1) == num:
                        zeroes_list[j] += 1
            self.matrix.append(zeroes_list)
        return self.matrix


# Печатает матрицу построчно с нумерацией
    def show_data(self) -> None:
        n = 1
        for row in self.matrix:
            if n < 10:
                print(f' {n} {row}')
            else:
                print(f'{n} {row}')
            n += 1
