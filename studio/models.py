from django.db import models


GENDER = (
    ('male','male'),
    ('female','female'),
    ('other','other'), 
)


class Singer(models.Model):
    singer_name = models.CharField(max_length = 155)
    gender = models.CharField(max_length=10, choices=GENDER, default = 'male')
    nationality = models.CharField(max_length = 155)
    has_been_nominated = models.BooleanField(default = False)
    
    def __str__(self):
        return self.singer_name


class Band(models.Model):
    band_name = models.CharField(max_length=20)
    # members = 


class Song(models.Model):
    song_name = models.CharField(max_length=155)
    release_date = models.DateField()
    total_views = models.BigIntegerField()
    
    # a song can be sung by many singers (feats)
    singers = models.ManyToManyField(Singer)
    
    def __str__(self):
        return self.song_name
    

class Album(models.Model):
    album_name = models.CharField(max_length=20)
    release_date = models.DateField()
    #album_songs =  
    
