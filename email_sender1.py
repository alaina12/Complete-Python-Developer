import smtplib
from email.message import EmailMessage 
# to use strings in email
from string import Template
from pathlib import Path

html = (Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Alaina'
email['to'] = 'mail2alaina@gmail.com'
email['subject']= 'You won 1,000,000 dollars'


email.set_content(html.substitue({'name': 'TinTin'}), 'html')
with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smt:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('19p0017mcc@gmail.com','vwjorjlnujfmpmmc')
	smtp.send_message(email)
	print('all good boss!')