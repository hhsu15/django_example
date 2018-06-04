from django.test import TestCase, Client
from .models import Flight, Airport
from selenium import webdriver


# set up the chromedriver path - shold be an easier way
#---this is not needed------
# chromeoptions = webdriver.ChromeOptions()
# pref = {'download.default_directory':'/Users/jessicatung'}
# chromeoptions.add_experimental_option('prefs', pref)

#--this is needed but doesn't work with Javis so commetting out
"""
chromedriver = './chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver)
"""

# Create your tests here.
def file_uri(filename):
	"""return url for file"""
	return 'http://127.0.0.1:8000/' + filename

class ModelsTestCase(TestCase):

	# To set up the fake data in the models
	def setUp(self):
		a1 = Airport.objects.create(code="aaa", city='city_a')
		a2 = Airport.objects.create(code='bbb', city='city_b')

		Flight.objects.create(origin=a1, destination=a2, duration=500)
		Flight.objects.create(origin=a2, destination=a1, duration=500)

	def test_departure_count(self):
		# test departure(from the related_name) count for a given airport
		a = Airport.objects.get(city='city_a')
		self.assertEqual(a.departures.count(), 1)

	def test_index(self):
		# test index function to simulate when user go into the index route
		client = Client()
		res = client.get('/')
		self.assertEqual(res.status_code, 200)
		self.assertEqual(res.context['flights'].count(),2)
    
 #    #---commet out for now since it doesn't work on Javis
	# def test_web_page(self):
	# 	"""Test web browser using selenium
	# 	"""
	# 	flight_url = 'http://127.0.0.1:8000/3'
	# 	driver.get(flight_url)
	# 	header = driver.find_element_by_tag_name('h1')
	# 	self.assertEqual(header.text, 'This is my Django Project')