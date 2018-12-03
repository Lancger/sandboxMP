from django.views.generic.base import View
from django.http import JsonResponse
import logging
import time

info_logger = logging.getLogger('sandbox_info')
error_logger = logging.getLogger('sandbox_error')
from utils.sandbox_utils import SandboxScan


class TestLoggingView(SandboxScan, View):

    def get(self, request):
        start_time = time.time()
        data = dict(online_hosts=self.basic_scan())
        end_time = time.time()
        work_time = (end_time - start_time)
        data['work_time'] = work_time
        return JsonResponse(data)

