# @Time   : 2019/1/11 11:26
# @Author : RobbieHan
# @File   : extras_tag.py

from django import template
from django.db.models.query import QuerySet
register = template.Library()


@register.simple_tag
def get_con(context, arg, key):
    if isinstance(context, QuerySet):
        context = context.values()
        instance = [con for con in context if con['id'] == arg]
        if instance:
            return instance[0][key]
        return ''



