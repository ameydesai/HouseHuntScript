from amazon_ses import AmazonSES, EmailMessage
import datetime
AccessKeyID = 'AKIAIEE65XFVJKO6HIJA'
SecretAccessKey = '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'

amazonSes = AmazonSES(AccessKeyID, SecretAccessKey)

message = EmailMessage()
message.subject = 'Hello from Amazon SES! Test subject'
message.bodyText = 'This is body text of test message.'

val=datetime.date.today()
print val,type(val)

#result = amazonSes.sendEmail('amey.r.desai@gmail.com', 'amey.r.desai@gmail.com', message)    
print result.requestId
print result.messageId
