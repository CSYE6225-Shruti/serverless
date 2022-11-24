import json
import sendgrid_function

SENDER = "shruti@demo.devshrutisutrawe.me"

def lambda_handler(event_message, context):
    
    print("From SNS event message: ") 
    print(event_message)
    
    event = json.loads(event_message['Records'][0]['Sns']['Message'])
    # event = event_message['Records'][0]['Sns']['Message']
    
    print("Seggregated event: ")
    print(event)
    
    recipient_email = event['recipient_email']
    recipient_name = event['recipient_name']
    verification_link = event['verification_link']
    
    subject = 'CSYE6225 Verification mail'
            
    response = sendgrid_function.send_account_verification_email(SENDER, recipient_email, subject, recipient_name, verification_link)
    return {
        'statusCode': 200,
        'body': response.body
    }