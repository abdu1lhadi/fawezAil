from django import forms
from .models import Comment

class NewCustomers(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email' ,'nepersnt','nopersnt', 'body')