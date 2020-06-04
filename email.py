#camera.py
import os
from flask import Flask, render_template
from flask_mail import Mail
from flask_mail import Message as Mail_Message

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USE_TLS'] = os.environ['MAIL_USE_TLS']
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_DEFAULT_SENDER'] = os.environ['MAIL_DEFAULT_SENDER']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']

mail = Mail(app)

def email(user_email):
    receipt_msg = Mail_Message("Hello from Thermy", recipients=[user_email])
    receipt_msg.body = "Is this now?"
    mail.send(receipt_msg)

@app.route("/send_mail")
def send_mail():
    email("dan@precisionathleticswi.com")
    return "Done"


if __name__ == '__main__':
    app.run()
