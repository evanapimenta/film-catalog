from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(label=('Nome'), max_length=50, required=True)
    last_name = forms.CharField(label=('Sobrenome'), max_length=50, required=True)

    class Meta:
        model = User
        fields = ('name', 'last_name') + UserCreationForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user