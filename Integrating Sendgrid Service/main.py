import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


def send_email():
    from_email = Email('dhevaponnarasan@gmail.com')
    to_email = To('selvatarshini@gmail.com')
    subject = 'Sending with Sendgrid'
    content = Content("Hi selva", "Hope you doing well")
    mail = Mail(from_email, to_email, subject, content)

    try:
        sg = SendGridAPIClient('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')
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


send_email()