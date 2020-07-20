import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mail_content='''
{}
'''

with open('monitored.html','r') as fp:
	mail_content=mail_content.format(fp.read())

#sender='systembug100@gmail'
sender=<Put your mail id>
#receiver=<Put your receiver mail id>
password=<Put your sender mail id password>

message=MIMEMultipart()
message['From']=sender
message['To']=receiver
message['Subject']='Test Mail - Mount Monitoring'

#print(mail_content)

part1=MIMEText(mail_content,'html')
message.attach(part1)

session=smtplib.SMTP('smtp.gmail.com',587)
session.sendmail(sender,receiver,message.as_string())
