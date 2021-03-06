# Generated by Django 2.1.3 on 2018-11-18 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name of pizza')),
                ('short_description', models.CharField(max_length=30, verbose_name='Description')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('pizzaShop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.PizzaShop')),
            ],
        ),
    ]
