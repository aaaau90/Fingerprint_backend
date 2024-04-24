from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    name = models.CharField(max_length=100)
    fines = models.BooleanField()
    criminal_record = models.BooleanField()

class UserfpSerializer(serializers.ModelSerializer):
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    fingerprint=models.TextField()
    