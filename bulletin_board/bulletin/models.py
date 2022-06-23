from django.db import models
from datetime import datetime
from bulletin_board.settings import AUTH_USER_MODEL
from django.urls import reverse


class Author(models.Model):
    name = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, verbose_name='Автор')

    def __str__(self):
        return self.name.username

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Category(models.Model):
    ''' Категории'''
    tanks = 'tanks'
    hills = 'hills'
    dd = 'dd'
    Merchants = 'Merchants'
    Guildmasters = 'Guildmasters'
    Questgivers = 'Questgivers'
    Blacksmiths = 'Blacksmiths'
    Tanners = 'Tanners'
    Zelievars = 'Zelievars'
    SpellMasters = 'SpellMasters'
    Categories = [(tanks, 'Танки'),
                  (hills, 'Хилы'),
                  (dd, 'ДД'),
                  (Merchants, 'Торговцы'),
                  (Guildmasters, 'Гилдмастеры'),
                  (Questgivers, 'Квестгиверы'),
                  (Blacksmiths, 'Кузнецы'),
                  (Tanners, 'Кожевники'),
                  (Zelievars, 'Зельевары'),
                  (SpellMasters, 'Мастера заклинаний')]

    name = models.CharField("Категория", max_length=25, choices=Categories, default=tanks, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Declaration(models.Model):
    """Обявления"""
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Пользыватель', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Описание')
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата пуболткации')
    response = models.ManyToManyField(AUTH_USER_MODEL, related_name='post_response', )
    accepted_response = models.ManyToManyField(AUTH_USER_MODEL, related_name='post_accepted_response', )

    file = models.FileField('Файл', upload_to="bulletin_file/", blank=True, null=True)
    image = models.ImageField('Изобнажение', upload_to="image/", blank=True, null=True)

    def get_absolute_url(self):
        return reverse('DeclarationDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    # def get_absolute_url(self):

    class Meta:
        verbose_name = "Обявление"
        verbose_name_plural = "Обявления"


class Reviews(models.Model):
    '''Отзывы'''

    declaration = models.ForeignKey(Declaration, verbose_name='обявление', related_name='review_declaration',
                                    on_delete=models.CASCADE, null=True)
    commentator = models.ForeignKey(AUTH_USER_MODEL, verbose_name='коментатор', on_delete=models.CASCADE)
    review = models.TextField('Отклик', max_length=3000)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"
