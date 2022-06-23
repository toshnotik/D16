from django.forms import ModelForm, Textarea
from .models import Declaration,Reviews


class DeclarationForm(ModelForm):
    class Meta:
        model = Declaration
        fields = ['user', 'category', 'title', 'text', 'file', 'image']
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...'
            }),
        }


class AddReviewsForm(ModelForm):
    class Meta:
        model =Reviews
        fields = ['review']
        widgets = {
            'review': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...'
            })

        }
