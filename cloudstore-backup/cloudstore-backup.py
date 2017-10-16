import logging
from .root_backup import RootBackup
from .gcs import Gcs

logger = logging.getLogger(__name__)


# Root backup
root_backup = RootBackup()
backup_file = root_backup.backup()
gcs = Gcs()

if backup_file is not None:
    gcs.upload(backup_file)