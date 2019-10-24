from django import forms
from pizza.models import Pizza, UserInfoOrder, Filling, GroupOfFilling


class PizzaModelForm(forms.ModelForm):
    class Meta:
        model = Pizza
        exclude = ['prise_pizza']


class UserInfoOrderModelForm(forms.ModelForm):
    class Meta:
        model = UserInfoOrder
        exclude = []


class FillingModelForm(forms.ModelForm):
    class Meta:
        model = Filling
        exclude = []


class GroupModelForm(forms.ModelForm):
    class Meta:
        model = GroupOfFilling
        exclude = []