from django import forms

class LoginForm(forms.Form):
    username_data = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'size': '40'})
    )
    password_data = forms.CharField(
        label="Password",
        widget=forms.TextInput(attrs={'size': '40'})
    )
