from django.shortcuts import render
from django.views.generic import CreateView
from pizza.models import Pizza
from pizza.forms import PizzaModelForm
from django.urls import reverse_lazy


class PizzaCreateView(CreateView):
    model = Pizza
    form_class = PizzaModelForm
    success_url = reverse_lazy("create_pizza")
    template_name = 'create_pizza.html'
