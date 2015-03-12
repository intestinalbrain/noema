# coding: utf-8


def create_menus(apps, schema_editor):
    noema_menu_schema = {'news': {'name': u'Новости',
                                  'parent': None},
                         'poster': {'name': u'Афиша',
                                    'parent': None},
                         'gallery': {'name': u'Галерея',
                                     'parent': None},
                         'photo': {'name': u'Фото',
                                   'parent': 'gallery'},
                         'video': {'name': u'Видео',
                                   'parent': 'gallery'},
                         'discography': {'name': u'Дискография',
                                         'parent': None},
                         'band': {'name': u'О группе',
                                  'parent': None}}

    Menu = apps.get_model('noema_site', 'Menu')
    menu = Menu(code='noema', name='noema')
    menu.save()

    parents = {}

    MenuItem = apps.get_model('noema_site', 'MenuItem')

    def _add_menu(code, attrs):
        name = attrs['name']
        parent_code = attrs['parent']
        if parent_code:
            if parent_code in parents:
                parent = MenuItem.objects.get(id=parents[parent_code])
            else:
                parent_attrs = noema_menu_schema[parent_code]
                parent = _add_menu(parent_code, parent_attrs)
                parent_id = parent.id
                parents[parent_code] = parent_id
        else:
            parent = None

        menu_item = MenuItem(code=code, name=name, parent=parent, menu=menu)
        menu_item.save()
        return menu_item


    for code, attrs in noema_menu_schema.items():
        if code in parents:
            continue
        menu_item = _add_menu(code, attrs)
        parents[menu_item.code] = menu_item.id
