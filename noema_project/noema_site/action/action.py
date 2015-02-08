__author__ = 'master'


class ActionBase(object):
    def __init__(self, url, name):
        self._url = url
        self._name = name

    @property
    def url(self):
        return self._url

    @property
    def name(self):
        return self._name
