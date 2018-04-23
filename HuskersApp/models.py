from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import requests


# Models for Huskers Network

class Venue(models.Model):
    name = models.CharField(max_length=200)
    address_line_1 = models.CharField(max_length=500)
    address_line_2 = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def venue_weather(self):
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=1c20b22acd0d5d1f853c04e0bcc77011&q='
        city = str(self.city)
        url = api_address + city
        res = requests.get(url).json()
        # cityId = res.id
        return res



class Group(models.Model):
    name = models.CharField(max_length=200)
    venue = models.ForeignKey(Venue, related_name='group_venue')
    meeting_time = models.TimeField()
    group_details = models.CharField(max_length=500, null=True)
    groupAdmin = models.ForeignKey(User, related_name='group_admin')
    hashtag = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)



class Post(models.Model):
    post_text = models.TextField(max_length=None)
    group = models.ForeignKey(Group, related_name='group_post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_post')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_text


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(max_length=8, blank=True)
    favorite_team = models.CharField(max_length=100, blank=True)
    current_location = models.CharField(max_length=100, blank=True)
    introduction = models.TextField(max_length=500, blank=True)





