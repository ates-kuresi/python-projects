import smtplib, ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


sender = '@sender'
recievers = ['reciever1@anymail.com', 'reciever2@anymail.com']
body_of_email = 'emaildeki yazi deneme'

msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'Baslik-deneme'
msg['Form'] = sender
msg['To'] = ','.join(recievers)


s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port= 465)
s.login(user = sender, password= 'passwd_of_@sender')
s.sendmail(sender, recievers, msg.as_string())
s.quit()
