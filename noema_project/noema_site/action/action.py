__author__ = 'master'


class ActionBase(object):
    def __init__(self, name):
        self._url = 'action/%s' % name
        self._name = name

    @property
    def url(self):
        return self._url

    @property
    def name(self):
        return self._name


class ActionCreator(object):
    cache = {}
    order = []
    all = []

    @classmethod
    def get(cls, type_):
        return cls.cache[type_]

    @classmethod
    def set(cls, type_):
        action = ActionBase(type_)
        cls.order.append(type_)
        cls.cache[type_] = action
        cls.all.append(action)

ActionCreator.set('add')
ActionCreator.set('edit')
ActionCreator.set('delete')


def get_action_list():
    return ActionCreator.all