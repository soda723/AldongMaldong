import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AMproject.settings")
django.setup()

from sub1app.models import RescueCenter

CSV_PATH ="./aldongmaldongVER2.csv"

count = 1
with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:

        if row['수의사인원수']=='' :
                row['수의사인원수']=None
        if row['질병연구자인원수']=='':
                row['질병연구자인원수']=None
        if row['진료실수']=='':
                row['진료실수']=None
        if row['수술실수']=='': 
                row['수술실수']=None
        if row['영상진단실수']=='': 
                row['영상진단실수']=None
        if row['입원실수']=='': 
                row['입원실수']=None
        if row['유전자원보관실수']=='': 
                row['유전자원보관실수']=None
        if row['재활실수']=='': 
                row['재활실수']=None
        if row['격리실수']=='': 
                row['격리실수']=None
        if row['구조차량대수']=='': 
                row['구조차량대수']=None    
        
        RescueCenter.objects.create(
            name = row['야생동물구조센터명'],
            XXX = row['XXX'],
            address_road = row['소재지도로명주소'],
            address_parcdel = row['소재지지번주소'],
            latitude = row['위도'],
            longitude = row['경도'],
            opentime = row['운영시작시각'],
            closetime = row['운영종료시각'],
            dayoff = row['휴무일'],
            designated = row['야생동물구조센터지정일자'],
            area = row['야생동물구조센터면적'],

            num_Vet = row['수의사인원수'],
            num_Researcher = row['질병연구자인원수'],
            room_consulation = row['진료실수'],
            room_operating = row['수술실수'],
            room_image = row['영상진단실수'],
            room_hospital = row['입원실수'],
            room_genetic = row['유전자원보관실수'],
            room_remedical = row['재활실수'],
            room_isolated = row['격리실수'],
            num_vehicle = row['구조차량대수'],

            box	= row['운반상자현황'], 
            equipment_trep = row['포획장비현황'],
            equipment_medical = row['진료장비현황'],
            explain	= row['구조센터기능'],
            representative = row['대표자명'],
            tel = row['전화번호'],
        )

        
        count += 1

        if count % 100 == 0:
            print(count)

print(count)
print('data update end')

