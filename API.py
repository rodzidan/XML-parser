# imports 
# requests - library for http requests
import requests
# json - library to create and parse json objects
import json

# Make http request and then assign reposne to var response.
# Code will not continue executino until response is saved
response = requests.get("https://search.lib.byu.edu/green/byu/record/lee.383397.json", verify=False)

# jsonResponse - the json returned from the http request as a json Object 
jsonResponse = json.loads(response.text)
print jsonResponse
