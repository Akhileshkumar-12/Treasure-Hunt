from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.expressions import When
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User , on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    Year= models.CharField(max_length=30)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    score=models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)
class McqProblems(models.Model):
    question = RichTextUploadingField(null=True, blank=True)
    optiona = models.TextField(max_length=100)
    optionb = models.TextField(max_length=100)
    optionc = models.TextField(max_length=100)
    optiond = models.TextField(max_length=100)
    correct_ans = models.IntegerField(default=0)


class McqSubmissions(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(McqProblems, on_delete=models.CASCADE)
    submitted_output = models.IntegerField(default=0)
    result = models.NullBooleanField(default=None, null=True)


class Contests(models.Model):
    participants = models.ManyToManyField(Profile, blank=True)
    name = models.CharField(max_length = 1000)
    contest_link = models.CharField(max_length = 1000)
    overview = RichTextUploadingField(null=True, blank=True)
    start_on = models.DateTimeField(default=timezone.now, blank=True)
    end_on = models.DateTimeField(default=timezone.now, blank=True)
    mcq_problems = models.ManyToManyField(McqProblems, blank=True)
    image_link =  models.CharField(max_length = 1000,default= "/static/newtheme/img/test.jpeg" ,blank = True) 
    ACTIVE = 'A'
    PAST = 'P'
    UPCOMING = 'U'
    STATUS = [(ACTIVE, 'Active'), (PAST, 'Past'), (UPCOMING, 'Upcoming')]
    
    def __str__(self):
        return self.name
    
class Event(models.Model):
    When=models.DateTimeField()