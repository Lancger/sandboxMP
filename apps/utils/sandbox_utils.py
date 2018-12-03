import os

from django.conf import settings

import nmap
import yaml
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sandboxMP.settings')
error_logger = logging.getLogger('sandbox_error')


class SandboxScan(object):

    config_file = None

    def basic_scan(self):
        """
        Use ICMP discovery online hosts and return online hosts.

        """
        hosts = self.get_hosts()
        nm = nmap.PortScanner()
        nm.scan(hosts=hosts, arguments='-n -sP -PE')
        return nm.all_hosts()

    def os_scan(self):
        """
        Get the system type by nmap scan and return hosts list with os type.
        """
        hosts = self.get_hosts()
        nm = nmap.PortScanner()
        nm.scan(hosts=hosts, arguments='-n sS -O')
        online_hosts = []
        for host in nm.all_hosts():
            try:
                os = nm[host]['osmatch'][0]['osclass'][0]['osfamily']
            except Exception:
                os = 'unknown'
            host_dict = {'host': host, 'os': os}
            online_hosts.append(host_dict)
        return online_hosts

    def get_hosts(self, hosts=None):
        """
        Return the hosts that will be used to scan.
        Subclasses can override this to return any hosts.
        """
        if hosts is None:
            _config = self.get_config_file()
            with open(_config) as f:
                scan_hosts_info = yaml.load(f)
                try:
                    hosts_list = scan_hosts_info['hosts']['net_address']
                    hosts = ' '.join(str(i) for i in hosts_list)
                    return hosts
                except Exception:
                    msg = '{}.get_hosts() is missing a hosts.'.format(self.__class__.__name__)
                    error_logger.error(msg)
                    raise TypeError(msg)
        return hosts

    def get_config_file(self):
        """
        Return 'config_file' that will be used to look up the scan hosts IP,
        network, range of IP, or other config settings.
        This method is called by the default implementation of get_hosts(),
        """

        if self.config_file is None:
            config_file = os.path.join(os.path.join(settings.BASE_DIR, 'config'), 'scanhosts.yml')
            if os.path.exists(config_file):
                return config_file
            else:
                msg = ' %(cls)s is missing a config file. Define %(cls)s.config_file, ' \
                      'or override %(cls)s.get_config_file().' % {'cls': self.__class__.__name__}
                error_logger.error(msg)
                raise AttributeError(msg)

        return self.config_file



