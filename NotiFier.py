import requests
import re
import smtplib
from bs4 import BeautifulSoup
from sms import notifier
import time
#sms
#import urllib2
#import cookielib
#from getpass import getpass
#import sys
#import os
#from stat import *
a = True
reg = ''
while a:
    page = requests.get("http://old.gtu.ac.in/Results.asp")
    print (page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    msg = ''
    columns = soup.findAll(text=re.compile('BE SEM 5'))

    if len(columns) > 0:
        #print "IF LOOP"
        for index in range(len(columns)):
            txt = columns[index]
            msg = msg + txt + '  Declared'
        msg = ' '.join(msg.split())
        if msg == "Result of BE SEM 5 - Regular (DEC 2016) Exam DeclaredResult of BE SEM 5 - Remedial (DEC 2016) Exam Declared":
          notifier(msg)
    print msg
    print time.ctime()
    time.sleep(300)
    
"""   server = smtplib.SMTP('smtp.gmail.com', 587)
         server.starttls()
         server.login("hellohi8878@gmail.com", "hellohi8878")
   
         server.sendmail("hellohi8878@gmail.com", "keyul31@gmail.com", msg)
         server.quit()
         print "Mail Sent"
   #sms
         message = msg
     number = '7096573736'
   print "SMS"
 
         if __name__ == "__main__":    
             username = "8866258602"
             passwd = "27856"

             message = "+".join(message.split(' '))

   #logging into the sms site
             url ='http://site24.way2sms.com/Login1.action?'
             data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

       #For cookies

             cj= cookielib.CookieJar()
             opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    #Adding header details
             opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
         try:
              usock =opener.open(url, data)
         except IOError:
              print "error"
           #return()

              jession_id =str(cj).split('~')[1].split(' ')[0]
            send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
              send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
              opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
         try:
             sms_sent_page = opener.open(send_sms_url,send_sms_data)
         except IOError:
             print "error"
        #return()

         print "success" 
       #return ()
       #sms
"""