from django import forms
from .models import Notes, Post


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes  # Specify the model to base the form on.
        #  Specify which fields to include in the form.
        fields = ['title', 'content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
