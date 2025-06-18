from celery import shared_task
from django.core.mail import send_mail
from telegram_bot import settings

@shared_task(bind=True)
def send_test_email(self, email): 
  
    mail_subject = 'Greetings Email'
    text = 'Wellcome to telegram bot!'
    to_email = email    
    send_mail(
        subject = mail_subject,
        message = text,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [to_email],
        fail_silently = True,
    )
    return 'Done'