from django.db import models
from django.contrib.auth.models import User
# Create your models here.

JOP_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
) 

class jop(models.Model):
    owenr = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    jop_type = models.CharField(max_length=15, choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='jobs_img/')
    published = models.DateTimeField()
    Vacanacy = models.IntegerField()
    salary = models.IntegerField()
    Experiencse = models.IntegerField()
    category = models.ForeignKey('Categorys', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Categorys(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Aplly(models.Model):
    jobs = models.ForeignKey(jop, verbose_name=("aplly_jop"), on_delete=models.CASCADE)
    name_job = models.CharField(max_length=50)
    email = models.EmailField(max_length=99)
    website = models.URLField()
    cv_job = models.FileField(upload_to='aplly/')
    cover_letter = models.TextField(max_length=500)


    def __str__(self):
        return self.name_job
    
    

