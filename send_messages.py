from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "AC388d08c36de5ff26c2fd8acacbb8aad8"
AUTH_TOKEN = "b308a23efb875b24021dedfd16b760cf"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def send_message(message_body, phone):
    message = client.messages.create(
        body=message_body+" You can reach them at 412-961-5899",  # Message body, if any
        to=phone,
        from_="+16307565499",
    )
