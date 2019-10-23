from django.contrib import admin
from django.urls import path
from pizza.views import PizzaCreateView, OrderDetailView, OrderCreateView, Result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PizzaCreateView.as_view(), name='create_pizza'),
    # path('order/<int:pk>/', OrderDetailView.as_view(), name='order')
    path('order/<int:pk>/', OrderCreateView.as_view(), name='order'),
    path('result_order/<int:pk>/', Result.as_view(), name='result_order'),
]
