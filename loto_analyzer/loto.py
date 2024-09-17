from loto_analyzer.matrix import Matrix
from loto_analyzer.utils.data_parser import get_data

class Loto:
    def __init__(self, url: str, init_date: str, final_date: str) -> None:
        self.url = url
        self.init_date = init_date
        self.final_date = final_date
        self.data = get_data(self.url, self.init_date, self.final_date)

        self.mtx = Matrix(self.data)

# Методы для анализа

    def days_off(self):
        print('Сколько дней прошло с последнего выпадения')
        for i in range(len(self.mtx.count_days_until_hit())):
            print(f'{i+1} выпадал {self.mtx.count_days_until_hit()[i]} дней назад')

    def frequency(self):
        print('Частота выпадения каждого из чисел')
        for i in range(len(self.mtx.count_frequency())):
            print(f'Число {i + 1} выпадало с частотой {round(self.mtx.count_frequency()[i])} за период в {len(self.mtx.transposed_matrix)} дней')