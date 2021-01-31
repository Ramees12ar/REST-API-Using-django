from django.db import models

# Create your models here.
class users(models.Model):
    emplo_id=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    phone=models.IntegerField()

    def upload_dir(self,filename):
        path="app/photo/{}".format(filename)
        return path
    photo=models.ImageField(upload_to=upload_dir,null=True,blank=True)

    def upload_file(self,filename):
        path="app/file/{}".format(filename)
        return path
    result=models.FileField(upload_to=upload_file,null=True,blank=True)

    def __str__(self):
        return f"{self.emplo_id}-{self.name}"