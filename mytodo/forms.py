from django import forms
from .models import ToDo

class ToDoForms(forms.Form):
    text = forms.CharField(max_length=50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Todo Ex: Del Junk Files!", 'aria-label':'Todo', 'aria-describedby':'add-btn'}))


class ModelToDOForm(forms.ModelForm):
    # its a short cut to add into database
    model = ToDo
    fields = ['text']
    widgets = {'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Todo Ex: Del Junk Files!", 'aria-label':'Todo', 'aria-describedby':'add-btn'})}