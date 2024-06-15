from flask import Flask, render_template,request
from flask_mail import Message, Mail
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('username')
app.config['MAIL_PASSWORD'] = os.getenv('password')


mail = Mail(app)

@app.route('/send_mail')
def send_mail():
    msg = Message('Hello', sender="Mandeep_MIS@mojopanda.com", recipients=['mandeepkumarmannu123@gmail.com'])
    msg.body = 'blanck'
    mail.send(msg)
    return 'Mail sent!'

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Split the email string into a list if email is provided
        email_list = email.split(',') if email else []

        # Send the email
        msg = Message(subject, sender=os.getenv('username'), recipients=email_list)
        msg.body = message
        mail.send(msg)
        # print(email_list)
        # print(name)
        # print(email)
        # print(subject)
        # print(message)

        # Provide feedback to the user
        return 'Mail sent successfully!'

    # Render the index.html template for GET requests
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
