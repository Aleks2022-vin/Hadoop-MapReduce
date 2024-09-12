import sys

geographic_data = {}

for line in open('geographic.csv', 'r'):
    city, county, region = line.strip().split('","')
    geographic_data[city] = (county, region)

# Читаем данные из стандартного ввода
for line in sys.stdin:
    id_restaurant, street_num, street_name, city = line.strip().split('","')
    # Если city указан в location, выполняем JOIN
    if city in geographic_data:
        county, region = geographic_data[city]
        print(f'"{city}","{county}","{region}","{id_restaurant}","{street_num}","{street_name}"')

