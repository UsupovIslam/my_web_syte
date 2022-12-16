from django.forms import ModelForm, Textarea, TextInput
from .models import Fruits


class FruitForm(ModelForm):
    class Meta:
        model = Fruits
        fields = ['name', 'description', 'img']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'piaceholder': 'Enter name of fruit'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter test'
            })
        }



