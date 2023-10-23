from django.db import models


# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=60, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цены')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


# Блюдо
class Meal(models.Model):
    name = models.CharField(null=False, max_length=100, verbose_name='Название блюда')
    weight = models.IntegerField(null=True, blank=False, verbose_name='Вес блюда (гр.)')
    calories = models.IntegerField(null=False, blank=False, verbose_name='Калорийность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Блюда'
        verbose_name = 'Блюдо'
        # ordering = ['weight']


# Обед
class Lunch(models.Model):
    name = models.CharField(null=False, max_length=100, db_index=True, verbose_name='Название обеда')
    description = models.TextField(null=True, blank=True, verbose_name='Описание обеда')
    price = models.FloatField(null=False, blank=False, verbose_name='Стоимость обеда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Обеды'
        verbose_name = 'Обед'
        ordering = ['price']


# Состав обеда
class LunchStructure(models.Model):
    meals = models.ManyToManyField(Meal, verbose_name='Блюда')
    lunch = models.ForeignKey('Lunch', null=True, on_delete=models.PROTECT, verbose_name='Обед')

    def __str__(self):
        return "Вариант: " + self.lunch.name

    class Meta:
        verbose_name_plural = 'Варианты обедов'
        verbose_name = 'Вариант обеда'
