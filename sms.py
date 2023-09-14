#This sms project will help in sending sms using python 
#twillio is the libraray to be used 
from twilio.rest import Client

account_sid = 'AC096730fd885a440bd82c6fe8551bcffd'
auth_token = '26ba430ddc2d374ef00b5d54b9ffc3a7'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14302434939',
  body='Dear mom, never be sad Your such a beautiful lady, So always be smiling!!',#any message to be convyed
  to='+919964******'#number of the reciever
)

print(message.sid)