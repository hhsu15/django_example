 
from django.urls import path
from . import views

urlpatterns = [
    # when user goes to the route "", run views.index
    path("",views.index),
    path("<int:flight_id>", views.flight)
]
