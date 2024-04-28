# from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
#     name = models.CharField(max_length=100)
#     fines = models.BooleanField()
#     criminal_record = models.BooleanField()

# class UserfpSerializer(serializers.ModelSerializer):
#     userid = models.ForeignKey('User', on_delete=models.CASCADE)
#     fingerprint=models.TextField()
    
    
from rest_framework import serializers
from .models import User, Userfp

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'fines', 'criminal_record']

class UserfpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userfp
        fields = ['id', 'userid', 'fingerprint']