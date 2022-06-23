from django.urls import path
from .views import DeclarationList, DeclarationCategory, DeclarationDetail, DeclarationSearch, DeclarationCreate, \
    DeclarationUpdateView, DeclarationDeleteView, AddReviews, ReviewDetail, ReviewDelete, user_response

urlpatterns = [
    path('', DeclarationList.as_view(), name='posts'),
    path('category/<int:pk>', DeclarationCategory.as_view(), name='category'),
    path('<int:pk>', DeclarationDetail.as_view(), name='declaration'),
    path('search/', DeclarationSearch.as_view(), name='search'),
    path('add/', DeclarationCreate.as_view(), name='create'),
    path('edit/<int:pk>', DeclarationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', DeclarationDeleteView.as_view(), name='delete'),
    path('addreviews/<int:pk>', AddReviews.as_view(), name='addreviews'),
    path('mypage/<int:pk>', ReviewDetail.as_view(), name='review'),
    path('delete_review/<int:pk>', ReviewDelete.as_view(), name='delete_review'),
    path('addreviews/<int:pk>', user_response, name='post_response')

]
