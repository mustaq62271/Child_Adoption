from django.db import models

# Create your models here.
class ChildTable(models.Model):

    name=models.CharField(max_length=20,blank=False)
    childcode=models.CharField(max_length=10,blank=False)
    childage=models.CharField(max_length=10,blank=False)
    health=models.CharField(max_length=10,blank=False)
    childweight=models.CharField(max_length=10,blank=False)
    childheight=models.CharField(max_length=10,blank=False)
    gender=models.CharField(max_length=10,blank=False)
    blood=models.CharField(max_length=10,blank=False)
    image = models.ImageField(upload_to='media/childimage/')

    def __str__(self):
        return self.name
