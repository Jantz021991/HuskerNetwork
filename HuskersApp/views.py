from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'HuskersApp/home.html',
                  {'HuskersApp': home})


def group(request):
    return render(request, 'HuskersApp/group.html',
                  {'HuskersApp': group})


def venue(request):
    return render(request, 'HuskersApp/venue.html',
                  {'HuskersApp': venue})

def feed(request):
    return render(request, 'HuskersApp/feed.html',
                  {'HuskersApp': feed})


def venue_detail(request):
    return render(request, 'HuskersApp/venue_detail.html',
                  {'HuskersApp': venue_detail})