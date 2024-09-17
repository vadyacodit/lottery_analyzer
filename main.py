from loto_analyzer.loto import Loto


link = 'https://www.loteriasyapuestas.es/es/resultados/bonoloto'
init_date = '20240901'
final_date = '20240915'

loto = Loto(link, init_date, final_date)
print(loto.lucky_numbers)
loto.show_data(loto.days_off)










