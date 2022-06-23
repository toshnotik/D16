from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Рассылка',
        'News',
        'skillfactor@yandex.ru',
        [user_email],
        fail_silently=False,
    )
