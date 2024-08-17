from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=64, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(required=True, max_length=64, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    company = forms.CharField(max_length=64, widget=forms.TextInput(attrs={"class": "form-control"}))
    subject = forms.CharField(required=True, max_length=80, widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "form-control"}))