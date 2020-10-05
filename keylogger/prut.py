import smtplib
import time 
from time import sleep 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders


def send_to():

    sender = "sender_email"
    receiver = "receiver_email"
    
   
    msg = MIMEMultipart() 
    
    
    msg['From'] = sender
    
   
    msg['To'] = receiver
    

    msg['Subject'] = "High-tech,low-life"
    

    body = "See_you_space_cowboy"
    

    msg.attach(MIMEText(body, 'plain')) 
    
   
    filename = "FILE_NAME"
    attachment = open(r"PATH_TO_FILE", "rb") 
    
   
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    
 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls() 
    

    s.login(sender, "SENDER_MAIL_PASSWORD") 
    text = msg.as_string() 
    s.sendmail(sender, receiver, text) 
    
    s.quit() 