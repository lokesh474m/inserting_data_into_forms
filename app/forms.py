from django import forms

class SchoolForm(forms.Form):
    Sname=forms.CharField()
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()