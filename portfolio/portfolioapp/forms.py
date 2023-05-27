
from django import forms
from django.forms import ModelForm
from .models import MyForm

class MyForm(forms.ModelForm):
     class Meta:
        model = MyForm
        fields ="__all__"
      
        widgets ={
         'first_name':forms.TextInput(attrs={'class':'form-control'}),
         'last_name':forms.TextInput(attrs={'class':'form-control'}),
         'email':forms.TextInput(attrs={'class':'form-control'}),
         'message':forms.Textarea(attrs={'class':'form-control'}),
        }