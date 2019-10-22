from django import forms
from django.forms import ModelForm, CharField, TextInput, IntegerField
from .models import Comment, Jobrequest

class NewCustomers(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email' ,'nepersnt','nopersnt', 'body')

class NewJob(forms.ModelForm):
    mobile_number = forms.IntegerField(max_value=999999999999, min_value=99999999, help_text='Enter Your Phone Number')
    

    class Meta:
        model = Jobrequest
        fields = ('name_employee', 'name_job' ,'certificate','mobile_number', 'description')