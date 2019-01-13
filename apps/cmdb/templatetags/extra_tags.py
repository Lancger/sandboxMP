# @Time   : 2019/1/11 11:26
# @Author : RobbieHan
# @File   : extras_tag.py

from django import template
from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model

register = template.Library()

from cmdb.models import Code, Cabinet

User = get_user_model()


@register.simple_tag
def get_con(context, arg, field):
    if isinstance(context, QuerySet):
        context = context.values()
        instance = [con for con in context if con['id'] == arg]
        if instance:
            return instance[0][field]
        return ''


@register.filter(name='compare_result')
def get_change_compare(changes):

    change_compare = []
    for key in ['network_type', 'service_type', 'operation_type']:
        msg = replace_msg(changes, key, Code, 'value')
        if msg:
            change_compare.append(msg)
    cabinet_msg = replace_msg(changes, 'dev_cabinet', Cabinet, 'number')
    if cabinet_msg:
        change_compare.append(cabinet_msg)
    user_msg = replace_msg(changes, 'leader', User, 'name')
    if user_msg:
        change_compare.append(user_msg)

    return '，'.join(str(i) for i in change_compare)


def replace_msg(changes, key, model, field):
    info = '字段"%(field)s"内容由"%(old)s"变更为"%(new)s"'
    if key in changes:
        old = changes[key][0]
        new = changes[key][1]
        try:
            data = model.objects.filter(id=old).values()[0]
            old_data = data[field]
        except Exception:
            old_data = old
        try:
            data = model.objects.filter(id=new).values()[0]
            new_data = data[field]
        except Exception:
            new_data = new
        msg = info % {
            'field': key,
            'old': old_data,
            'new': new_data
        }
        return msg
