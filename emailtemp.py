import smtplib
import datetime

def send_email(recipient):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('reminderofsubscription@gmail.com', 'BronGoated123')
    server.sendmail(
        'reminderofsubscription@gmail.com',
        recipient,
        'this message is from python')

    server.quit()

if datetime.date.today().strftime('%A') == 'Thursday':
    recipient = 'adamsrodgers@etsu.edu'
    send_email(recipient)