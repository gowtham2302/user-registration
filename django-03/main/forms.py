from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser

class RegisterForm(UserCreationForm):
     first_name = forms.CharField(required=True , widget=forms.TextInput(attrs={'class':'form-control'}) )
     last_name = forms.CharField(required=True ,  widget=forms.TextInput(attrs={'class':'form-control'}) )
     api_key= forms.CharField(required=True , widget=forms.TextInput(attrs={'class':'form-control'}) )

     Doctor_attending = forms.CharField(required=True , widget=forms.TextInput(attrs={'class':'form-control'}) )
     date_of_visit = forms.DateField(required=True , widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}) )
     last_date_of_visit = forms.DateField(required=True , widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}) )

     class Meta:
        model = NewUser
        fields = ["username" , "email", "first_name" ,"last_name","api_key","Doctor_attending","date_of_visit","last_date_of_visit", "password1" , "password2"]
     
     def __init__(self, *args, **kwargs) :
         super(RegisterForm , self).__init__(*args, **kwargs)

         self.fields['username'].widget.attrs['class'] = 'form-control' 
         self.fields['email'].widget.attrs['class'] = 'form-control' 
         self.fields['password1'].widget.attrs['class'] = 'form-control' 
         self.fields['password2'].widget.attrs['class'] = 'form-control' 