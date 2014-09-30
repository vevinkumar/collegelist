from django.db import models

class UserList(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.user_name

class CollegeList(models.Model):
    college_id = models.CharField(max_length=20)
    college_name = models.CharField(max_length=200)
    district = models.CharField(max_length=50)
    image1 = models.CharField(max_length=200)
    image2 = models.CharField(max_length=200)
    image3 = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.college_id