from django.db import models

class Course(models.Model):
    #id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    language = models.CharField(max_length=100)
    duration=models.DurationField()
    description = models.TextField(null=True,blank=True)
    Coefficient=models.FloatField()
    startDate=models.DateField(auto_now_add=True)
    photo=models.ImageField(upload_to='course_photos',blank=True)


