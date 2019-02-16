from threading import Thread

from flask_mail import Message
from flask import render_template, current_app
from app import mail

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_mail(subject,sender,receipients,text_body,html_body):
    msg = Message(subject, sender=sender, recipients=receipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,args=(current_app._get_current_object(),msg)).start()

def send_password_reset_mail(user):
    token = user.get_reset_password_token()
    send_mail('[Microblog] Reset Your Password', sender=current_app.config["ADMINS"][0],
              receipients=[user.email],
              text_body=render_template('email/reset_password.text',user=user,token=token),
              html_body=render_template('email/reset_password.html', user=user,token=token)
              )


