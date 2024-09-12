# Hadoop-MapReduce

Скрипты

В репозитории содержатся два скрипта на Python:

mapjoin.py: выполняет INNER JOIN датасетов location и geographic по полю city.
reducejoin.py: выполняет INNER JOIN датасетов location и generalinfo по полю id_restaurant.
Запуск скриптов с помощью Hadoop Streaming

Чтобы запустить скрипты с помощью Hadoop Streaming, вам нужно создать два файла: mapper.py и reducer.py. В mapper.py нужно поместить код из mapjoin.py, а в reducer.py - код из reducejoin.py.

Затем вы можете запустить Hadoop Streaming с помощью следующей команды:

bash

Verify

Open In Editor
Edit
Copy code
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -input input.txt \
  -output output.txt \
  -mapper mapper.py \
  -reducer reducer.py
Замените input.txt и output.txt на ваши входные и выходные файлы соответственно.

Входные файлы

Входные файлы для скриптов должны быть в формате CSV и содержать следующие поля:

location.csv: id_restaurant, street_num, street_name, city
geographic.csv: city, county, region
generalinfo.csv: id_restaurant, label, food_type, review, city
Выходные файлы

Выходные файлы для скриптов будут в формате CSV и содержать следующие поля:

mapjoin_output.txt: city, county, region, id_restaurant, street_num, street_name
reducejoin_output.txt: id_restaurant, street_num, street_name, city, label, food_type, review
