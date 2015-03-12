__author__ = 'master'

from django.shortcuts import render_to_response

from noema_site.menu.models import Menu
from noema_site.context.context import get_context_list
from noema_site.action.action import get_action_list

def standard_view(template, current_menu):
    menu_list = get_context_list(Menu.get_menu_item_list('noema'))
    submenu_list = get_context_list(Menu.get_submenu_item_list('noema', current_menu))
    def decor(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result['menu_list'] = menu_list
            result['submenu_list'] = submenu_list
            result['action_list'] = get_action_list()
            return render_to_response(template, result)
        return wrapper
    return decor

def view(template):
    def decor(func):
        def wrapper(*args, **kwargs):
            return render_to_response(template, func(*args, **kwargs))
        return wrapper
    return decor

