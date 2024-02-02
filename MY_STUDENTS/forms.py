from django import forms
from .models import *

class Student_Form(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

        labels={
            'name':"Student Name"
        }

        widgets={
            'idno':forms.TextInput(attrs={'class':"form-control"}),
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'img':forms.ClearableFileInput(attrs={'class':"form-control"}),
            'rollno':forms.NumberInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'password':forms.NumberInput(attrs={'class':"form-control"}),
            'class_name':forms.TextInput(attrs={'class':"form-control"}),
            'mobile':forms.NumberInput(attrs={'class':"form-control"}),
            'age':forms.NumberInput(attrs={'class':"form-control"}),
        }