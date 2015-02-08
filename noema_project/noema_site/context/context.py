__author__ = 'master'

class ContextBase(object):
    def __init__(self, item):
        self._item = item

    def compile(self):
        return {}

class ModelItemContext(ContextBase):
    def __init__(self, model_item):
        ContextBase.__init__(self, model_item)

    def compile(self, alias={}):
        result = {}
        for field in self._item._meta._field_name_cache:
            field_name = field.get_attname()
            field_name = alias.get(field_name, field_name)
            result[field_name] = getattr(self._item, field_name)
        return result

def get_context_list(obj_list, alias={}):
    return [obj.context(alias=alias) for obj in obj_list]

