from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Optional


@dataclass
class Message:
    sender: str
    recipient:str
    subject:str
    body: str

    def compose_multipart_message(self):
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = self.recipient
        message['Subject'] = self.subject
        message.attach(MIMEText(self.body, 'plain'))
        return message
    

  