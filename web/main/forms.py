from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm, TextInput, Textarea


class NewUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(NewUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'




	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ["title", "ab_theme", "image"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Takirip'
            }),
            "ab_theme": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Takirip jaili qiskasha'
            }),
        }

class ClassesForm(ModelForm):
    class Meta:
        model = Classes
        fields = ["title"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите класс'
            }),
        }

class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"