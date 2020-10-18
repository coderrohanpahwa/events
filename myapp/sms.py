# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc2a7e10a8a382fc0595bd51a422de800'
auth_token = 'f18bdea1f1a01950eb1c792866a0e96d'


message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15712235121',
                     to='+918221988235'
                 )

print(message.sid)
def send_sms(account_sid,account_token,body,from_,to):
    from twilio.rest import Client
    message = client.messages \
        .create(
        body=body,
        from_=from_,
        to=to
    )

