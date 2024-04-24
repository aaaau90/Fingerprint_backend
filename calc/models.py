from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    fines = models.IntegerField()
    criminal_record = models.BooleanField()
    

class Userfp(models.Model):
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    fingerprint=models.TextField()