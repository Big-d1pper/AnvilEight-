from django.shortcuts import render
from django.views.generic import CreateView
from pizza.models import Pizza, Filling
from pizza.forms import PizzaModelForm
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.db.models import Sum


class PizzaCreateView(CreateView):
    model = Pizza
    form_class = PizzaModelForm
    # success_url = reverse_lazy("create_pizza")
    template_name = 'create_pizza.html'

    def get_success_url(self):
        return reverse('order', kwargs={'pk': self.object.id})



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print('_______________________')
    #     print(self)
    #     return context


class OrderDetalView(DetailView):
    model = Pizza
    context_object_name = 'pizza'
    template_name = 'form_order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderDetalView, self).get_context_data(**kwargs)
        filling = Filling.objects.filter(pizza=kwargs['object'])
        prise = 0
        for filling in filling:
            prise += filling.prise
            context['prise'] = prise
        return context

