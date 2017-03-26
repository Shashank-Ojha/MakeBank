from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "AC388d08c36de5ff26c2fd8acacbb8aad8"
AUTH_TOKEN = "b308a23efb875b24021dedfd16b760cf"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Hello Monkey!",  # Message body, if any
    to="+16309080289",
    from_="+16307565499",
)
print (message.sid)