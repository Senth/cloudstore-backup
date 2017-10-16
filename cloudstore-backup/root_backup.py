import logging
from datetime import date
from subprocess import call
from os import remove, path
from .config import TMP_STORE_DIR, ROOT_BACKUP_DIRS, ENCRYPT_NAME, BACKUP_MYSQL

logger = logging.getLogger(__name__)

CUR_DATE = date.today().strftime('%Y-%m-%d')


class RootBackup:
    MYSQLDUMP_FILE = '/tmp/mysqldump.sql'
    TAR_FILE = TMP_STORE_DIR + '/root-backup.tgz'
    GPG_FILE = TMP_STORE_DIR + '/root-backup-' + CUR_DATE + '.gpg'
    GPG_COMMAND = [
        'gpg',
        '-o', GPG_FILE,
        '-r', ENCRYPT_NAME,
        '--batch',
        '--no-tty',
        '--encrypt', TAR_FILE
    ]

    def __init__(self):
        self.dirs_to_backup = list()
        self.dirs_to_backup.extend(ROOT_BACKUP_DIRS)

    def backup(self):
        """:return backup file name, None if failed"""
        # Backup mysql database
        if BACKUP_MYSQL:
            self._dump_mysql()
            self.dirs_to_backup.append(RootBackup.MYSQLDUMP_FILE)

        # Tar everything
        call(['mount', '/boot'])
        tar_command = ['tar', 'czf', RootBackup.TAR_FILE]
        tar_command.extend(self.dirs_to_backup)
        call(tar_command)

        # Encrypt the tar
        if path.isfile(RootBackup.TAR_FILE):
            call(RootBackup.GPG_COMMAND)

        # Return if successful
        if path.isfile(RootBackup.GPG_FILE):
            return RootBackup.GPG_FILE
        else:
            return None

    def _cleanup(self):
        if BACKUP_MYSQL:
            remove(RootBackup.MYSQLDUMP_FILE)
        remove(RootBackup.TAR_FILE)
        call(['umount', '/boot'])
        # Don't remove the gpg file yet, we have to upload it first!

    def _dump_mysql(self):
        call(['mysqldump', '--all-databases', '>', RootBackup.MYSQLDUMP_FILE])