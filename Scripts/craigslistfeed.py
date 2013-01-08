import feedparser
import re
import os
import sqlite3
from pymongo import Connection


craigslistfeed=feedparser.parse('http://saltlakecity.craigslist.org/apa/index.rss')
rent=800
values=[]

def getDollarValue(value):
    dollarValue=re.search('\$(\d+)',value)
    if not dollarValue:
	return rent+1
    return int(dollarValue.group(1))	

idDB="database/idvalues.db"
#idDB="../database/idvalues.db"
connectionsql=sqlite3.connect(idDB)
cursor=connectionsql.cursor()
cursor.execute("Select * from id")
ids=cursor.fetchall()


for entry in craigslistfeed.entries:
    rows={}	    
    title=entry["title"].encode('ascii','ignore')
    dollarValue=getDollarValue(title)
    if dollarValue:
    	if dollarValue <=rent:
	   entryId=os.path.splitext(entry["id"].encode('ascii','ignore').split("/")[-1])[0]
	   if entryId in ids:
	       continue
	   cursor.execute('INSERT INTO id VALUES(?)',(entryId,))
	   rows["id"]=entryId
	   rows["rent"]=dollarValue
           rows["title"]=title
	   rows["summary"]=entry["summary"].encode('ascii','ignore')		
	   rows["link"]=entry["link"].encode('ascii','ignore')			
	   rows["date"]=entry["updated"].encode('ascii','ignore')[0:10]
  	   values.append(rows)

connectionsql.commit()
cursor.close()
connection = Connection('localhost', 27017)
db = connection['craigslist-db']
posts=db.posts
posts.insert(values)


	
	


