from django.db import models

# Create your models here.
class counterModel(models.Model):
    id = models.AutoField(primary_key=True)
    count= models.IntegerField(default=0)
    def __str__(self):
        return str(self.count)
    

class loginModel(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)