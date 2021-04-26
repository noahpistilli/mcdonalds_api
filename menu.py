import json
import requests


def breakfast():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100001.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def beef():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100005.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def chicken():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100007.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def sandwiches():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100014.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def salad():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100004.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result
	

def sides():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100006.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def desserts():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100003.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def beverages():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100000.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def mccafe():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100008.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def valuepicks():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100015.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def happymeals():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100009.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result


def condiments():
	food = requests.get('https://www.mcdonalds.com/services/mcd/categoryDetails.ca.en-ca.100002.true.true..false.json')
	get_json = food.json()
	
	result = json.dumps(get_json)
	
	return result
