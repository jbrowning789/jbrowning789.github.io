from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """


    context = {
    }

    return render(request, 'distanceapp/home.html', context)

def mapview(request):

    context = {}

    return render(request, 'distanceapp/mapview.html', context)


def dataservices(request):
    context = {
    }

    return render(request, 'distanceapp/dataservices.html', context)


def about(request):
    context = {
    }

    return render(request, 'distanceapp/about.html', context)

def proposal(request):
    context = {
    }

    return render(request, 'distanceapp/proposal.html', context)

def mockup(request):
    context = {
    }

    return render(request, 'distanceapp/mockup.html', context)