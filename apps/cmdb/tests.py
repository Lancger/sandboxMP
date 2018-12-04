from django.views.generic.base import View
from django.http import JsonResponse
import logging
import time

info_logger = logging.getLogger('sandbox_info')
error_logger = logging.getLogger('sandbox_error')
from utils.sandbox_utils import SandboxScan, LoginExecution


class TestLoggingView(SandboxScan, LoginExecution, View):

    def get(self, request):
        start_time = time.time()
        # data = dict(online_hosts=self.basic_scan())
        # end_time = time.time()
        # work_time = (end_time - start_time)
        # data['work_time'] = work_time
        # kwargs = {'hostname': '172.16.3.101', 'port': 22, 'username': 'root', 'password': 'leadsec@7766'}
        # password_data = self.password_login_execution(**kwargs)
        key_kwargs = {'hostname': '172.16.3.101', 'port': 22, 'username': 'root', 'private_key': '/root/.ssh/id_rsa'}
        key_data = self.private_key_login_execution(**key_kwargs)

        return JsonResponse(key_data)

