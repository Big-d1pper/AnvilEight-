from django.contrib import admin
from django.urls import path
from pizza.views import PizzaCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PizzaCreateView.as_view(), name='create_pizza'),
]
