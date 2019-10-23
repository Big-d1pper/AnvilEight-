from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from pizza.models import Pizza, Filling, UserInfoOrder
from pizza.forms import PizzaModelForm, UserInfoOrderModelForm
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail


class PizzaCreateView(CreateView):
    model = Pizza
    form_class = PizzaModelForm
    # success_url = reverse_lazy("create_pizza")
    template_name = 'create_pizza.html'

    def get_success_url(self):
        return reverse('order', kwargs={'pk': self.object.id})


class OrderDetailView(DetailView):
    model = Pizza
    context_object_name = 'pizza'
    template_name = 'form_order.html'

    # def get_context_data(self, **kwargs):
    #     context = super(OrderDetailView, self).get_context_data(**kwargs)
    #     filling = Filling.objects.filter(pizza=kwargs['object'])
    #     prise = 0
    #     for filling in filling:
    #         prise += filling.prise
    #         context['prise'] = prise
    #     return context


class OrderCreateView(CreateView):
    model = UserInfoOrder
    form_class = UserInfoOrderModelForm
    template_name = 'form_order.html'
    success_url = reverse_lazy('result_order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filling = Filling.objects.all()
        prise = 0
        for filling in filling:
            prise += filling.prise
            print(prise)
            context['prise'] = prise
        return context

    def get(self, request, *args, **kwargs):
        return super(OrderCreateView, self).get(request, *args, **kwargs)

    def get_initial(self, *args, **kwargs):
        return {'pizza': self.kwargs['pk']}

    def get_success_url(self):
        return reverse('result_order', kwargs={'pk': self.object.id})


class Result(DetailView):
    model = UserInfoOrder
    template_name = "result_order.html"
    context_object_name = 'user'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        email = self.object.email
        send_mail(
            'Subject here',
            'Here is the message.',
            'b1gd1pperalaex@gmail.com',
            [email],
            fail_silently=False,
        )
        # emeil = UserInfoOrder.objects.filter(user=kwargs['object'])
        print(self.object.email) #- вытянуть емейл пользователя который сделал заказ
        return context

