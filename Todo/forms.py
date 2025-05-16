from django import forms
from.models import Todo

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name','description','status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
