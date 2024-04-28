from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    fines = models.IntegerField()
    criminal_record = models.BooleanField()

    def __str__(self):
        return self.name

class Userfp(models.Model):
    userid = models.ForeignKey(User, related_name='fingerprints', on_delete=models.CASCADE)
    fingerprint = models.TextField()

    def __str__(self):
        return f"Fingerprint for {self.userid.name}"