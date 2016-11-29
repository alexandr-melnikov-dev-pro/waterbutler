from waterbutler.core import metadata

import logging

logger = logging.getLogger(__name__)


class BaseOneDriveMetadata(metadata.BaseMetadata):

    def __init__(self, raw, path):
        super().__init__(raw)
        self._path = path

    @property
    def id(self):
        return self.raw['id']

    @property
    def provider(self):
        return 'onedrive'

    @property
    def path(self):
        return '/' + self._path.raw_path

    @property
    def materialized_path(self):
        return str(self._path)

    @property
    def extra(self):
        return {
            'id': self.raw['id'],
            'parentReference': self.raw['parentReference']['path']
        }


class OneDriveFolderMetadata(BaseOneDriveMetadata, metadata.BaseFolderMetadata):

    @property
    def name(self):
        return self.raw['name']

    @property
    def etag(self):
        return self.raw.get('eTag')


class OneDriveFileMetadata(BaseOneDriveMetadata, metadata.BaseFileMetadata):

    @property
    def name(self):
        return self.raw['name']

    @property
    def size(self):
        return self.raw.get('size')

    @property
    def modified(self):
        return self.raw.get('lastModifiedDateTime')

    @property
    def content_type(self):
        if 'file' in self.raw.keys():
            return self.raw['file'].get('mimeType')
        return 'application/octet-stream'

    @property
    def extra(self):
        return {
            'id': self.raw.get('id'),
            'etag': self.raw.get('eTag'),
        }

    @property
    def etag(self):
        return self.raw['eTag']


class OneDriveRevision(metadata.BaseFileRevisionMetadata):

    @property
    def version_identifier(self):
        return 'revision'

    @property
    def version(self):
        return self.raw['eTag']

    @property
    def modified(self):
        return self.raw['lastModifiedDateTime']