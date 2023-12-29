from django.urls import path
from .views import event_list, detail

urlpatterns = [
    path("list", event_list, name = "event_list"),
    path('<str:code>', detail, name='detail'),
]