from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from profiles.models import Profile

def send_client_email(subject, sender, response, name, receiver):
    # Creating message subject and sender
    subject = subject
    sender = sender
    body = response

    #passing in the context vairables
    text_content = render_to_string('email/clientemail.txt',{"name": name, "body": body})
    html_content = render_to_string('email/clientemail.html',{"name": name, "body": body })

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()