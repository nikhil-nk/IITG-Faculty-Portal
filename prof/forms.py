from django import forms
from django.contrib.auth.models import User

from .models import professor,department,education,award_fellowships,award_achievement,experience,project,publication_books,publication_conferences,publication_journals,publication_thesis,student_completed,student_ongoing


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
