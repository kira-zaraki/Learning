from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Expoilted, Cours
from django.forms import ModelForm

class SingupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SingupForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'single-input'

    username = forms.CharField(max_length=30, required=False, help_text='Username', widget=forms.TextInput(attrs={'placeholder': "username"}))
    #                            widget=forms.TextInput(attrs = {'class' : 'single-input'}))
    # first_name = forms.CharField(max_length=30, required=False, help_text='First Name')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Last Name')
    email = forms.CharField(max_length=100, required=False, help_text='Email', widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
    password1 = forms.CharField(max_length=100, required=False, help_text='password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(max_length=100, required=False, help_text='password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}



class ExloitedForm(ModelForm):
    # type = forms.MultipleChoiceField(choices=(('T','Teacher'),('S','Student')))
    # type = forms.ModelChoiceField(queryset=Expoilted.objects.all(), to_field_name='type')
    class Meta:
        model = Expoilted
        fields = {'type'}


class CoursForm(ModelForm):
    def __init__(self, *arg, **kwargs):
        super(CoursForm, self).__init__(*arg, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'single-input'


    class Meta:
        model = Cours
        fields = '__all__'
        exclude = ['trainer']

