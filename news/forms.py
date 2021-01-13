from django.core.exceptions import ValidationError
from django import forms
from news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'image', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()
        if new_slug == 'create':
            raise ValidationError('URL не может словом "Create"')
        return new_slug