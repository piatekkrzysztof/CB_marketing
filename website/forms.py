from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from website.models import *

class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserCreateForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise ValidationError("hasła nie są zgodne")

    def clean_login(self):
        user_name = self.cleaned_data.get('login')
        user = User.objects.filter(username=user_name)
        if user:
            raise ValidationError("Podana nazwa użytkownika jest już zajęta")
        return user_name

class CreateCategoryForm(forms.Form):
    name=forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

class CreateBlogPost(forms.Form):
    title = forms.CharField(max_length=250)
    text = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices=[(category.id, category.name) for category in Category.objects.all()]

class CreateArticleCategoryForm(forms.Form):
    name=forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

class CreateArticleForm(forms.Form):
    title = forms.CharField(max_length=250)
    text = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices=[(cat.id, cat.name) for cat in Article_category.objects.all()]