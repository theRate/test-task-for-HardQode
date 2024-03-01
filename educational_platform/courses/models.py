from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Product(models.Model):
    """Сущность продукта"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор/преподаватель')
    title = models.CharField('Название продукта', max_length=128, blank=False)
    start_date = models.DateTimeField('Дата старта', blank=False)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2, blank=False)
    min_group_users = models.PositiveIntegerField('Min учащихся в группе', default=5)
    max_group_users = models.PositiveIntegerField('Max учащихся в группе', default=50)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Сущность урока"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField('Название урока', max_length=128, blank=False)
    url = models.URLField('Ссылка на видео', max_length=256, blank=False)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title


class Group(models.Model):
    """Сущность группы"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    members = models.ManyToManyField(User, blank=True, verbose_name='Участники')
    title = models.CharField('Название группы', max_length=128, blank=False)

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'

    def __str__(self):
        return self.title
