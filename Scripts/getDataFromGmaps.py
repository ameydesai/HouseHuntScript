import simplejson
import urllib2
import urllib
from pymongo import Connection


connection = Connection('localhost', 27017)
db = connection['craigslist-db']
posts=db.posts
url1="http://maps.googleapis.com/maps/api/directions/json?origin=40.765023,-111.848931&"
url2="&sensor=false&alternatives=true&mode=walking"
collection=db["location"]

def checkExistingLocation(collection,location):
    for value in collection.find():
	if location in value:
	    return True
    return False

for post in posts.find():
    if 'location' not in post:
	continue
    location=str(post['location'])
    if 'UT' not in location:
	temp={}
	temp['link']=post['link']
	location=location.replace('.','')+" UT"
	existing=checkExistingLocation(collection,location)
	if not existing:
            destParams={"destination":location}        
            url=url1+urllib.urlencode(destParams)+url2       
	    result=simplejson.load(urllib2.urlopen(url))
	    if result['routes']:
	        legs=result['routes'][-1]
	        distance=legs['legs'][0]['distance']
                value=distance['text'].replace(",","")
	        posts.update(temp,{"$set":{"distance":value}},upsert=True)
                collection.insert({location:value})


 
		       
	


