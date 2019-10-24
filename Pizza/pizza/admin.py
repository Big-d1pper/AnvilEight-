from django.contrib import admin
from pizza.models import Pizza, Dough, Filling, UserInfoOrder, GroupOfFilling


admin.site.register(Pizza)
admin.site.register(Dough)
admin.site.register(Filling)
admin.site.register(UserInfoOrder)
admin.site.register(GroupOfFilling)
