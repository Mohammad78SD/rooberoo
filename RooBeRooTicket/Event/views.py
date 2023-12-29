from django.shortcuts import render
from .models import Event
# Create your views here.


# define list to render events lists html page
def event_list(request):
    events = Event.objects.all()
    eventlist = {
        'events' : events
    }
    return render(request, 'events/eventlist.html', context= eventlist)