import multiprocessing
from oslo_concurrency import processutils
import os
from shakenfist_utilities import logs

from .config import config


LOG, _ = logs.setup('magnolia')


def main():
    LOG.info('Starting')

    worker_count = multiprocessing.cpu_count() * 2 + 1
    os.makedirs(config.PID_FILE_DIR, exist_ok=True)
    os.makedirs(config.QUEUE_DIR, exist_ok=True)

    cmd = config.API_COMMAND_LINE % {
        'port': config.API_PORT,
        'timeout': config.API_TIMEOUT,
        'name': 'magnolia',
        'pid_file_dir': config.PID_FILE_DIR,
        'queue_dir': config.QUEUE_DIR,
        'workers': worker_count
    }
    LOG.info('Executing %s' % cmd)
    processutils.execute(cmd, check_exit_code=[0, 1, -15], shell=True)
    LOG.info('gunicorn ended')
