from django.core.mail import send_mail
from flake8.api import legacy as flake8


def check_files(file_objects):
    style_guide = flake8.get_style_guide()
    for file in file_objects:
        report = style_guide.input_file(file.file.path)
        file.review = report.get_statistics(('E', 'W', 'F'))
        send_mail(
            'Review',
            str(file.review),
            from_email='fake@fake.ru',
            fail_silently=False,
            recipient_list=[file.author.email]
        )
    return file_objects
