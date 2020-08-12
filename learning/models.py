from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.

class Cours(models.Model):
    title = models.CharField(max_length=50)
    free = models.IntegerField()
    available_seats = models.IntegerField()
    _schedule = models.CharField(max_length=100, db_column='schedule')
    picture = models.ImageField(upload_to='cours', default='default.jpg')
    objectives = models.TextField()
    eligibility = models.TextField()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name='cours')


    @property
    def schedule(self):
        s = json.loads(self._schedule)
        return f'{s[0]}.00 pm to {s[1]}.00 pm'


class Sections(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    cour = models.ForeignKey(Cours, on_delete=models.CASCADE)


class Pages(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)

class Expoilted(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='exploited')
    type = models.CharField(max_length=50, choices=(('T','Teacher'),('S','Student')))

