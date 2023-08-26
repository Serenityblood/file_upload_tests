from django.core.mail import send_mail
from flake8.api import legacy as flake8

from .models import File
from api_file_upload.celery import app


@app.task
def send_mail_report(to, message):
    send_mail(
        'Review',
        message=message,
        from_email='fake@fake.ru',
        fail_silently=False,
        recipient_list=[to]
    )


@app.task
def check_files():
    style_guide = flake8.get_style_guide()
    for file in File.objects.filter(new=True):
        report = style_guide.input_file(file.file.path)
        file.review = report.get_statistics(('E', 'W', 'F'))
        file.new = False
        send_mail_report.delay(file.author.email, str(file.review))
