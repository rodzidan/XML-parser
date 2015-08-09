from app import app
# imports 
# requests - library for http requests
import requests
# json - library to create and parse json objects
import json

# function which finds the start year from a list of spans, given that some spans may not conatin a year
# @param spans - the list of spans
# @return firstYear the first year for the span
def getFirstYearFromSpans(spans):
	firstYear = 0
	# iterate over the spans 
	for span in spans:
		# check for a year key in the start element
		# if the year key is present use it store the start date
		if 'year' in span['start']:
			firstYear = span['start']['year']
			break	
	# return the start date 
	return firstYear


# function which returns the run for a given holding via its URI
# @param uri - the uri for the holdings
# @return Array - array containing the start and end year for the holding
def getHoldings(uri):
	# Make http request and then assign reposne to var response.
	# Code will not continue executino until response is saved
	response = requests.get(uri, verify=False)

	# jsonResponse - the json returned from the http request as a json Object 
	jsonResponse = json.loads(response.text)

	# get all the spans and find the first span with a start year
	
	spans = jsonResponse['holdings'][0]['marcHoldings'][0]['spans']
	
	# find the first year 
	
	firstYear = getFirstYearFromSpans(spans)	

	#get the latest year

	# first get the length of the holdings
	length = len(jsonResponse['holdings'][0]['marcHoldings'][0]['spans'])

	# then get the last year by the index from length
	latestYear = jsonResponse['holdings'][0]['marcHoldings'][0]['spans'][length-1]['end']['year']
	#latestYear = latestYearSpan['end']['year']

	# make array for result
	result = [firstYear, latestYear]
	
	# return result
	return result

# function to build a json response from three arrays 
# @param arr1 array 
# @param arr2 array
# @param arr3 array
# @return jsonObject json object representatino for the three arrays
def buildJsonResponseFromArrays(arr1, arr2, arr3):
	jsonObject = {}
	jsonObject['Time'] = arr1
	jsonObject['Journal of african earth science (and middle east).'] = arr2
	jsonObject['Communications from the international Brecht Society'] = arr3
	return jsonObject
	

# test function 
#print getHoldings("https://search.lib.byu.edu/green/byu/record/lee.383397.json")
#print getHoldings("https://search.lib.byu.edu/green/byu/record/lee.633102.json")
#print getHoldings("https://search.lib.byu.edu/green/byu/record/lee.1586992.json")

@app.route('/')
@app.route('/index')
def index():
	result1 =  getHoldings("https://search.lib.byu.edu/green/byu/record/lee.383397.json")		
	result2 = getHoldings("https://search.lib.byu.edu/green/byu/record/lee.633102.json")
	result3 =  getHoldings("https://search.lib.byu.edu/green/byu/record/lee.1586992.json")
	return json.dumps(buildJsonResponseFromArrays(result1, result2, result3))
