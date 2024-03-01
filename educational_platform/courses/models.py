from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.
class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор/преподаватель')
    title = models.CharField(max_length=128, blank=False, verbose_name='Название продукта')
    start_date = models.DateTimeField(blank=False, verbose_name='Дата старта')
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, verbose_name='Цена')
    min_group_users = models.PositiveIntegerField(default=5, verbose_name='Min учащихся в группе')
    max_group_users = models.PositiveIntegerField(default=50, verbose_name='Max учащихся в группе')


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField(max_length=128, blank=False, verbose_name='Название урока')
    url = models.URLField(max_length=256, blank=False, verbose_name='Ссылка на видео')


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    members = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='Участники')
    title = models.CharField(max_length=128, blank=False, verbose_name='Название группы')
