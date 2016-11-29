from waterbutler import settings

config = settings.child('ONEDRIVE_PROVIDER_CONFIG')


BASE_URL = config.get('BASE_URL', 'https://api.onedrive.com/v1.0/drive/items/')
BASE_CONTENT_URL = config.get('BASE_CONTENT_URL', 'https://api.onedrive.com/v1.0/drive/items/')
BASE_ROOT_URL = config.get('BASE_ROOT_URL', 'https://api.onedrive.com/v1.0')
ONEDRIVE_COPY_REQUEST_TIMEOUT = config.get('ONEDRIVE_COPY_REQUEST_TIMEOUT', 60)
ONEDRIVE_ASYNC_REQUEST_SLEEP_INTERVAL = config.get('ONEDRIVE_ASYNC_REQUEST_SLEEP_INTERVAL', 3)
# 10mb
ONEDRIVE_RESUMABLE_UPLOAD_CHUNK_SIZE = config.get('ONEDRIVE_RESUMABLE_UPLOAD_CHUNK_SIZE', 1024 * 1024 * 10)
# 90mb
ONEDRIVE_RESUMABLE_UPLOAD_FILE_SIZE = config.get('ONEDRIVE_RESUMABLE_UPLOAD_FILE_SIZE', 1024 * 1024 * 90)
assert ONEDRIVE_RESUMABLE_UPLOAD_FILE_SIZE > ONEDRIVE_RESUMABLE_UPLOAD_CHUNK_SIZE