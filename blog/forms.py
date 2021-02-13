from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('job','worker','Employee_phone_number','customer_name','customer_number','addres','city','status','details')

        widgets = {
            'job': forms.TextInput(attrs={'class':'form-control'}),
            'worker': forms.Select(attrs={'class': 'form-control'}),
            'Employee_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_number': forms.TextInput(attrs={'class': 'form-control'}),
            'addres': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
        }