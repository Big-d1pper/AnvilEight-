from django import forms
from pizza.models import Pizza


class PizzaModelForm(forms.ModelForm):
    class Meta:
        model = Pizza
        exclude = []


