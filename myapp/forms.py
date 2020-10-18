from django import forms
from .models import UserCreation,Sponsor,DetailsOfEvent
from django.contrib.auth.forms import AuthenticationForm,UsernameField
class UserCreationForm(forms.ModelForm):
    class Meta:
        model=UserCreation
        exclude=['otp',]
        widgets={
            'password':forms.PasswordInput()
                }

class OtpForm(forms.ModelForm):
    class Meta:
        model=UserCreation
        fields=['otp']
class LoginForm(forms.ModelForm):
    class Meta:
        model=UserCreation
        fields=['name','password']
        widgets={
            'password':forms.PasswordInput()

        }
class SponsorForm(forms.ModelForm):
    class Meta:
        model=Sponsor
        fields='__all__'
        labels={'Amount':'Enter Amount in Thousands '}
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}, ),
        }
class EventForm(forms.ModelForm):
    class Meta:
        model=DetailsOfEvent
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'},),
            'description':forms.Textarea(attrs={'class':'form-control'},),
            'date':forms.DateInput(attrs={'class':"form-control" ,'type':"date"},),
        }
        labels={'name':'Name of Event'}