
import requests
import json


response = requests.get("https://search.lib.byu.edu/green/byu/record/lee.383397", verify=False)
obj = json.loads(response.text)
print obj
