from kiss_bootcamp.celery import app
from .service import send


@app.task(bind=True, default_retry_delay=2 * 60)
def send_confirm_subscribe(self, subject: str, message: str, emails: list, html_message: str) -> str:
    return send(self, subject, message, emails, html_message)


@app.task(bind=True, default_retry_delay=5 * 60)
def send_news(self, subject: str, message: str, emails: list, html_message: str) -> str:
    return send(self, subject, message, emails, html_message)