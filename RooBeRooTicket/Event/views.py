from django.shortcuts import render
from .models import Event, Sans
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
    # if request.method == 'POST':
    #     current_flight = Flight.objects.get(no=code)
    #     email=request.POST['email']
    #     name=request.POST['name']
    #     lastname=request.POST['lastname']
    #     nationalid=request.POST['nationalid']
    #     seat=request.POST['seat']
    #     # check available seat
    #     if name == '':
    #         return HttpResponse('Error: Name should not be empty')
    #     if int(current_flight.capacity) < int(seat):
    #         return HttpResponse("Error: There is no enough seat. max seat available is :{}".format(current_flight.capacity))
    #     Ticket.objects.create(
    #         flight=current_flight,
    #         name=name,
    #         lastname=lastname,
    #         email = email,
    #         nationalid=nationalid,
    #         seat=seat,
    #         reservation_code=generate_reservation_code()
    #     )
    #     current_flight.capacity = current_flight.capacity - int(seat)
    #     current_flight.save()
    #     f_list = {
    #         'flights' : current_flight,
    #         'flag' : True
    #     }
    #     return render(request, 'flights/detail.html', context=f_list)