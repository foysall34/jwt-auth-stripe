from celery import shared_task
import time

@shared_task
def send_email_task(email):
    print(f" Sending email to {email} ...")
    time.sleep(5)
    print(" Email sent successfully!")
    return "Email sent"
