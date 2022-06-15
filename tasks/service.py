import os
from invoke import task
from .config import *

@task()
def collector_run(conf):
    """Run collector service"""
    service_name = 'collector'
    cmd = f"cd {os.path.join(SERVER_STUBS_BASE_OUTPUT_PATH, service_name, 'python', 'src')} && PYTHONPATH={service_name} uvicorn collector.main:app --host 0.0.0.0 --port 8000 --log-level debug"
    conf.run(cmd)