from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import glob
import smtplib
import zomatopy

ZomatoData = pd.read_csv('zomato.csv',encoding='latin1')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['Ahmedabad','Bangalore','Chennai','Delhi NCR','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer',
'Aligarh','Allahabad','Amravati','Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi',
'Bhopal','Bhubaneswar','Bikaner','Bokaro Steel City','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad',
'Durg-Bhilai Nagar','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur',
'Gurgaon','Guwahati‚ Gwalior','Hubli-Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur',
'Jhansi','Jodhpur','Kannur','Kanpur','Kakinada','Kochi','Kottayam','Kolhapur','Kollam','Kota','Kozhikode','Kurnool',
'Lucknow','Ludhiana','Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik',
'Nellore','Noida','Palakkad','Patna','Pondicherry','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Siliguri',
'Solapur','Srinagar','Sultanpur','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tirunelveli','Tiruppur','Ujjain','Vijayapura',
'Vadodara','Varanasi','Vasai-Virar City','Vijayawada','Visakhapatnam','Warangal']

city_dict = [x.lower() for x in WeOperate]

##Validating Location
def Check_Location(loc, city_names= city_dict):  
	config={"user_key":"337f3a03601af0bbcc30b2e3506be18d"}
	zomato = zomatopy.initialize_app(config)
	location_detail=zomato.get_location(loc, 1)
	location_json = json.loads(location_detail)
	number_of_loc = len(location_json['location_suggestions'])

	try:
		if number_of_loc == 0:
			return {'location_result': False, 'location_name': None}
		elif (location_json['location_suggestions'][0]['city_name']).lower() not in city_dict:
			return {'location_result': False, 'location_name': None}
		else:
			return {'location_result': True, 'location_name': location_json['location_suggestions'][0]['city_name']}
	except:
		dispatcher.utter_message("Sorry, please enter a valid request!")

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):

		loc = tracker.get_slot('location')
		check= Check_Location(loc)

		return[SlotSet('check_loc',check['location_result']), SlotSet('location',check['location_name'])]

# Finding top restaurants
def results(loc,cuisine,price):
	config={"user_key":"337f3a03601af0bbcc30b2e3506be18d"}
	zomato = zomatopy.initialize_app(config)
	location_detail=zomato.get_location(loc, 1)
	location_json = json.loads(location_detail)
	location_results = len(location_json['location_suggestions'])
	lat=location_json["location_suggestions"][0]["latitude"]
	lon=location_json["location_suggestions"][0]["longitude"]
	city_id=location_json["location_suggestions"][0]["city_id"]
	cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85, 'thai': 95}
		 
		
	list1 = [0,20,40,60,80]
	d = []
	df = pd.DataFrame()
	for i in list1:
		results = zomato.restaurant_search("", lat, lon, cuisine, limit=i)
		d1 = json.loads(results)
		d = d1['restaurants']
		df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
		 'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
		 'restaurant_address': x['restaurant']['location']['address'],
		 'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d])
		df = df.append(df1)

	if price == 'Less than Rs.300':
		min_val = 0
		max_val = 300
	elif price == '300-700':
		min_val = 301
		max_val = 700
	else:
		min_val = 701
		max_val = 10000000

	#sorting by review & filter by budget
	df = df[(df['budget_for2people'] >= min_val) & (df['budget_for2people'] <= max_val)]
	df = df.sort_values(by='restaurant_rating', ascending=False)

	return df

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')

		glob.restaurants = results(loc, cuisine, price)

		glob.restaurants = glob.restaurants.drop_duplicates()
		top5 = glob.restaurants.head(5)
		print(top5)

		if len(top5) == 0:
			response= "no results"
		else:
			response = 'Showing you top results:' + "\n"
			for index, row in top5.iterrows():
				response = response + str(row["restaurant_name"]) + ' (rated ' + row['restaurant_rating'] + ') in ' + row['restaurant_address'] + ' and the average budget for two people ' + str(row['budget_for2people'])+"\n"
				
		dispatcher.utter_message(str(response))
		return [SlotSet('location',loc)]

# Sending Mail
class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		recipient = tracker.get_slot('email')

		top5 = glob.restaurants[:5]
		response = 'Showing you top results:' + "\n"
		for idx, row in top5.iterrows():
			response = response + 'Restaurant Name: ' + str(row["restaurant_name"]) + "\n" + 'User Rating: ' + row[
				'restaurant_rating'] + "\n" + 'Address : ' + row[
						   'restaurant_address'] + "\n" + 'Average Budget for two people ' + str(
				row['budget_for2people']) + "\n\n"

		user = "zomatobot.assign@gmail.com"
		password = "zomato123"
		sent_from = user
		to = tracker.get_slot('email')
		subject = " Restaurant recommendations in " + tracker.get_slot("location").title()

		email_text = """\  
					From: %s  
					To: %s  
					Subject: %s
					%s
					""" % (sent_from, to, subject, response)
		print(email_text)

		try:
			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.ehlo()
			server.login(user, password)
			server.sendmail(sent_from, to, email_text)
			server.close()
			print(response)
			dispatcher.utter_message("Message sent.Have a great day!")

		except:

			dispatcher.utter_message("Unfortunately I am not able to send email!!!")
		
		return [SlotSet('email',to)]