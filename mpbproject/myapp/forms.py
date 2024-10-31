from django import forms
from .models import Admin,Customer,Pawnbroker


class DateInput(forms.DateInput):
    input_type = "date"



class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}


class CRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}


class PawnbrokerForm(forms.ModelForm):
    class Meta:
        model = Pawnbroker
        fields = "__all__"
        labels = {"category":"Select Category"}