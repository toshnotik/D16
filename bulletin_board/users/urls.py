from django.urls import path
from .views import UserPage

urlpatterns = [
    path('', UserPage.as_view(), name='mypage')
]
