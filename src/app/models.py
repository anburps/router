from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    
    name= models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    experince=models.IntegerField()

    def __str__(self):
        return self.name
    
class GetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=250,unique=False)
    created_at=models.DateTimeField()

    def __str__(self):
        return self.user.username

    