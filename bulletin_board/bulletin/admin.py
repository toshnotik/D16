from django.contrib import admin

from .models import Category, Declaration, Reviews, Author


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name',)


@admin.register(Declaration)
class DaclarationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'text', 'category', 'date_create')
    list_display_links = ('title',)
    list_filter = ('user', 'title', 'category', 'date_create')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ( 'commentator', 'review', 'review_date')
    list_display_links = ('review',)


admin.site.register(Author)
