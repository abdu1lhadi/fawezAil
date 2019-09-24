from django import forms
from .models import Comment, Jobrequest

class NewCustomers(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email' ,'nepersnt','nopersnt', 'body')

class NewJob(forms.ModelForm):
    class Meta:
        model = Jobrequest
        fields = ('name_employee', 'name_job' ,'certificate','mobile_number', 'description')