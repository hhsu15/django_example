from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Airport, Flight
# Create your views here.

# def index(request):
# 	return HttpResponse("Hello World")

# render html
def index(request):
	context = {
	'airports' : Airport.objects.all()
	}
	return render(request, "flights/index.html", context)

def flight(request, flight_id):
	
	try:
		flight = Flight.objects.get(id=flight_id) #pk = primary key

	except Exception as e:
		raise Http404('Flight does not exist')

	context = {
		"flight": flight
	}
	return render(request, "flights/flight.html", context)
