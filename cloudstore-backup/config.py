# Configuration variables for the backup

# Location to store temporary tar.gz and gpg objects (preferably somewhere with large amounts of storage)
TMP_STORE_DIR = '/mnt/lvm/temp'

# Place mysqldump user and password in ~/.my.cnf (with permission 600)
BACKUP_MYSQL = True

# Backup root directories
ROOT_BACKUP_DIRS = [
    '/bin',
    '/boot',
    '/etc',
    '/lib32',
    '/lib64',
    '/opt',
    '/root',
    '/usr',
    '/var',
]

# Media backup rsync directories
MEDIA_BACKUP_DIRS = [
    '/mnt/lvm/appz',
    '/mnt/lvm/audiobooks',
    '/mnt/lvm/ebooks',
    '/mnt/lvm/games',
    '/mnt/lvm/movies/Documentaries',
    '/mnt/lvm/music',
    '/mnt/lvm/other movies',
    '/mnt/lvm/personal development',
    '/mnt/lvm/pron/Wet',
    '/mnt/lvm/senth',
    '/mnt/lvm/spiddekauga',
    '/mnt/lvm/users',
]

# Encrypt name for GPG
ENCRYPT_NAME = 'senth.wallace@gmail.com'

# Days to keep root backup
DAYS_TO_KEEP_ROOT = 60

# GCS location
GCS_BUCKET = 'gs://spiddekauga-backup'
GCS_MEDIA_DIR = '/lvm/'