from dataclasses import field
from django.forms import ModelForm, widgets
from django import forms
from .models import Service

class ProjectForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})