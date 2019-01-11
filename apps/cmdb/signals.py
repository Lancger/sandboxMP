# @Time   : 2019/1/10 16:08
# @Author : RobbieHan
# @File   : signals.py.py

import os

from django.dispatch import receiver
from django.db.models.signals import post_delete

from .models import DeviceInfo, ConnectionInfo, DeviceFile


@receiver(post_delete, sender=DeviceInfo)
def auto_delete_connection(sender, instance, **kwargs):
    dev_connection = getattr(instance, 'dev_connection')
    if dev_connection:
        ConnectionInfo.objects.filter(id=dev_connection).delete()


@receiver(post_delete, sender=DeviceFile)
def auto_delete_file(sender, instance, **kwargs):
    if instance.file_content:
        if os.path.isfile(instance.file_content.path):
            os.remove(instance.file_content.path)