from matrix import Matrix
from typing import *
from utils.data_parser import get_data

class Loto():
    def __init__(self, url: str, init_date: str, final_date: str):
        self.url = url
        self.init_date = init_date
        self.final_date = final_date

        self.data = get_data(self.url, self.init_date, self.final_date)
        self.matrix = Matrix(self.data)

    def get_matrix(self):
        print(self.matrix.matrix)

    def prettify_matrix(self):
        self.matrix.show_data()







