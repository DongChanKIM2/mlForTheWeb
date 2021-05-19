from django.db import models
from django.contrib.auth.models import User
import json
# from jsonfield import JSONfield
import sqlite3
from django.db.models.deletion import CASCADE
import numpy as np


# Create your models here.
# 나와 내가 평가하는 영화들을 저장할 class
# 우선 django의 기본적인 기능만 사용할 거니까 User(AbstractUser를 상속받은) 사용
# array: 내가 평가한 영화들 평점
# arrayratedmoviesindex: 내가 평가한 영화들 index
# lastrecs: 나한테 추천할 영화(마지막 순서)
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, unique=True)
    array = models.TextField()
    # array = jsonfield.JSONField()
    arrayratedmoviesindxs = models.TextField()
  
    name = models.CharField(max_length=1000)
    lastrecs = models.TextField()
  


    def save(self, *args, **kwargs):
        create = kwargs.pop('create', None)
        recsvec = kwargs.pop('recsvec', None)
        if create==True:
            super(UserProfile, self).save(*args, **kwargs)
        elif recsvec!=None:
             self.lastrecs = json.dumps(recsvec.tolist())
             super(UserProfile, self).save(*args, **kwargs)
        else:
            nmovies = MovieData.objects.count()
            array = np.zeros(nmovies)
            ratedmovies = self.ratedmovies.all()
            self.arrayratedmoviesindxs = json.dumps([m.movieindx for m in ratedmovies])
            for m in ratedmovies:
                array[m.movieindx] = m.value
            self.array = json.dumps(array.tolist())
            super(UserProfile, self).save(*args, **kwargs)
    

class MovieRated(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=CASCADE, related_name='ratedmovies')
    movie = models.CharField(max_length=100)
    movieindx = models.IntegerField(default=-1)
    value = models.IntegerField()


class MovieData(models.Model):
    title = models.CharField(max_length=100)
    array = models.TextField()
    # array = jsonfield.JSONField()
    ndim = models.IntegerField(default=300)
    description = models.TextField()
