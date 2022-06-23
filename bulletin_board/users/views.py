from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from bulletin.models import Declaration, Reviews
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class UserPage(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'profile'
    template_name = 'mypage.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(username=self.request.user)
        my_posts = Declaration.objects.filter(user=self.request.user)
        context['reviews'] = []
        for post in my_posts:
            context['reviews'].append(Reviews.objects.filter(declaration=post.id))
        return context

    def post(self, request, *args, **kwargs):
        # Принять отклик
        if request.POST.get('accept_response'):
            accept_data = request.POST.get('accept_response').split(' ')
            post = Declaration.objects.get(id=accept_data[-1])
            user = CustomUser.objects.get(username=accept_data[0])
            post.accepted_response.add(user)
            messages.info(request, 'Вы приняли отклик!')
        elif request.POST.get('accept_response'):
            accept_data = request.POST.get('accept_response').split(' ')
            post = Declaration.objects.get(id=accept_data[-1])
            user = CustomUser.objects.get(username=accept_data[0])
            post.response.remove(user)
            messages.info(request, 'Вы отклонили отклик!')
        return redirect('mypage')
