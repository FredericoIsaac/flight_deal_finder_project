from twilio.rest import Client


class NotificationManager:
    def __init__(self, flight_info: dict):
        # Twilio API
        self.ACCOUNT_SID = ""
        self.AUTH_TOKEN = ""
        self.PHONE_NUMBER_TWILLIO = "+"
        self.PHONE_NUMBER = ""
        self.info = flight_info


    def send_message(self):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
        message = client.messages \
            .create(body=f"Lowes price alert! Only £{self.info['price']} "
                         f"to fly from {self.info['from_name']}-{self.info['from_code']}"
                         f" to {self.info['to_name']}-{self.info['to_code']}",
                    from_=self.PHONE_NUMBER_TWILLIO,
                    to=self.PHONE_NUMBER
                    )
        print(message.status)
