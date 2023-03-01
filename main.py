from data import get_data
from decorators import handle_exception
from email_client import EmailClient
from message import Message
from environs import Env
from smtplib import SMTP_SSL

env = Env()
env.read_env()

HOST = env("EMAIL_HOST")
PORT = env("PORT")
HOST_USER = env("EMAIL_HOST_USER")
HOST_USER_PASSWORD = env("EMAIL_HOST_USER_PASSWORD")



def create_smtp_server():
     return SMTP_SSL(HOST, PORT)



@handle_exception
def main():
    data = get_data("https://jsonplaceholder.typicode.com/posts", "text")
    message_body = str(data)
    receiver = "solomonuche42@gmail.com"
    message = Message(
        HOST_USER, receiver, "TESTING EMAIL CLIENT", message_body
    ).compose_multipart_message()

    smtp_server = create_smtp_server()

    email_client = EmailClient(
        smtp_server, HOST_USER, HOST_USER_PASSWORD, HOST_USER, receiver
    )

    email_client.send_message(message)


if __name__ == "__main__":
    main()
