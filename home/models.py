from email import message
from django.db import models

# Create your models here.
class contactModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    message=models.TextField()
    
    class Meta:
        verbose_name_plural = 'contacts'
        
    def __str__(self):
        return self.name