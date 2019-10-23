from django import forms
from pizza.models import Pizza, UserInfoOrder


class PizzaModelForm(forms.ModelForm):
    class Meta:
        model = Pizza
        exclude = ['prise_pizza']


class UserInfoOrderModelForm(forms.ModelForm):
    class Meta:
        model = UserInfoOrder
        exclude = []


