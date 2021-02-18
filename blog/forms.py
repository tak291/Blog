from django import forms
from .models import Post

#Model for the form and where to edit the form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('job','worker','Employee_phone_number','customer_name','customer_number','addres','city','status','price', 'GSD', 'payment','appointment_date', 'details' )

        widgets = {
            'job': forms.TextInput(attrs={'class':'form-control'}),
            'worker': forms.RadioSelect(attrs={}),
            'Employee_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_number': forms.TextInput(attrs={'class': 'form-control'}),
            'addres': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'GSD': forms.RadioSelect(attrs={}),
            'payment': forms.RadioSelect(attrs={}),
            'appointment_date': forms.SelectDateWidget(attrs={}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
        }