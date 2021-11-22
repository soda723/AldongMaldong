from django.db import models
# from django.db.models import Model
# Create your models here.

class RescueCenter(models.Model):
    name = models.CharField(max_length=30)
    address_road = models.CharField(max_length=50)
    address_parcdel = models.CharField(max_length=50, null=True)
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)
    opentime = models.CharField(max_length=30)
    closetime = models.CharField(max_length=30)
    dayoff = models.CharField(max_length=30, null=True)
    designated = models.DateField(null=True, )
    area = models.TextField(null=True)
    num_Vet = models.IntegerField(null=True)
    num_Researcher = models.IntegerField(null=True)
    room_consulation = models.IntegerField(null=True)
    room_operating = models.IntegerField(null=True)
    room_image = models.IntegerField(null=True)
    room_hospital = models.IntegerField(null=True)
    room_genetic = models.IntegerField(null=True)
    room_remedical = models.IntegerField(null=True)
    room_isolated = models.IntegerField(null=True)
    num_vehicle = models.IntegerField(null=True)
    box	= models.TextField(null=True)
    equipment_trep = models.TextField(null=True)
    equipment_medical = models.TextField(null=True)
    explain	= models.TextField(null=True)
    representative = models.TextField(null=True)
    tel = models.CharField(max_length = 30)
    XXX = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.pk} : {self.name}'


class AnimalInfo(models.Model):
    animal_class = models.CharField(max_length=50)#강
    infoNum = models.CharField(max_length=50)#접수번호
    name = models.CharField(max_length=50)#국명
    natural = models.CharField(max_length=50) #천연기념물여부
    endangered = models.CharField(max_length=50)#멸종위기종여부
    date_rescue = models.DateField()#구조일자
    date_result = models.DateField()#구조결과일자
    result = models.CharField(max_length=50)#구조결과
    discoverd_place = models.CharField(max_length=50)#발견장소

    def __str__(self):
            return f'{self.pk} - 접수번호 : {self.infoNum}, {self.name}'

