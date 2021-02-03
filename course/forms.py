from django import forms
from django.core.exceptions import ValidationError

from .models import Course
from .models import ContactUs


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'info', 'image', 'mentor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
            'Mentor': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()
        if new_slug == 'create':
            raise ValidationError('URL не может словом "Create"')
        return new_slug


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'phone_number', 'course']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control input'}),
            'course': forms.Select(attrs={'class': 'form-control'})
        }
