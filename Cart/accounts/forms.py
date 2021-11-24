from django import forms
from .models import account
class regForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Renter Password'}))

    class Meta:
        model = account
        fields = ['first_name','last_name','email','phone','password']

    def clean(self):
        cleaned_data = super(regForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password and confirm_password not the same')
    def __init__(self,*args,**kwargs):
        super(regForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'last name'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['phone'].widget.attrs['placeholder'] = 'phone'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
