from django.db import models

# Create your models here.
class text_finding(models.Model):
    text = models.CharField(max_length=1000,null=True)