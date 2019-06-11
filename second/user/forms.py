from django import forms
from .models import User

class Data_signup_form(forms.ModelForm):
    STATE_CHOICES = (
        (1,"Andra Pradesh"),
        (2,"Arunachal Pradesh"),
        (3,"Assam"),
        (4,"Bihar"),
        (5,"Chhattisgarh"),
        (6,"Goa"),
        (7,"Gujarat"),
        (8,"Haryana"),
        (9,"Himachal Pradesh"),
        (10,"Jammu and Kashmir"),
        (11,"Jharkhand"),
        (12,"Karnataka"),
        (13,"Kerala"),
        (14,"Madya Pradesh"),
        (15,"Maharashtra"),
        (16,"Manipur"),
        (17,"Meghalaya"),
        (18,"Mizoram"),
        (19,"Nagaland"),
        (20,"Orissa"),
        (21,"Punjab"),
        (22,"Rajasthan"),
        (23,"Sikkim"),
        (24,"Tamil Nadu"),
        (25,"Telagana"),
        (26,"Tripura"),
        (27,"Uttaranchal"),
        (28,"Uttar Pradesh"),
        (29,"West Bengal"),

    )

    username  = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'field','placeholder':'Username'}))
    password  = forms.CharField(label='',widget = forms.PasswordInput(attrs={'class':'field','placeholder':'Password'}))
    cpassword = forms.CharField(label='',widget = forms.PasswordInput(attrs={'class':'field','placeholder':'Confirm Password'}))
    fname     = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'field','placeholder':'First Name'}))
    lname     = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'field','placeholder':'Last Name'}))
    dob       = forms.DateField(label='DOB',widget=forms.SelectDateWidget(years=range(1990,2100),attrs={'class':'field','placeholder':'DOB'}))
    address   = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'field','placeholder':'Address'}))
    state     = forms.ChoiceField(label='',choices = STATE_CHOICES,widget=forms.Select(attrs={'class':'field','placeholder':'State'}))
    city      = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'field','placeholder':'City'}))
    
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'cpassword',
            'fname',
            'lname',
            'dob',
            'address',
            'state',
            'city',
        ]
        
    def clean_cpassword(self):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        if password != cpassword:
            raise forms.ValidationError("Password and Confirm Password is not same")
        return cpassword

class User_signin(forms.Form):
    username  = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'field','placeholder':'Username'}))
    password  = forms.CharField(label='',widget = forms.PasswordInput(attrs={'class':'field','placeholder':'Password'}))

    class Meta:
        fields = [
            'username',
            'password',
        ]