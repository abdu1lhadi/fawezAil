from django import forms
from django.forms import ModelForm, CharField, TextInput, IntegerField
from .models import Comment, Jobrequest

class NewCustomers(forms.ModelForm):
    nopersnt = forms.IntegerField(help_text='Enter Your Phone Number', label='Phone Number')

    class Meta:
        model = Comment
        fields = ('name', 'email' ,'nepersnt','nopersnt', 'body')

    def clean_nopersnt(self, *args, **kwargs):
        csnumber = self.cleaned_data.get("nopersnt")
        if csnumber > 999999999999:
            raise forms.ValidationError("Enter Your Phone Number, Must Be No More Than 12 Numbers")

        if csnumber < 99999999:
            raise forms.ValidationError("Enter Your Phone Number, Must Be At Least 10 Numbers")
        
        return csnumber


class NewJob(forms.ModelForm):
    mobile_number = forms.IntegerField(help_text='Enter Your Phone Number')
    

    class Meta:
        model = Jobrequest
        fields = ('name_employee', 'name_job' ,'certificate','mobile_number','email_employe','description')

    def clean_mobile_number(self, *args, **kwargs):
        number = self.cleaned_data.get("mobile_number")
        if number > 999999999999:
            raise forms.ValidationError("Enter Your Phone Number, Must Be No More Than 12 Numbers")

        if number < 99999999:
            raise forms.ValidationError("Enter Your Phone Number, Must Be At Least 10 Numbers")
        
        return number
