from django.db import models

# Create your models here.

#사진을 저장할 수 있게
class box_image(models.Model):
    image=models.ImageField(upload_to='userimg', null=True)

    def __str__(self):
        return f'{self.pk} : {self.image}'

    def delete(self, *args, **kwargs):
        #삭제할때 미디어 파일도 자동으로 삭제
        super(box_image, self).delete(*args, **kwargs)
        if self.image : 
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))

class Info(models.Model):
    name = models.CharField(max_length=50)
    explain = models.TextField(null=True)
    endangered = models.BooleanField(default=False)#멸종위기종여부
    protected = models.BooleanField(default=False) #보호종여부
    etc = models.TextField(null=True)

    def __str__(self):
        return f'{self.pk} : {self.name}'

