from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address_line_1', 'address_line_2', 'city', 'state', 'country')


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'venue', 'meeting_time','group_details', 'groupAdmin', 'hashtag', 'users')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_text', 'group', 'user')

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=60, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', )

    # def clean_password2(self):
    #     '''Check if both password matches'''
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password2']
