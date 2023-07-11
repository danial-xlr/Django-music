from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    
class UserRegisterationForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email=forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email'}))
    password1=forms.CharField(label='Password',max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(label='Comfirm password',max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    
    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('This email is already taken')
        return email
    
    """ def clean_password2(self):
        p1=self.cleaned_data['password1']
        p2=self.cleaned_data['password2']
        
        if p1!=p2:
            raise forms.ValidationError('Passwords not matched')
        return p2 """
        
    def clean(self):
        cleaned_data = super().clean()
        p1=cleaned_data.get('password1')
        p2=cleaned_data.get('password2')
            
        if p1 and p2:
            if p1 != p2:
                raise forms.ValidationError('Passwords not matched')
        
    
    