from django import forms
from .models import student

class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
        labels ={
            'name':'name',
            'address':'address',
            'phone':'phone',
            'cours':'cours',
            'place':'place',
        }