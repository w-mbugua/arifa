from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email(name, receiver):
    subject = 'Welcome to Jirani Watch'
    sender = settings.EMAIL_HOST_USER

    text_content = render_to_string('email/jiraniemail.txt', {"name": name})
    html_content = render_to_string('email/jiraniemail.html', {"name": name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()