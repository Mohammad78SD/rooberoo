from django.shortcuts import render,HttpResponse
from Event.models import Event
from channels.layers import get_channel_layer

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
    return render(request, 'main_app/index.html',{
        'room_name':"broadcast"
    })
from asgiref.sync import async_to_sync
def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type':'send_notification',
            'message':"Notification"
        }
    )
    return HttpResponse("Done")