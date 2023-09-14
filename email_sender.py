# making a email sender using python modules
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Alaina umme hafiza'
email['to'] = 'mail2alaina@gmail.com'
email['subject'] = " Hello this is Alana"

email.set_content("I am a python developer!!")

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('19p0017mcc@gmail.com','vwjorjlnujfmpmmc')
	smtp.send_message(email)
	print('all good boss!')

