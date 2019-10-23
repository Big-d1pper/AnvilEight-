# Generated by Django 2.2.5 on 2019-10-23 15:27

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0006_auto_20191020_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfoOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('telephone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('name', models.CharField(max_length=50)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Pizza')),
            ],
        ),
    ]
