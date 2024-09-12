import sys

# Словарь для хранения данных из датасета generalinfo
generalinfo_data = {}

# Читаем данные из датасета generalinfo
for line in open('generalinfo.csv', 'r'):
    id_restaurant, label, food_type, review, city = line.strip().split('","')
    generalinfo_data[id_restaurant] = (label, food_type, review, city)

# Читаем данные из стандартного ввода
for line in sys.stdin:
    # Разделяем строку на поля
    id_restaurant, street_num, street_name = line.strip().split('","')

    # Если id_restaurant указан в generalinfo, выполняем JOIN
    if id_restaurant in generalinfo_data:
        label, food_type, review, city = generalinfo_data[id_restaurant]
        print(f'"{id_restaurant}","{street_num}","{street_name}","{city}","{label}","{food_type}","{review}"')
