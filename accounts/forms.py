from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from django import forms 
from .models import UserBankAccount,UserAddress

class UserRegistrationForm(UserCreationForm):
    account_type = forms.ChoiceField(choices= ACCOUNT_TYPE)
    gender = forms.ChoiceField(choices= GENDER_TYPE)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    city =forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    street_address =forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = User 
        fields = ['username','first_name','last_name', 'email','password1','password2', 'account_type','gender','birth_date','city','postal_code','street_address','country']

    def save(self,commit=True):
        user = super().save(commit=False)

        if commit:
            user.save() #user model e data save korlam

            account_type =self.cleaned_data.get('account_type')
            gender =self.cleaned_data.get('gender')
            birth_date =self.cleaned_data.get('birth_date')
            city =self.cleaned_data.get('city')
            postal_code =self.cleaned_data.get('postal_code')
            street_address =self.cleaned_data.get('street_address')
            country =self.cleaned_data.get('country')

            UserBankAccount.objects.create(
                user = user,
                account_type = account_type,
                gender = gender,
                birth_date = birth_date,
                account_no = 100000 + user.id,
                
            )
            UserAddress.objects.create(
                user = user,
                city = city,
                postal_code = postal_code,
                street_address = street_address,
                country = country,

            )
        return user
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })





          
