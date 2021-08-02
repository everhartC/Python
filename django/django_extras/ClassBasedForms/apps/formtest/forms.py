from django import forms
class RegisterForm(forms.Form):
    fname = forms.CharField(max_length=45)
    lname = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confpw = forms.CharField(max_length=100, widget=forms.PasswordInput)
    