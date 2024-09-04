#import smtplib
#mail = 'bartek.test.97@gmail.com'
#password = 'vsmt nnix jzwd vxgx'
#
#
#with  smtplib.SMTP("smtp.gmail.com") as connection: #Remeber to change the security options!!!
#    connection.starttls()
#    connection.login(user=mail, password=password)
#    connection.sendmail(from_addr=mail, to_addrs='bartek.yest@yahoo.com', msg='Subject:Hello\n\nThis is body of the mail')
    
#import datetime as dt
#
#now = dt.datetime.now()
#print(now)
#
#date_of_birth = dt.datetime(year=1997, month=9, day=15)
#print(date_of_birth)

import smtplib
import datetime as dt
import random

mail = 'bartek.test.97@gmail.com'
password = 'vsmt nnix jzwd vxgx'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open ('/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day032_Mailing/quotes.txt') as quotes_file:
        quotes = quotes_file.readlines()
        selected = random.choice(quotes)
        
    print(selected)       
    with  smtplib.SMTP("smtp.gmail.com") as connection: #Remeber to change the security options!!!
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail, to_addrs='bartek.yest@yahoo.com', msg='Subject:Motivation\n\nHere is your motivation: {}'.format(selected))


