from django import forms
from .models import *


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address_line_1', 'address_line_2', 'city', 'state', 'country')


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'venue', 'meeting_time', 'groupAdmin', 'hashtag', 'users')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_text', 'group', 'user')

