from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.http import HttpResponse
from .serializers import *

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


@login_required
def venue_list(request):
    """
    List All Venues 
    """
    venues = Venue.objects.all()
    serializer = VenueSerializer(venues, many=True)
    return render(request, 'HuskersApp/venue_list.html',
                    {'venues': venues})
       

@login_required
def venue_edit(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    if request.method == 'POST':
        form = VenueForm(request.POST, instance=Venue)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.updated_date = timezone.now()
            venue.save()
            venue = Venue.objects.filter(created_date__lte=timezone.now())
            return render(request, 'HuskersApp/venue_list.html',
                            {'venue': venue})

    else:
        form = VenueForm(instance=venue)
    return render(request, 'HuskersApp/venue_edit.html',
                {'form': form})


@login_required
def venue_new(request):
    """
    Add a new Venue
    """
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.created_date = timezone.now()
            venue.save()
            venues = Venue.objects.filter(created_date__lte=timezone.now())
            return render(request, 'HuskersApp/venue_list.html',
                            {'venues': venues})

    else:
        form = VenueForm
    return render(request, 'HuskersApp/venue_new.html',
                    {'form': form})


@login_required
def venue_delete(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    venue.delete()
    return redirect('HuskersApp/venue_list.html')
