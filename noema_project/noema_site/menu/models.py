__author__ = 'master'


from django.db.models import Model, CharField, AutoField, ForeignKey


class Menu(Model):
    id = AutoField(primary_key=True)
    code = CharField(max_length=16)
    name = CharField(max_length=32)

    def __unicode__(self):
        return ' | '.join([self.code, self.name])

    class Meta:
        db_table = 'menu'


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