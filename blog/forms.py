from django import forms
from .models import Comment, Jobnew

class NewCustomers(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email' ,'nepersnt','nopersnt', 'body')

class NewJob(forms.ModelForm):
    class Meta:
        model = Jobnew
        fields = ('name_employee', 'name_job' ,'certificate','mobile_number', 'description')