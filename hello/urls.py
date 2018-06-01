 
from django.urls import path
from . import views

urlpatterns = [
    # when user goes to the route "", run views.index
    path("",views.index, name='index'),
    path("<int:flight_id>", views.flight, name='flight'),
    path("<int:flight_id>/book", views.book, name='book'),
    path("user_index", views.user_index, name='user_index'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),


]
