__author__ = 'master'


from django.db.models import Model, CharField, AutoField, ForeignKey

from noema_site.context.context import ModelItemContext


class Menu(Model):
    id = AutoField(primary_key=True)
    code = CharField(max_length=16)
    name = CharField(max_length=32)

    def __unicode__(self):
        return ' | '.join([self.code, self.name])

    class Meta:
        db_table = 'menu'

    @classmethod
    def get_noema_menu_item_list(cls):
        return MenuItem.objects.filter(menu=cls.objects.get(code='noema')).all()


class MenuItem(Model):
    id = AutoField(primary_key=True)
    code = CharField(max_length=16)
    name = CharField(max_length=32)
    parent = ForeignKey('self', null=True, default=None, blank=True)
    menu = ForeignKey(Menu, null=True, default=None, blank=True)

    def __unicode__(self):
        return ' | '.join([self.code, self.name])

    class Meta:
        db_table = 'menu_item'


    def context(self, alias={}):
        return ModelItemContext(self).compile()