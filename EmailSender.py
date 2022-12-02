import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_address = ''
sender_pass = ''


def send(personFrom, personTo):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = personFrom.email
    message['Subject'] = '🎁Secret Santa 2022!'

    email_content = 'Your person is ' \
                    + personTo.name + '! Marry Christmas!🎄'


    message.attach(MIMEText(email_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(message['From'], message['To'], text)
    session.quit()

    print('SENT TO: ' + personFrom.email)
