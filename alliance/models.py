from django.db import models

# Create your models here.

class Personn(models.Model):
    l_name = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    birthday = models.DateField()
    post = models.CharField(max_length=250, blank=True)
    phone = models.IntegerField(blank=True)
    
    
    def __str__(self):
        return self.l_name