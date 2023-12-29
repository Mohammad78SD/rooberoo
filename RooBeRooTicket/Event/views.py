from django.shortcuts import render

# Create your views here.


# define list to render events lists html page
def list(request):
    return render(request, 'flights/eventlist.html')