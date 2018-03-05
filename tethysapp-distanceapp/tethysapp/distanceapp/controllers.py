from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import RangeSlider
from tethys_sdk.gizmos import TextInput

@login_required()
def home(request):
    """
    Controller for the app home page.
    """


    context = {}

    return render(request, 'distanceapp/home.html', context)

def mapview(request):
    slider1 = RangeSlider(display_text='Time of Day',
                          name='slider1',
                          min='6AM',
                          max='9PM',
                          initial='6AM',
                          step=1)
    text_input = TextInput(display_text='Location Search',
                           name='input',
                           placeholder='e.g.: BYU Clyde Building',
                           prepend='')
    map_button = Button(
        display_text='Calculate',
        name='map-button',
        icon='glyphicon glyphicon-globe',
        style='info',
        attributes={
            'data-toggle': 'tooltip',
            'data-placement': 'top',
            'title': 'Calculate'
        }
    )

    context = {'slider1': slider1,
               'map_button': map_button,
               'text_input': text_input
            }

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