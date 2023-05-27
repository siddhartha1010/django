from django.db import models

# Create your models here.
class MyForm(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.first_name


