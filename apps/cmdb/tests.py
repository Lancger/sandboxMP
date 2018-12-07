from django.views.generic.base import View
from django.http import JsonResponse
import logging
import time

info_logger = logging.getLogger('sandbox_info')
error_logger = logging.getLogger('sandbox_error')
from utils.sandbox_utils import SandboxScan, LoginExecution

scan = SandboxScan()
execution = LoginExecution()


class TestLoggingView(View):

    def get(self, request):
        start_time = time.time()
        # data = dict(online_hosts=self.basic_scan())
        # end_time = time.time()
        # work_time = (end_time - start_time)
        # data['work_time'] = work_time
        # kwargs = {'hostname': '172.16.3.102', 'port': 22, 'username': 'root', 'private_key': '/root/.ssh/id_rsa'}

        # hosts = self.basic_scan()
        # key_data = []
        # for host in hosts:
        #     key_kwargs = {'hostname': host, 'port': 22, 'username': 'root', 'private_key': '/root/.ssh/id_rsa'}
        #     data = self.private_key_login_execution(**key_kwargs)
        #     key_data.append(data)
        # data = dict(data=key_data)
        # return JsonResponse(data)

        # key_kwargs = {'hostname': '172.16.3.101', 'port': 22, 'username': 'root', 'private_key': '/root/.ssh/id_rsa'}
        # data = le.private_key_login_execution(**key_kwargs)
        # data['commnds'] = le.get_commands()
        # hosts = scan.get_hosts()
        # data['hosts'] = hosts
        # data['auth_type1'] = le.get_auth_type()
        # data['scan_type'] = le.get_scan_type()
        # key = ['hosts']
        # data = le.get_conf_content(*key)
        kwargs = {
            'hostname': '172.16.3.101',
            'username': execution.get_ssh_username(),
            'port': execution.get_ssh_port(),
            'password': execution.get_ssh_password(),
            'private_key': execution.get_ssh_private_key()
        }
        defaults = execution.login_execution(auth_type='private_key', **kwargs)

        return JsonResponse(defaults)