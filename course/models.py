from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    course_details = models.TextField()
    thumnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    video = models.FileField()

    def __str__(self):
        return self.name
# primary key = always uniq