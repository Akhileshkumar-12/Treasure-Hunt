from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User , on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    Year= models.CharField(max_length=30)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
        