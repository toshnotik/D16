from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import RegisterUser


class NewsRegisterView(CreateView):
    model = User
    form_class = RegisterUser
    success_url = '/sign/login'
