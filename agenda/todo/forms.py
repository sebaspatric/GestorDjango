from django.forms import DateInput
from django.forms.models import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('date',)
        #fields = '__all__'
        #fields = ['title', 'description']
        widgets = {
            'estimated_end': DateInput(attrs={'type': 'date'}),
        }