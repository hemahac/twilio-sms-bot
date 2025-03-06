from twilio.rest import Client

# ضع بيانات حساب Twilio هنا
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
twilio_number = "YOUR_TWILIO_PHONE"
to_number = "YOUR_VERIFIED_PHONE"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Twilio!",
        from_=twilio_number,
            to=to_number
            )

            print(f"Message sent! SID: {message.sid}")