from django.contrib import admin
from django.urls import path
from pizza.views import PizzaCreateView, OrderDetailView, OrderCreateView, Result, FillingCreateView, GroupCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PizzaCreateView.as_view(), name='create_pizza'),
    path('order/<int:pk>/', OrderCreateView.as_view(), name='order'),
    path('result_order/<int:pk>/', Result.as_view(), name='result_order'),
    path('add_filling/', FillingCreateView.as_view(), name='add_filling'),
    path('add_group', GroupCreateView.as_view(), name='add_group')
]
