import smtplib, ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from myMailAuth import * # This is for hide my informations


sender = myMail
recievers = ['ateskuresiz@gmail.com', '']
body_of_email = 'emaildeki yazi deneme'

msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'Baslik-deneme'
msg['Form'] = sender
msg['To'] = ','.join(recievers)


s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port= 465)
s.login(user = sender, password= myPasswd)
s.sendmail(sender, recievers, msg.as_string())
s.quit()
