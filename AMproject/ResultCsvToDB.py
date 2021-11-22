import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AMproject.settings")
django.setup()

from sub1app.models import AnimalInfo

CSV_PATH ="./data2.csv"

count = 1
with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:

        AnimalInfo.objects.create(
            animal_class = row['강'],
            infoNum = row['접수번호'],
            name = row['국   명'],
            natural = row['천연기념물'], 
            endangered = row['멸종 위기종'], 
            date_rescue = row['구조 일자'], 
            date_result = row['구조결과일자'], 
            result = row['구조 결과'], 
            discoverd_place = row['발견장소 특징'], 
        )

        count += 1

        if count % 100 == 0:
            print(count)

print(count)
print('data update end')
