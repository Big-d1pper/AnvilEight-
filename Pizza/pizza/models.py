from django.db import models


class Pizza(models.Model):
    name_of_pizza = models.CharField(max_length=255)
    dough = models.ForeignKey('pizza.Dough', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_pizza


class Dough(models.Model):
    name_dough = models.CharField(max_length=255)

    def __str__(self):
        return self.name_dough


class Filling(models.Model):
    name_of_filling = models.CharField(max_length=255)
    prise = models.DecimalField(max_digits=6, decimal_places=2)
    pizza = models.ForeignKey('pizza.Pizza', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_filling
