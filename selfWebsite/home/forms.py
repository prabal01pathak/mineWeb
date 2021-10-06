from .models import HomePage
from django import forms


class SubscriberForm(forms.ModelForm):
    Name = forms.CharField(max_length=100,required=True, label='Name',widget=forms.Textarea(attrs={'rows':4, 'cols':40,'placeholder':"Name"} ))
    Email = forms.EmailField(max_length=100, required=True, label='Email',widget=forms.Textarea(attrs={'rows':4, 'cols':40,'placeholder':"Email"} )) 
    Mobile = forms.CharField(max_length=100, required=False, label='Mobile',widget=forms.Textarea(attrs={'rows':4, 'cols':40,'placeholder':"Mobile Ex. +919772328323"} )) 
    Message = forms.CharField(max_length=1000, required=False, label='Message',widget=forms.Textarea(attrs={'rows':4, 'cols':40,'placeholder':"Message"} )) 

    class Meta:
        model = HomePage
        fields = ['Name', 'Email', 'Mobile', 'Message']
