import os
from invoke import task
from .config import *


@task()
def event_collector_testing(conf):
    """Run event collector testing"""
    service_name = 'collector'
    cmd = f"cd {os.path.join(SERVER_STUBS_BASE_OUTPUT_PATH, service_name, 'python', 'src', service_name)} && PYTHONPATH=.. pytest  --disable-pytest-warnings -sv tests"
    conf.run(cmd)