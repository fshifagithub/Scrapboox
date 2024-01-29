from django import forms

from django.contrib.auth.forms import UserCreationForm
from scrap.models import scraps,UserProfile
from django.contrib.auth.models import User




class VehicleForm(forms.ModelForm):
    class Meta:
        model=scraps
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "category":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            

        }

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class ScrapboxForm(forms.ModelForm):
    class Meta:
        model=scraps
        fields=["name","category","price","location","picture","phone_no"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        
        model=UserProfile
        fields=["user","email","phone"]



class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    product_id = forms.IntegerField(widget=forms.HiddenInput())

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than 0")
        return quantity
