from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Declaration, Reviews
from users.models import CustomUser
from django.urls import reverse_lazy


@receiver(m2m_changed, sender=Declaration.response.through)
def notify_new_response(sender, instance, **kwargs):
    """отправить письмо автору поста после отклика"""
    # Если тип изменения было добавление, то...
    if kwargs['action'] == "post_add":
        # instance в себе содержит измененный пост
        username = instance.user.username
        email = instance.user.email
        content = instance.title
        HOST = 'http://127.0.0.1:8000'
        link = reverse_lazy('mypage')
        link = HOST + f'{link}'
        send_mail_new_response.apply_async([email, username, link, content], countdown=5)


@receiver(m2m_changed, sender=Declaration.accepted_response.through)
def notify_accept_response(sender, instance, **kwargs):
    """отправить письмо юзеру оставившего отклик"""
    # Если тип изменения было добавление, то...
    if kwargs['action'] == "post_add":
        # instance в себе содержит измененный пост
        user = instance.accepted_response.all().order_by('-id')[0]
        username = user.username
        email = user.email
        content = instance.title
        HOST = 'http://127.0.0.1:8000'
        link = reverse_lazy('declaration', kwargs={'pk': instance.id})
        link = HOST + f'{link}'
        send_mail_accept_response.apply_async([email, username, link, content], countdown=5)
