from django.shortcuts import render, HttpResponse
from .models import Event, Sans, Ticket, User
# Create your views here.


# define list to render events lists html page
def event_list(request):
    events = Event.objects.all()
    eventlist = {
        'events' : events
    }
    return render(request, 'events/eventlist.html', context= eventlist)


def detail(request, code):
    if request.method == 'GET':
        event = Event.objects.get(pk = code)
        sans = Sans.objects.filter(event = event)

            
        context = {
            'event' : event,
            'sanslist' : sans, 
            'flag' : False
        }
        return render(request, 'events/details.html', context=context)
    
    
    if request.method == 'POST':
        current_event = Event.objects.get(pk = code)
        user_name = request.POST.get('user_name')
        user = User.objects.get(name = user_name)
        quantity = request.POST.get('quantity')
        sans_id = request.POST.get('sans_id')
        sans = Sans.objects.get(pk=sans_id)
        if user == '':
            return HttpResponse('Error: Name should not be empty')
        if int(sans.free_capacity) < int(quantity):
            return HttpResponse("Error: There is no enough seat. max seat available is :{}".format(sans.free_capacity))
        ticket = Ticket.objects.create(user=user, quantity=quantity, sans=sans)
        sans.free_capacity -= int(quantity)
        sans.save()
        sanses = Sans.objects.filter(event = current_event)
        context = {
            'event' : current_event,
            'sanslist' : sanses, 
            'flag' : True
        }
        return render(request, 'events/details.html', context=context)