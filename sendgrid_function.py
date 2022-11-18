import json
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_account_verification_email(send_from, send_to, subject, receiver_name, verification_link):

    try:
        message = Mail(
            from_email=send_from,                                 
            to_emails=send_to,
            subject=subject,
            html_content='<p>Hi ' + str(receiver_name) + ',</p><p>Please click the below link to verify your account.</p><a href="' + str(verification_link) + '">Verfication Link</a></p><p>Thank you!</p>')
        
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        
        response = sg.send(message)

        print('Using SendGrid API E-Mail send ')
        print( response)
        print( 'SendGrid Status code:')
        print(response.status_code)
        print( 'SendGrid body:')
        print(response.body)
        print( 'SendGrid header:')
        print(response.headers)
        
        return response

    except Exception as e:
        print("inside exception")
        print(e)