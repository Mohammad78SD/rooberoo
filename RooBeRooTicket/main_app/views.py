from django.shortcuts import render
from Event.models import Event

# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST['title']
        event = Event.objects.filter(title=title)
        print(event)
        event_list ={
            'events' : event
        }
        
        return render(request, 'events/eventlist.html', context=event_list)
    return render(request, 'main_app/index.html')