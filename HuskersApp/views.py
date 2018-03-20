from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    posts = Post.objects.count()
    groups = Group.objects.count()
    members = User.objects.count()
    return render(request, 'HuskersApp/home.html',
                  {'HuskersApp': home,
                  'posts': posts,
                  'groups': groups,
                  'members': members})