from pymongo import Connection
from amazon_ses import AmazonSES, EmailMessage
from datetime import datetime
def sendMail(body):

    AccessKeyID = 'AKIAIEE65XFVJKO6HIJA'
    SecretAccessKey = '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'

    amazonSes = AmazonSES(AccessKeyID, SecretAccessKey)

    message = EmailMessage()
    message.subject = 'House hunt'
    message.bodyText = body

    result = amazonSes.sendEmail('amey.r.desai@gmail.com', 'amey.r.desai@gmail.com', message)

connection = Connection('localhost', 27017)
db = connection['craigslist-db']
posts=db.posts
results=[]
	
daily=posts.find({'date':{'$lt':datetime.today().strftime('%Y-%m-%d')}}).sort('date',-1)

for post in daily:
    if 'distance' in post:
        miles=float(post['distance'][:-2])
     	if miles<=6.0:
	    results.append((post['link'],post['rent'],post['distance']))

test=""
for val in results:
    test=test+str(val)+"\n"
print test
sendMail(test)

