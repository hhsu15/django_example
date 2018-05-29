from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Airport, Flight, Passenger
# Create your views here.

# def index(request):
# 	return HttpResponse("Hello World")

# render html
def index(request):
	context = {
	'flights' : Flight.objects.all()
	}
	return render(request, "flights/index.html", context)

def flight(request, flight_id):
	
	try:
		flight = Flight.objects.get(pk=flight_id) #pk = primary key

	except Exception as e:
		raise Http404('Flight does not exist')

	context = {
		"flight": flight,
		"passengers": flight.passenger.all(),
		# get non passengers (ppl who can book), by excluding current flight
		"non_passengers":Passenger.objects.exclude(flights=flight).all(),
	}
	return render(request, "flights/flight.html", context)

def book(request, flight_id):
	try:
		passenger_id = int(request.POST['passenger_selection'])
		passenger = Passenger.objects.get(pk=passenger_id)
		flight = Flight.objects.get(pk=flight_id)
	
	except Exception as e:
		return HttpResponse("There was an error")
    
    # Add the flight
	passenger.flights.add(flight)	

	# redirect to the route named flight (in the urls.py)
    # also pass the args as flight_id
	return HttpResponseRedirect(reverse("flight", args=(flight_id)))
