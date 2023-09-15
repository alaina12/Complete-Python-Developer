#This sms project will help in sending sms using python 
#twillio is the libraray to be used 
from twilio.rest import Client

account_sid = 'add the wuthentication id'
auth_token = 'add the authentiction token'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14302434939',
  body='Dear mom, never be sad Your such a beautiful lady, So always be smiling!!',#any message to be convyed
  to='+919964******'#number of the reciever
)

print(message.sid)
