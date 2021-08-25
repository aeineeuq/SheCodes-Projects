
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import NewsStory

# allow Django to infer all the form fields and validation from a model
class StoryForm(ModelForm):
    # nested class we want Django to infer from
    class Meta:
        model = NewsStory
        # list of fields to be included in the form
        fields = ['title', 'content','pub_date', 'img_url']
        widgets = {
            'title': TextInput(attrs={
                'style': 'min-width: 50%;', 
            }),
            'content': TextInput(attrs={
                'style': 'min-width: 80%;' 'min-height:200px;'
            }),
        	'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs = {
                'class':'form-control',
                'placeholder':'Select a date',
                'type':'date'}),
            'img_url': TextInput(attrs={
                'style': 'min-width: 50%;', 
            }),           
    	}

# django form fields are customised via widget attributes