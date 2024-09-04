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
import pandas

#mail = 'bartek.test.97@gmail.com'
#password = 'vsmt nnix jzwd vxgx'
#
#now = dt.datetime.now()
#weekday = now.weekday()
#if weekday == 2:
#    with open ('/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day032_Mailing/quotes.txt') as quotes_file:
#        quotes = quotes_file.readlines()
#        selected = random.choice(quotes)
#        
#    print(selected)       
#    with  smtplib.SMTP("smtp.gmail.com") as connection: #Remeber to change the security options!!!
#        connection.starttls()
#        connection.login(user=mail, password=password)
#        connection.sendmail(from_addr=mail, to_addrs='bartek.yest@yahoo.com', msg='Subject:Motivation\n\nHere is your motivation: {}'.format(selected))
#  


mail = 'bartek.test.97@gmail.com'
password = 'vsmt nnix jzwd vxgx'

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv('/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day032_Mailing/birthdays.csv')
birthday_dict = {(row['month'], row['day']): row for index, row in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f'/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day032_Mailing/letter_templates/letter_{random.randint(1,3)}.txt'

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])
    
    # Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        message = f'Subject: Happy Birthday\n\n{contents}'
        connection.sendmail(from_addr=mail, to_addrs=birthday_person['email'], msg=message)
