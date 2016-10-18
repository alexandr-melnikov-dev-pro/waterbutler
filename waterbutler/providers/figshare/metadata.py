from waterbutler.core import metadata
from waterbutler.core.provider import build_url

from waterbutler.providers.figshare import settings


class BaseFigshareMetadata(metadata.BaseMetadata):

    @property
    def provider(self):
        return 'figshare'


class FigshareFileMetadata(BaseFigshareMetadata, metadata.BaseFileMetadata):

    def __init__(self, raw, raw_file=None):
        super().__init__(raw)
        if raw_file:
            self.raw_file = raw_file
        else:
            self.raw_file = self.raw['files'][0]

    @property
    def id(self):
        return self.raw_file['id']

    @property
    def name(self):
        return self.raw_file['name']

    @property
    def path(self):
        return '/{0}/{1}'.format(self.article_id, self.raw_file['id'])

    @property
    def materialized_path(self):
        return '/{0}/{1}'.format(self.article_name, self.name)

    @property
    def article_id(self):
        return self.raw['id']

    @property
    def article_name(self):
        return self.raw['title']

    @property
    def content_type(self):
        return None

    @property
    def size(self):
        return self.raw_file['size']

    @property
    def modified(self):
        return None

    @property
    def etag(self):
        return '{}::{}'.format(self.raw['status'].lower(),
                               self.article_id,
                               self.raw_file['computed_md5'])

    @property
    def is_public(self):
        return (settings.PRIVATE_IDENTIFIER not in self.raw['url'])

    @property
    def web_view(self):
        if self.is_public:
            segments = ('articles', str(self.article_id))
        else:
            segments = ('account', 'articles', str(self.article_id))
        return build_url(settings.VIEW_URL, *segments)

    @property
    def can_delete(self):
        """Files can be deleted if not public."""
        return (not self.is_public)

    @property
    def extra(self):
        return {
            'fileId': self.raw_file['id'],
            'articleId': self.article_id,
            'status': self.raw['status'].lower(),
            'downloadUrl': self.raw_file['download_url'],
            'canDelete': self.can_delete,
            'webView': self.web_view
        }


class FigshareFolderMetadata(BaseFigshareMetadata,
                             metadata.BaseFolderMetadata):
    """Default config only allows articles of defined_type fileset to be
    considered folders.
    """

    @property
    def id(self):
        return self.raw['id']

    @property
    def name(self):
        return self.raw['title']

    @property
    def path(self):
        return '/{0}/'.format(self.raw.get('id'))

    @property
    def materialized_path(self):
        return '/{0}/'.format(self.name)

    @property
    def size(self):
        return None

    @property
    def modified(self):
        return self.raw['modified_date']

    @property
    def etag(self):
        return '{}::{}::{}'.format(self.raw['status'].lower(), self.raw.get('doi'), self.raw.get('id'))

    @property
    def extra(self):
        return {
            'id': self.raw.get('id'),
            'doi': self.raw.get('doi'),
            'status': self.raw['status'].lower(),
        }
