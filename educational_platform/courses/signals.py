from django.db.models.functions import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import *


@receiver(post_save, sender=Access)
def add_to_group(sender, instance, **kwargs):
    print('!!! SIGNAL WAS WORKED !!!')
    # Запрашиваем все группы по данному продукту
    all_groups = Group.objects.filter(product=instance.product)
    group_counter = all_groups.count()

    # Пересобираем группы после допуска нового участника
    date_time_now = timezone.make_aware()timezone.now().replace(microsecond=False)
    date_time_start = instance.product.start_date
    print(date_time_now, date_time_start, sep='\n')
    if datetime.datetime.now() < instance.product.start_date:
        print(timezone.now(), instance.product.start_date)

    if not group_counter:
        # Создаем группу и добавляем туда пользователя
        group = Group.objects.create(
            title=f'Группа {group_counter + 1}',
            product=instance.product,
        )
        group.members.add(instance.member)
    else:
        # Добавляем пользователя в последнюю созданную группу, но не больше лимита
        group = all_groups[group_counter - 1]
        if group.members.count() < instance.product.max_group_users:
            group.members.add(instance.member)
        else:
            group = Group.objects.create(
                title=f'Группа {group_counter + 1}',
                product=instance.product,
            )
            group.members.add(instance.member)
