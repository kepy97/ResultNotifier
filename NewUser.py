import pymysql
from sms import notifier
from mail import sendmail
import time

conn = pymysql.connect(host='localhost', user='root', passwd='root', db='gtudatabase')
cursor = conn.cursor()
conn.autocommit(True)

sql=("select id from studentdetails")
cursor.execute(sql)
data=cursor.fetchall()

send = "You Have Successfully Registered. You will receive notification when your result will declare.                             From : Kepy"
header = "Successfull Registration"

for row in data:
    pid = row[0]
    print pid

def notification(id):
    try:
        sql=("select emailid from studentdetails where id = " + str(id))
        cursor.execute(sql)
        data=cursor.fetchall()
        
        for row in data:
            print row[0]
            sendmail(send,row[0],header)
    except Exception as e:
        print " Error Found IN SENDING MAIL " + str(e)

    try:
        sql=("select mobile from studentdetails where id = " + str(id) )
        cursor.execute(sql)
        data=cursor.fetchall()

        for row in data:
            print row[0]
            notifier(send,row[0])
    except Exception as e:
        print " Error Found IN SENDING SMS " + str(e)

loop = True
while loop:
    cursor.execute("select * from studentdetails")
    data = cursor.fetchall()
    for row in data:
        if(row[0]>pid):
            notification(row[0])
            pid = row[0]
            print row[0]
    print time
    time.sleep(15)
