from django.contrib import admin
from pizza.models import Pizza, Dough, Filling


admin.site.register(Pizza)
admin.site.register(Dough)
admin.site.register(Filling)