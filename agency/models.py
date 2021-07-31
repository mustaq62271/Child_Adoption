from django.db import models

# Create your models here.
class AgencyTable(models.Model):

    name=models.CharField(max_length=20,blank=False)
    division=models.CharField(max_length=10,blank=False)
    district=models.CharField(max_length=10,blank=False)
    contact=models.CharField(max_length=15,blank=False)
    address=models.TextField(max_length=100,blank=False)

    def __str__(self):
        return self.name
