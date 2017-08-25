from celery import shared_task
from django.utils.crypto import get_random_string
import string
from django.contrib.auth.models import User
from django.core.mail import send_mail
from celery import Celery
from django.conf import settings
from celeryRabbit.celery import app


@app.task(queue='create_queue')
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)


@app.task(queue='email_queue')
def send_email(to, subject, body):
    send_mail(subject, body, 'noreply@celeryRabbit.me' ,[to,])
    return 'Email sent successfully!'

@app.task(queue='email_queue')
def confirmation_email(to):
    send_mail('Test Subject', 'Test Body', 'noreply@celeryRabbit.me' ,[to,])
    return 'Email sent successfully!'


