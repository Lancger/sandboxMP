# @Time   : 2018/12/21 20:17
# @Author : RobbieHan
# @File   : views_device.py

from django.views.generic import TemplateView

from system.mixin import LoginRequiredMixin
from custom import (BreadcrumbMixin, SandboxDeleteView,
                    SandboxListView, SandboxUpdateView, SandboxCreateView)
from .models import Cabinet, DeviceInfo, DeviceFile


class CabinetView(LoginRequiredMixin, BreadcrumbMixin, TemplateView):
    template_name = 'cmdb/cabinet.html'


class CabinetCreateView(SandboxCreateView):
    model = Cabinet
    fields = '__all__'


class CabinetUpdateView(SandboxUpdateView):
    model = Cabinet
    fields = '__all__'


class CabinetListView(SandboxListView):
    model = Cabinet
    fields = ['id', 'number', 'position', 'desc']

    def get(self, request):
        data = request.GET
        if 'number' in data and data['number']:
            self.filters = dict(number__icontains=data['number'])
        if 'position' in data and data['position']:
            self.filters = dict(position__icontains=data['position'])
        return super().get(request)


class CabinetDeleteView(SandboxDeleteView):
    model = Cabinet


