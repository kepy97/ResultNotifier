import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendmail(i,result):
	
    """server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("hellohi8878@gmail.com", "hellohi8878")
    msg = result
    msg = msg + str(i)
    server.sendmail("hellohi8878@gmail.com", "keyul31@gmail.com", msg)
    server.quit()
    print('Mail Sent')"""

    #fromaddr = "hellohi8878@gmail.com"
    fromaddr = "keyul31@gmail.com"
    toaddr = "keyulvpatel97@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Result Declared Just Now"
 
    body = result + ' ' + str(i)
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "9879027856")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    toaddr = "meet25197@gmail.com"
    server.sendmail(fromaddr, toaddr,text)
    print('Mail Sent')
    server.quit()