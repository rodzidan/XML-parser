import urllib2
import requests
from xml.dom import minidom
from xml.etree import ElementTree
response = urllib2.urlopen("https://search.lib.byu.edu/green/byu/record/lee.383397").read()
#elements = ElementTree.fromstring(response)
#print elements

#response = requests.get("https://search.lib.byu.edu/green/byu/record/lee.383397", stream=True)
# if the server sent a Gzip or Deflate compressed response, decompress
# as we read the raw stream:
#xmldoc = minidom.parse(response)
e = ElementTree.fromstring(response)
print e

#for hold in e.find

#for element in xmldoc.getElementsByTagName('marcHoldings'):
#    marcHolding = element.getElementsByTagName('marcHolding')
#    spans = marcHolding.getElementsByTagName('spans')
#    print spans

#response.raw.decode_content = True

#events = ElementTree.iterparse(response.raw)
#for elem, event in events:
    # do something with `elem`
#    print elem
