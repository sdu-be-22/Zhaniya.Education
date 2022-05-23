from random import choices
from unicodedata import name
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

# choices = [('1 synyp', '1 synyp'),('2 synyp', '2 synyp'),('3 synyp', '3 synyp'),('4 synyp', '4 synyp'),('5 synyp', '5 synyp'),('6 synyp', '6 synyp'),('7 synyp', '7 synyp'),('8 synyp', '8 synyp'),('9 synyp', '9 synyp'),('10 synyp', '10 synyp'),('11 synyp', '11 synyp'),]
classes = Classes.objects.all().values_list('title', 'title')

classes_list = []
for item in classes:
    classes_list.append(item)

class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ["title", "ab_theme", "classes", "image", ]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Takirip'
            }),
            "ab_theme": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Takirip jaili qiskasha'
            }),
            "classes": forms.Select(choices = classes_list, attrs={
                'class': 'form-control',
                'placeholder': 'Takirip'
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
        widgets ={ 
                "classes": forms.Select(choices = classes_list, attrs={
                'class': 'form-control',
                'placeholder': 'Takirip'
            }),
        }

class VideoForm(ModelForm):
    
    class Meta:
        model=Video
        fields="__all__"
        widgets ={ 
                "classes": forms.Select(choices = classes_list, attrs={
                'class': 'form-control',
                'placeholder': 'Synyp'
            }),
        }      

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ["title", "authors", "front_image", ]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "authors": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Avtorlari'
            }),
            "classes": forms.Select(choices = classes_list, attrs={
                'class': 'form-control',
                'placeholder': 'synyp'
            }),
        }