import config
from twilio.rest import Client



Client = Client(config.account_sid, config.auth_token)

call = Client.messages.create(
    to="...",
    from_="...",
    body="This is our first message"
)

print(f"Message sent with SID: {call.sid}")