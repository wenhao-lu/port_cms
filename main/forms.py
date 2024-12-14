from django import forms
from .models import Project, Work, Stack, Education

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'url', 'github', 'image', 'subtitle', 'content1', 'content2', 'content3']


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'position', 'duration', 'url', 'github', 'image', 'subtitle', 'content1', 'content2', 'content3']


class StackForm(forms.ModelForm):
    class Meta:
        model = Stack
        fields = ['name', 'url', 'image']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'major', 'school', 'date', 'course']
