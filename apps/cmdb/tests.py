from django.test import TestCase

# Create your tests here.
from django.views.generic.base import View, TemplateView
from django.shortcuts import HttpResponse
import logging
import datetime

info_logger = logging.getLogger('sandbox_info')
error_logger = logging.getLogger('sandbox_error')


class TestLoggingView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = {'changed_by': '管理员', 'history_type': 'update',
                   'history_date': datetime.datetime(2019, 1, 13, 12, 23, 33, 946528),
                   'changes': {'network_type': [5, 4], 'service_type': [12, 10], 'dev_cabinet': [6, 4], 'leader': [2, 1]}}
        return context
