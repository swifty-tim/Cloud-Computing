# cant use / and not using quotes


import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import requests
import sys, json

res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')

result = res.text

mylist = result.split(':')

argList = sys.argv
try:
    data = argList[1]
except:
    print "ERROR"
    sys.exit(1)
    
queue = 'C13720705'+data    

# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = mylist[0]
secret_access_key = mylist[1]


# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

c = conn.create_queue(queue, 120)

print 'queue '+ c.id+ ' is now created'


# Get a list of the queues that exists and then print the list out
# rs = conn.get_all_queues()
# for q in rs:
# 	print q.id
#  