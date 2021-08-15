from django.db import models

# Create your models here.

class Super_AdminAccount(models.Model):
    name=models.CharField(max_length=255, default="First Name")
    qr_code= models.ImageField(upload_to='SuperAdmin/',default="SuperAdmin/dummy.jpg")