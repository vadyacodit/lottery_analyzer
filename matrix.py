from typing import *



class Matrix:
    def __init__(self, data: Dict) -> None:
        self.data = data
        self.matrix = self.create_matrix(self.data)

    def create_matrix(self, data: Dict) -> List:
        self.matrix = []
        for val in data.values():
            self.matrix.append(val)
        final_matrix = [[0 for _ in range(49)] for _ in range(30)]

        return self.matrix


    def show_data(self) -> None:
        n = 1
        for val in self.data.values():
            print(f'{n} {val}')
            n += 1
