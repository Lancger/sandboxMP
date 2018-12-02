# @Time   : 2018/11/28 17:31
# @Author : RobbieHan
# @File   : views_code.py


from django.views.generic import TemplateView

from system.mixin import LoginRequiredMixin
from custom import (BreadcrumbMixin, SandboxCreateView,
                    SandboxListView, SandboxUpdateView, SandboxDeleteView)
from .models import Code
from .forms import CodeCreateForm, CodeUpdateForm


class CodeView(LoginRequiredMixin, BreadcrumbMixin, TemplateView):
    template_name = 'cmdb/code.html'

    def get_context_data(self, **kwargs):
        context = dict(code_parent=Code.objects.filter(parent=None))
        return context


class CodeCreateView(SandboxCreateView):
    model = Code
    form_class = CodeCreateForm
    template_name_suffix = '_create'

    def get_context_data(self, **kwargs):
        kwargs['code_all'] = Code.objects.all()
        return super().get_context_data(**kwargs)


class CodeListView(SandboxListView):
    model = Code
    fields = ['id', 'key', 'value', 'parent__value']

    def get(self, request):
        if 'parent' in request.GET and request.GET['parent']:
            self.filters = dict(parent__key=request.GET['parent'])
        return super().get(request)


# from django.http import JsonResponse
# from django.views.generic import View
# class CodeListView(LoginRequiredMixin, View):
#     fields = ['id', 'key', 'value', 'parent__value']
#     filters = {}
#
#     def get(self, request):
#         context = self.get_datatables_paginator(request)
#         return JsonResponse(context)
#
#     def get_datatables_paginator(self, request):
#         datatables = request.GET
#         draw = int(datatables.get('draw'))
#         start = int(datatables.get('start'))
#         length = int(datatables.get('length'))
#         order_column = datatables.get('order[0][column]')
#         order_dir = datatables.get('order[0][dir]')
#         order_field = datatables.get('columns[{}][data]'.format(order_column))
#         if order_dir == 'asc':
#             queryset = Code.objects.all().order_by(order_field)
#         else:
#             queryset = Code.objects.all().order_by('-{0}'.format(order_field))
#         record_total_count = queryset.count()
#         if self.filters:
#             queryset = queryset.filter(**self.filters)
#         if self.fields:
#             queryset = queryset.values(*self.fields)
#         record_filter_count = queryset.count()
#
#         object_list = queryset[start:(start+length)]
#
#         data = list(object_list)
#
#         return {
#             'draw': draw,
#             'recordsTotal': record_total_count,
#             'recordsFiltered': record_filter_count,
#             'data': data,
#         }


class CodeUpdateView(SandboxUpdateView):
    model = Code
    form_class = CodeUpdateForm
    template_name_suffix = '_update'

    def get_context_data(self, **kwargs):
        kwargs['code_all'] = Code.objects.exclude(id=self.request.GET['id'])
        return super().get_context_data(**kwargs)


class CodeDeleteView(SandboxDeleteView):
    model = Code
