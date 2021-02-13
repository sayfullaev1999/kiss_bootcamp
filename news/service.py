from django.core.mail import send_mail
from django.conf import settings


def send(self, subject: str, message: str, emails: list, html_message: str) -> str:
    if not isinstance(emails, list):
        emails = [emails]
    try:
        send_mail(
            subject=subject,
            from_email=settings.DEFAULT_FROM_EMAIL,
            message=message,
            recipient_list=emails,
            html_message=html_message
        )
        return 'Success!!!'
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
