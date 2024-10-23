from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomUser

class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Password again"
        self.fields['username'].label = "Имя"

        for field_name, field in self.fields.items():
            if field_name not in ('password1', 'password2'):
                field.widget = forms.TextInput(attrs={"class": "form-control p-0"})
            else:
                field.widget = forms.PasswordInput(attrs={"class": "form-control p-0"})


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  ]