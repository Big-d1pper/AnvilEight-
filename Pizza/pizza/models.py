from django.db import models
from django.urls import reverse
from phone_field import PhoneField


class Pizza(models.Model):
    name_of_pizza = models.CharField(max_length=255)
    dough = models.ForeignKey('pizza.Dough', on_delete=models.CASCADE)
    filling = models.ManyToManyField('pizza.Filling')
    prise_pizza = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('Lot-detail-url-name', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name_of_pizza


class Dough(models.Model):
    name_dough = models.CharField(max_length=255)

    def __str__(self):
        return self.name_dough


class GroupOfFilling(models.Model):
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.group


class Filling(models.Model):
    name_of_filling = models.CharField(max_length=255)
    prise = models.DecimalField(max_digits=6, decimal_places=2)
    group = models.ForeignKey('pizza.GroupOfFilling', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_filling


class UserInfoOrder(models.Model):
    email = models.EmailField()
    telephone = PhoneField(blank=True, help_text='Contact phone number')
    name = models.CharField(max_length=50)
    pizza = models.ForeignKey('pizza.Pizza', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


