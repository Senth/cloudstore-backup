import logging
from subprocess import call

logger = logging.getLogger(__name__)


class Gcs:
    def upload(self, file):
        gsutil_cp_command = ['gsutil', 'cp']
        if type(file) is list or type(file) is tuple:
            gsutil_cp_command.extend(file)
        else:
            gsutil_cp_command.append(file)
        call(gsutil_cp_command)
        return True

    def rsync(self, dirs):
        # TODO
        return None

