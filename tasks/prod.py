import os
from invoke import task
from .config import *


def deploy_service(config, service_name, service_path, server_root_path, user, host, need_restart=True):
    print(f"Deploy {service_name}")
    cmd = f"rsync -uazp {service_path} {user}@{host}:{server_root_path}"
    res = config.run(cmd)
    if need_restart:
        print(f"Restart {service_name}")
        cmd = f"ssh {user}@{host} 'systemctl restart {service_name}'"
        res = config.run(cmd)
    return True
