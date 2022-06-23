from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from bulletin_board.settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.decorators import login_required

from .models import Declaration, Category, Reviews, Author
from .filters import DaclarationFilter
from .forms import DeclarationForm, AddReviewsForm


class DeclarationList(ListView):
    model = Declaration
    template_name = 'Declaration.html'
    context_object_name = 'Declaration'
    ordering = ['-date_create']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_tanks'] = Category.objects.get(name='tanks').id
        context['category_hills'] = Category.objects.get(name='hills').id
        context['category_dd'] = Category.objects.get(name='dd').id
        context['category_Merchants'] = Category.objects.get(name='Merchants').id
        context['category_Guildmasters'] = Category.objects.get(name='Guildmasters').id
        context['category_Questgivers'] = Category.objects.get(name='Questgivers').id
        context['category_Blacksmiths'] = Category.objects.get(name='Blacksmiths').id
        context['category_Tanners'] = Category.objects.get(name='Tanners').id
        context['category_Zelievars'] = Category.objects.get(name='Zelievars').id
        context['category_SpellMasters'] = Category.objects.get(name='SpellMasters').id

        return context


class DeclarationCategory(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'DeclarationCategory'

    def get_context_data(self, **kwargs):
        id = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        # Контекст для списка новостей в текущей категории
        context['category'] = Declaration.objects.filter(category=id)
        context['category_name'] = Category.objects.get(pk=id)

        return context


class DeclarationDetail(DetailView):
    model = Declaration
    template_name = 'DeclarationDetail.html'
    context_object_name = 'DeclarationDetail'
    queryset = Declaration.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Declaration, id=self.kwargs.get(self.pk_url_kwarg))
        if self.request.user == post.user:
            context['author'] = True

        else:
            context['is_not_author'] = True

        return context

    '''def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)

        if not obj:
            obj = super().get_object()
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj'''


class DeclarationSearch(ListView):
    model = Declaration
    template_name = 'search.html'
    context_object_name = 'search'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DaclarationFilter(self.request.GET, queryset=self.get_queryset())
        return context


class DeclarationCreate(LoginRequiredMixin, CreateView):
    model = Declaration
    template_name = 'declaration_create.html'
    form_class = DeclarationForm
    login_url = '/accounts/login/'
    success_url = '/'

    # permission_required = ('News.add_post', 'News.view_post')


class DeclarationUpdateView(LoginRequiredMixin, UpdateView):
    model = Declaration
    template_name = 'declaration_edit.html'
    form_class = DeclarationForm
    login_url = '/accounts/login/'
    redirect_file_name = '/'
    success_url = '/'
    # permission_required = ('News.change_post', 'News.view_post')


class DeclarationDeleteView(LoginRequiredMixin, DeleteView):
    model = Declaration
    template_name = 'declaration_delete.html'
    queryset = Declaration.objects.all()
    success_url = '/'
    login_url = '/accounts/login/'
    # permission_required = ['News.delete_post', 'News.view_post']


class AddReviews(LoginRequiredMixin, CreateView):
    template_name = 'add_reviews.html'
    form_class = AddReviewsForm
    login_url = '/accounts/login/'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        pk = self.kwargs.get('pk')
        user = self.request.user
        self.object.commentator = user
        self.object.declaration_id = pk
        self.object.save()
        return super().form_valid(form)

    '''def post(self, request, *args, **kwargs):
        post = get_object_or_404(Declaration, id=self.kwargs.get(self.pk_url_kwarg))
        user_email = post.user.email

        reviews = Reviews(review=request.POST['review'],
                          commentator=self.request.user,
                          )

        send_mail(
            subject=f'отклик от пользывателя : {reviews.commentator}',
            message=f'текст отклика : {reviews.review}',
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[user_email]
        )

        return redirect('/')'''


class ReviewDetail(DetailView):
    model = Reviews
    template_name = 'reviews.html'
    context_object_name = 'reviewdetail'

    # def post(self,request,*args,**kwargs):


class ReviewDelete(DeleteView):
    model = Reviews
    template_name = 'reviews_delete.html'
    queryset = Reviews.objects.all()
    success_url = '/mypage'


@login_required(login_url='/accounts/login/')
def user_response(request, pk):
    """отклик на пост"""
    post = get_object_or_404(Declaration, id=request.POST.get('post_response'))
    post.response.add(request.user)
    messages.info(request, 'Отклик успешно отправлен!')
    return redirect('post_detail', pk=pk)
