# Download the Python helper library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC27ee1c3ad33b5a65196df1be692516ac"
auth_token  = "e597e20b27bdc19f0348ddfa46351caf"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body="17", to="+19084202938", from_="+17324973029")
print message.sid
