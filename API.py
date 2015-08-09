# imports 
# requests - library for http requests
import requests
# json - library to create and parse json objects
import json



def getHoldings(uri):
	# Make http request and then assign reposne to var response.
	# Code will not continue executino until response is saved
	response = requests.get(uri, verify=False)

	# jsonResponse - the json returned from the http request as a json Object 
	jsonResponse = json.loads(response.text)

	# get the first year 
	firstYear = jsonResponse['holdings'][0]['marcHoldings'][0]['spans'][0]['start']['year']

	#get the latest year

	# first get the length of the holdings
	length = len(jsonResponse['holdings'][0]['marcHoldings'][0]['spans'])

	# then get the last year by the index from length
	latestYear = jsonResponse['holdings'][0]['marcHoldings'][0]['spans'][length-1]['start']['year']

	# make array for result
	result = [firstYear, latestYear]
	
	# return result
	return result
	

# test function 
print getHoldings("https://search.lib.byu.edu/green/byu/record/lee.383397.json")


