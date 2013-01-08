import urllib2
from time import sleep
from pymongo import Connection
from BeautifulSoup import BeautifulSoup

def getLocationFromSource(soup):
    ultag=soup.find('ul',{'class':'blurbs'})
    if ultag is not None:
        litags=ultag.findAll('li')
        for litag in litags:
	    if 'Location:' in litag.text:
	        return litag.text.split("Location:")[1]


connection = Connection('localhost', 27017)
db = connection['craigslist-db']
posts=db.posts

for post in posts.find():
    temp={}
    request=urllib2.Request(post['link'])
    temp['link']=post['link']
    sleep(0.1)
    page=urllib2.urlopen(request)
    location=getLocationFromSource(BeautifulSoup(page))
    if location is not None:
        posts.update(temp,{"$set":{"location":location}})    
   

