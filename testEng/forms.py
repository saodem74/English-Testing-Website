from django.contrib.auth.models import User
from django import forms
from .models import word, topic, comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class WordForm(forms.ModelForm):

    class Meta:
        model = word
        fields = ['name', 'meaning', 'pronunc', 'type', 'image', 'audio', 'tolearn']


class TopicForm(forms.ModelForm):

    class Meta:
        model = topic
        fields = ['name', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['content']