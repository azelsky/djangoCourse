from django.db import models

# Create your models here.

class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пиццерия')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Интернет-адрес пиццерии')

    class Meta:
        verbose_name = 'Пиццария'
        verbose_name_plural = 'Пиццарии'

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzaShop = models.ForeignKey(PizzaShop, verbose_name='Name of store',on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Name of pizza')
    short_description = models.CharField(max_length=30, verbose_name='Description')
    price = models.IntegerField(default=0, verbose_name='Price')
    photo = models.ImageField('Photo', upload_to='firstapp/photo', default='', blank=True)

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        ordering = ['name']

    def __str__(self):
        return self.name