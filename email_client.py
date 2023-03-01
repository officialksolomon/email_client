from email.message import Message
from smtplib import SMTP





class EmailClient:
    def __init__(
        self,
        server: SMTP,
        username: str,
        password: str,
        sender: str,
        receiver: str,
    ):
        self.server = server
        self.username = username
        self.password = password
        self.sender = sender
        self.receiver = receiver

    def _connect(self):
        self.server.login(self.username, self.password)

    def _quit(self):
        self.server.quit()

    def send_message(self, message: Message):
        self._connect()
        self.server.send_message(message, self.sender, self.receiver)
        print("==== Email successfully sent ====")
        self._quit()
